import typing
from enum import Enum, auto
from vkwave_api.token.token import (
    ABCUserSyncToken as UST,
    ABCUserAsyncToken as UAT,
    ABCBotSyncToken as BST,
    ABCBotAsyncToken as BAT,
)
GroupId = typing.NewType("GroupId", int)
UserId = typing.NewType("UserId", int)
AnyId = typing.Union[GroupId, UserId]

AnyUserToken = typing.Union[UST, UAT]
AnyBotToken = typing.Union[BST, BAT]
AnyToken = typing.Union[AnyUserToken, AnyBotToken]
