from typing import (
    Optional,
    Dict
)
from abc import ABC, abstractmethod


class VKPayAction(ABC):

    @abstractmethod
    def generate_hash(self) -> str:
        raise NotImplementedError('VKPayAction is abstract class')


class VKPayActionPayToGroup(VKPayAction):
    """
    Платёж в пользу сообщества с заданной суммой
    """

    def __init__(
        self,
        amount: int,
        group_id: int,
        description: Optional[str] = None,
        data: Optional[Dict[str, str]] = None
    ):
        """
        :param amount: сумма платежа в рублях. Минимальное значение — 1;
        :param group_id: идентификатор сообщества
        :param description: описание платежа
        """
        self._action: str = 'pay-to-group'
        self._amount: int = amount
        self._group_id: int = group_id
        self._description: Optional[str] = description
        self._data: Optional[Dict[str, str]] = data

    def generate_hash(self) -> str:
        _hash: str = f'action={self._action}&group_id={self._group_id}&amount={self._amount}'
        if self._description is not None:
            _hash += f'&description={self._description}'
        if self._data is not None:
            _hash += f'&data={self._data}'

        return _hash


class VKPayActionPayToUser(VKPayAction):
    """
    Платёж с заданной суммой пользователю
    """

    def __init__(
        self,
        amount: int,
        user_id: int,
        description: Optional[str] = None
    ):
        """
        :param amount: сумма платежа в рублях. Минимальное значение — 1;
        :param user_id: идентификатор пользователя
        :param description: описание платежа
        """
        self._action: str = 'pay-to-user'
        self._amount: int = amount
        self._user_id: int = user_id
        self._description: Optional[str] = description

    def generate_hash(self) -> str:
        _hash: str = f'action={self._action}&user_id={self._user_id}&amount={self._amount}'
        if self._description is not None:
            _hash += f'&description={self._description}'

        return _hash


class VKPayActionTransferToGroup(VKPayAction):
    """
    Перевод сообществу произвольной суммы
    """

    def __init__(
        self,
        group_id: int,
        description: Optional[str] = None
    ):
        """
        :param group_id: идентификатор сообщества
        :param description: описание платежа
        """
        self._action: str = 'transfer-to-group'
        self._group_id: int = group_id
        self._description: Optional[str] = description

    def generate_hash(self) -> str:
        _hash: str = f'action={self._action}&group_id={self._group_id}'
        if self._description is not None:
            _hash += f'&description={self._description}'
        return _hash

class VKPayActionTransferToUser(VKPayAction):
    """
    Перевод пользователю произвольной суммы
    """

    def __init__(
        self,
        user_id: int,
        description: Optional[str] = ''
    ):
        """
        :param user_id: идентификатор пользователя
        :param description: описание платежа
        """
        self._action: str = 'transfer-to-group'
        self._user_id: int = user_id
        self._description: Optional[str] = description

    def generate_hash(self) -> str:
        _hash: str = f'action={self._action}&user_id={self._user_id}'
        if self._description is not None:
            _hash += f'&description={self._description}'
        return _hash
