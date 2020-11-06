from typing import Optional, Dict
from abc import ABC, abstractmethod


class VKPayAction(ABC):

    @abstractmethod
    def generate_hash(self) -> str:
        raise NotImplementedError('VKPayAction is abstract class')


class VKPayActionPayToGroup(VKPayAction):
    """
    Payment to the group with the specified amount
    """

    def __init__(
        self,
        amount: int,
        group_id: int,
        description: Optional[str] = None,
        data: Optional[Dict[str, str]] = None
    ):
        """
        :param amount: the amount of payment in rubles. The minimum value is 1;
        :param group_id:
        :param description: payment description
        :param data: dictionary with custom parameters (from vk api docs)
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
    Payment with the specified amount to the user
    """

    def __init__(
        self,
        amount: int,
        user_id: int,
        description: Optional[str] = None
    ):
        """
        :param amount: the amount of payment in rubles. The minimum value is 1;
        :param user_id:
        :param description: payment description
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
    Transfer of any amount to the group
    """

    def __init__(
        self,
        group_id: int,
        description: Optional[str] = None
    ):
        """
        :param group_id:
        :param description: payment description
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
    Transfer of any amount to the user
    """

    def __init__(
        self,
        user_id: int,
        description: Optional[str] = ''
    ):
        """
        :param user_id:
        :param description: payment description
        """
        self._action: str = 'transfer-to-group'
        self._user_id: int = user_id
        self._description: Optional[str] = description

    def generate_hash(self) -> str:
        _hash: str = f'action={self._action}&user_id={self._user_id}'
        if self._description is not None:
            _hash += f'&description={self._description}'
        return _hash
