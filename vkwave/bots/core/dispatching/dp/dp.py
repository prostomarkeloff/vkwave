import logging
from typing import List, NewType, Optional, cast, Union

from vkwave.api.methods import API
from vkwave.api.token.token import AnyABCToken
from vkwave.bots.core.dispatching.events.base import BaseEvent, BotEvent, UserEvent
from vkwave.bots.core.dispatching.events.raw import ExtensionEvent
from vkwave.bots.core.dispatching.router.router import HANDLER_NOT_FOUND, BaseRouter
from vkwave.bots.core.tokens.storage import TokenStorage, UserTokenStorage
from vkwave.bots.core.tokens.types import GroupId
from vkwave.bots.core.types.bot_type import BotType
from vkwave.types.bot_events import get_event_object
from vkwave.types.user_events import get_event_object as user_get_event_object

from .middleware.middleware import MiddlewareManager
from .processing_options import ProcessEventOptions
from .result_caster import ResultCaster

ProcessingResult = NewType("ProcessingResult", bool)

logger = logging.getLogger(__name__)


class Dispatcher:
    def __init__(
        self,
        api: API,
        token_storage: Union[TokenStorage, UserTokenStorage],
        bot_type: BotType = BotType.BOT,
    ):
        self.bot_type: BotType = bot_type
        self.api: API = api
        self.middleware_manager = MiddlewareManager()
        self.token_storage: Union[TokenStorage, UserTokenStorage] = token_storage
        self.routers: List[BaseRouter] = []
        self.result_caster: ResultCaster = ResultCaster()

    def add_router(self, router: BaseRouter):
        self.routers.append(router)

    async def process_event(
        self, revent: ExtensionEvent, options: ProcessEventOptions
    ) -> ProcessingResult:
        event: BaseEvent

        logger.debug(f"ProcessEventOptions:\n{options}")
        logger.debug(f"New event! Raw:\n{revent}")

        if options.do_not_handle:
            logger.debug("ProcessEventOptions.do_not_handle is True")
            logger.debug("Event was skipped")
            return ProcessingResult(False)

        if revent.bot_type is BotType.BOT:
            revent.raw_event = cast(dict, revent.raw_event)
            group_id = revent.raw_event["group_id"]
            token = await self.token_storage.get_token(GroupId(group_id))
            event = BotEvent(get_event_object(revent.raw_event), self.api.with_token(token))
        else:
            revent.raw_event = cast(list, revent.raw_event)
            obj = user_get_event_object(revent.raw_event)
            event = UserEvent(obj, self.api.with_token(self.token_storage.current_token))

        logger.debug(f"New event! Formatted:\n{event}")

        if not await self.middleware_manager.execute_pre_process_event(event):
            return ProcessingResult(False)
        for router in self.routers:
            if await router.is_suitable(event):
                result = await router.process_event(event)
                if result is HANDLER_NOT_FOUND:
                    continue
                await self.result_caster.cast(result, event)
                logger.debug("Event was succesfully handled")
                return ProcessingResult(True)
        logger.debug("Event wasn't handled")
        return ProcessingResult(False)

    async def cache_potential_tokens(self, tokens: Optional[List[AnyABCToken]] = None):
        tokens_to_cache = self.api.default_api_options.tokens.copy()
        if tokens is not None:
            tokens_to_cache.extend(tokens)

        for token in tokens_to_cache:
            ctx = self.api.with_token(token)
            id_to_cache: int
            if self.bot_type is BotType.BOT:
                groups = (await ctx.groups.get_by_id()).response
                id_to_cache = cast(int, groups[0].id)
            else:
                users = (await ctx.users.get()).response
                id_to_cache = cast(int, users[0].id)
            self.token_storage.append(id_to_cache, token)
