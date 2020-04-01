import typing

from vkwave.api.token.token import ABCBotAsyncToken as BAT
from vkwave.api.token.token import ABCBotSyncToken as BST
from vkwave.api.token.token import ABCUserAsyncToken as UAT
from vkwave.api.token.token import ABCUserSyncToken as UST

GroupId = typing.NewType("GroupId", int)
UserId = typing.NewType("UserId", int)
AnyId = typing.Union[GroupId, UserId]

AnyUserToken = typing.Union[UST, UAT]
AnyBotToken = typing.Union[BST, BAT]
AnyToken = typing.Union[AnyUserToken, AnyBotToken]
