from vkwave_client.abstract import AbstractAPIClient
from vkwave_api.token.token import AnyABCToken, Token
from vkwave_api.token.strategy import ABCGetTokenStrategy, RandomGetTokenStrategy
from vkwave_api.methods._error import ErrorDispatcher, Error
from typing import Optional, Tuple, List, Union, AsyncGenerator
from .account import Account
from .ads import Ads
from .app import App
from .apps import Apps
from .auth import Auth
from .board import Board
from .database import Database
from .docs import Docs
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
from .storage import Storage
from .stories import Stories
from .streaming import Streaming
from .users import Users
from .utils import Utils
from .video import Video
from .wall import Wall
from .widgets import Widgets


from contextlib import asynccontextmanager
from .status import Status

import copy
import random


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

    async def _get_token(self) -> Token:
        return await self.api_options.get_token_strategy.get_token(
            self.api_options.tokens
        )

    async def _get_client(self) -> AbstractAPIClient:
        # TODO: maybe get_client_strategy
        return random.choice(self.api_options.clients)

    async def get_client_and_token(self) -> Tuple[AbstractAPIClient, Token]:
        return await self._get_client(), await self._get_token()

    def update_pre_request_params(self, params: dict, token: Token) -> dict:
        params.update(v=self.api_options.api_version, access_token=token)
        return params

    @asynccontextmanager
    async def sync_token(self) -> AsyncGenerator["APIOptionsRequestContext", None]:
        """Grab random token and work only with it"""
        copied = copy.copy(self.api_options)
        copied.tokens = [random.choice(copied.tokens)]
        new = APIOptionsRequestContext(copied)
        yield new
        del copied
        del new


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

    @staticmethod
    def with_options(options: APIOptions) -> APIOptionsRequestContext:
        return APIOptionsRequestContext(options)
