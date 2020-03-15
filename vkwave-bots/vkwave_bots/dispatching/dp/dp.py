from vkwave_bots.types.bot_type import BotType
from vkwave_bots.tokens.storage import TokenStorage
from vkwave_api.methods import API
from vkwave_bots.tokens.types import GroupId, UserId
from vkwave_types.bot_events import get_event_object
from vkwave_types.user_events import get_event_object as user_get_event_object
from vkwave_bots.dispatching.events.base import BaseEvent, BotEvent, UserEvent
from vkwave_bots.dispatching.router.router import BaseRouter, HANDLER_NOT_FOUND
from vkwave_api.token.token import AnyABCToken
from vkwave_types.objects import GroupsGroup
from .processing_options import ProcessEventOptions
from typing import NewType, Optional, List, cast
from .middleware.middleware import MiddlewareManager
from vkwave_bots.dispatching.extensions.base import ExtensionEvent
from .result_caster import ResultCaster
from asyncio import get_running_loop

ProcessingResult = NewType("ProcessingResult", bool)


class Dispatcher:
    def __init__(
        self, api: API, token_storage: TokenStorage, bot_type: BotType = BotType.BOT
    ):
        self.bot_type: BotType = bot_type
        self.api: API = api
        self.middleware_manager = MiddlewareManager()
        self.token_storage: TokenStorage = token_storage
        self.routers: List[BaseRouter] = []
        self.result_caster: ResultCaster = ResultCaster()

    def add_router(self, router: BaseRouter):
        self.routers.append(router)

    async def process_event(
        self, revent: ExtensionEvent, options: Optional[ProcessEventOptions] = None
    ) -> ProcessingResult:
        event: BaseEvent
        if revent.bot_type is BotType.BOT:
            revent.raw_event = cast(dict, revent.raw_event)
            group_id = revent.raw_event["group_id"]
            token = await self.token_storage.get_token(GroupId(group_id))
            event = BotEvent(
                get_event_object(revent.raw_event), self.api.with_token(token)
            )
        else:
            revent.raw_event = cast(list, revent.raw_event)
            obj = user_get_event_object(revent.raw_event)
            user_id = obj.peer_id
            token = await self.token_storage.get_token(UserId(user_id))
            event = UserEvent(obj, self.api.with_token(token))

        if not await self.middleware_manager.execute_pre_process_event(event):
            return ProcessingResult(False)
        for router in self.routers:
            if await router.is_suitable(event):
                result = await router.process_event(event)
                if result is HANDLER_NOT_FOUND:
                    continue
                await self.result_caster.cast(result, event)
                return ProcessingResult(True)
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
