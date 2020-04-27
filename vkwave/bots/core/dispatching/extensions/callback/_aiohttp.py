from asyncio import get_running_loop
from typing import TYPE_CHECKING, Optional

from aiohttp import web

from vkwave.bots.core.dispatching.dp.processing_options import ProcessEventOptions
from vkwave.bots.core.dispatching.events.raw import ExtensionEvent
from vkwave.bots.core.dispatching.extensions.base import BaseExtension
from vkwave.bots.core.tokens.types import GroupId
from vkwave.bots.core.types.bot_type import BotType

from .conf import ConfirmationStorage

if TYPE_CHECKING:
    from vkwave.bots.core.dispatching.dp.dp import Dispatcher


class CallbackView(web.View):
    async def get(self):
        raise web.HTTPForbidden()

    async def post(self):
        event: dict = await self.request.json()
        e_type = event.get("type")
        if not e_type:
            raise web.HTTPForbidden()
        group_id = event["group_id"]

        if e_type == "confirmation":
            return web.Response(
                body=await self.request.app["storage"].get_confirmation(GroupId(group_id))
            )

        if self.request.app["support_secret"]:
            if not event["secret"] == self.request.app["secret"]:
                raise web.HTTPForbidden()

        options = ProcessEventOptions(do_not_handle=False)
        revent = ExtensionEvent(BotType.BOT, event)

        get_running_loop().create_task(self.request.app["dp"].process_event(revent, options))

        return web.Response(body="ok")


class AIOHTTPCallbackExtension(BaseExtension):
    def __init__(
        self,
        dp: "Dispatcher",
        path: str,
        host: str,
        port: int,
        secret: Optional[str] = None,
        confirmation_storage: Optional[ConfirmationStorage] = None,
    ):
        self.confirmation_storage = confirmation_storage or ConfirmationStorage()
        self.secret = secret  # maybe we need secret storage too?
        self.dp = dp

        self.path = path
        self.host = host
        self.port = port

    def add_confirmation(self, group_id: GroupId, confirmation: str):
        self.confirmation_storage.add_confirmation(group_id, confirmation)

    async def _start(self):
        app = web.Application()
        app["secret"] = self.secret
        app["support_secret"] = bool(self.secret)
        app["storage"] = self.confirmation_storage
        app["dp"] = self.dp

        app.router.add_view(self.path, CallbackView)

        runner = web.AppRunner(app)
        await runner.setup()

        site = web.TCPSite(runner, self.host, self.port)
        await site.start()

    async def start(self):
        get_running_loop().create_task(self._start())
