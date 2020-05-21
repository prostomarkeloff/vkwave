import copy
import random
from contextlib import asynccontextmanager
from typing import AsyncGenerator, List, Optional, Tuple, Union, cast

from vkwave.api.methods._error import (
    APIError,
    Error,
    ErrorDispatcher,
    UnsuccessAPIRequestException,
)
from vkwave.api.token.strategy import ABCGetTokenStrategy, RandomGetTokenStrategy
from vkwave.api.token.token import AnyABCToken, Token
from vkwave.client.abstract import AbstractAPIClient
from vkwave.client.context import ResultState
from vkwave.client.types import MethodName

from .account import Account
from .ads import Ads
from .app import App
from .apps import Apps
from .auth import Auth
from .board import Board
from .database import Database
from .docs import Docs
from .execute import Execute
from .fave import Fave
from .friends import Friends
from .gifts import Gifts
from .groups import Groups
from .leads import Leads
from .likes import Likes
from .market import Market
from .messages import Messages
from .newsfeed import Newsfeed
from .notes import Notes
from .notifications import Notifications
from .orders import Orders
from .pages import Pages
from .photos import Photos
from .polls import Polls
from .pretty import Pretty
from .search import Search
from .secure import Secure
from .stats import Stats
from .status import Status
from .storage import Storage
from .stories import Stories
from .streaming import Streaming
from .users import Users
from .utils import Utils
from .video import Video
from .wall import Wall
from .widgets import Widgets

TokensInput = Union[List[AnyABCToken], AnyABCToken]
ClientsInput = Union[List[AbstractAPIClient], AbstractAPIClient]


class APIOptions:
    def __init__(
        self,
        tokens: TokensInput,
        clients: ClientsInput,
        get_token_strategy: ABCGetTokenStrategy,
        api_version: str,
        error_dispatcher: ErrorDispatcher,
    ):
        self.tokens = tokens if isinstance(tokens, list) else [tokens]
        self.clients = clients if isinstance(clients, list) else [clients]
        self.get_token_strategy = get_token_strategy
        self.api_version: str = api_version
        self.error_dispatcher = error_dispatcher

    def add_token(self, tokens: TokensInput):
        self.tokens.extend(tokens if isinstance(tokens, list) else [tokens])

    def add_client(self, clients: ClientsInput):
        self.clients.extend(clients if isinstance(clients, list) else [clients])

    async def get_token(self) -> Token:
        return await self.get_token_strategy.get_token(self.tokens)

    def get_client(self) -> AbstractAPIClient:
        return random.choice(self.clients)

    async def get_client_and_token(self) -> Tuple[AbstractAPIClient, Token]:
        return self.get_client(), await self.get_token()

    def update_pre_request_params(self, params: dict, token: Token) -> dict:
        params.update(v=self.api_version, access_token=token)
        return params


class APIOptionsRequestContext:
    def __init__(self, api_options: APIOptions):
        self.api_options = api_options

        self.account = Account("account", self)
        self.ads = Ads("ads", self)
        self.app = App("app", self)
        self.apps = Apps("apps", self)
        self.auth = Auth("auth", self)
        self.board = Board("board", self)
        self.database = Database("database", self)
        self.docs = Docs("docs", self)
        self.execute = Execute("execute", self)
        self.fave = Fave("fave", self)
        self.friends = Friends("friends", self)
        self.gifts = Gifts("gifts", self)
        self.groups = Groups("groups", self)
        self.leads = Leads("leads", self)
        self.likes = Likes("likes", self)
        self.market = Market("market", self)
        self.messages = Messages("messages", self)
        self.newsfeed = Newsfeed("newsfeed", self)
        self.notes = Notes("notes", self)
        self.notifications = Notifications("notifications", self)
        self.orders = Orders("orders", self)
        self.pages = Pages("pages", self)
        self.photos = Photos("photos", self)
        self.polls = Polls("polls", self)
        self.pretty = Pretty("pretty", self)
        self.search = Search("search", self)
        self.secure = Secure("secure", self)
        self.stats = Stats("stats", self)
        self.status = Status("status", self)
        self.storage = Storage("storage", self)
        self.stories = Stories("stories", self)
        self.streaming = Streaming("streaming", self)
        self.users = Users("users", self)
        self.utils = Utils("utils", self)
        self.video = Video("video", self)
        self.wall = Wall("wall", self)
        self.widgets = Widgets("widgets", self)

    async def handle_error(self, error: Error) -> Optional[dict]:
        dispatcher = self.api_options.error_dispatcher
        result = await dispatcher.process_error(error, self)
        return result

    @asynccontextmanager
    async def sync_token(self) -> AsyncGenerator["APIOptionsRequestContext", None]:
        """Grab random token and work only with it"""
        copied = copy.copy(self.api_options)
        copied.tokens = [random.choice(copied.tokens)]
        new = APIOptionsRequestContext(copied)
        yield new
        del copied
        del new

    async def api_request(self, method_name: MethodName, params: dict) -> dict:
        client, token = await self.api_options.get_client_and_token()

        params = self.api_options.update_pre_request_params(params, token)
        ctx = client.create_request(method_name, params)
        await ctx.send_request()

        state = ctx.result.state

        exc_data = None
        data = None

        if state is ResultState.UNHANDLED_EXCEPTION:
            exc = cast(Exception, ctx.result.exception)
            raise exc
        if state is ResultState.HANDLED_EXCEPTION:
            exc_data = ctx.result.exception_data
            exc_data = cast(dict, exc_data)
            if not ("error" in exc_data or "response" in exc_data):
                raise UnsuccessAPIRequestException()
        else:
            data = ctx.result.data
            data = cast(dict, data)

        result = data or exc_data
        result = cast(dict, result)

        if "error" in result:
            err_handler_result = await self.handle_error(Error(result))
            if err_handler_result:
                result = err_handler_result

        return result


class API:
    def __init__(
        self,
        tokens: TokensInput,
        clients: ClientsInput,
        get_token_strategy: Optional[ABCGetTokenStrategy] = None,
        api_version: Optional[str] = None,
        error_dispatcher: Optional[ErrorDispatcher] = None,
    ):
        self.default_api_options = APIOptions(
            tokens,
            clients,
            get_token_strategy or RandomGetTokenStrategy(),
            api_version or "5.103",
            error_dispatcher or ErrorDispatcher(),
        )

    def get_context(self) -> APIOptionsRequestContext:
        return APIOptionsRequestContext(self.default_api_options)

    def with_token(self, token: AnyABCToken) -> APIOptionsRequestContext:
        copied = copy.copy(self.default_api_options)
        copied.tokens = [token]
        new = APIOptionsRequestContext(copied)
        return new

    def with_options(self, options: APIOptions) -> APIOptionsRequestContext:
        return APIOptionsRequestContext(options)
