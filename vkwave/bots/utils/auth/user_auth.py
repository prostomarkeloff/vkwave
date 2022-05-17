from typing import Union, Dict, Optional

from vkwave.bots.utils.auth.types import OAuthResponse
from vkwave.bots.utils.auth.errors import AuthError
from vkwave.bots.utils.auth import BaseTwoAuth
from vkwave.http import AIOHTTPClient


class TwoAuth(BaseTwoAuth):
    async def get_code(self) -> int:
        code = int(input('Input 2FA code: '))
        return code


class Auth:
    auth_url: str = 'https://oauth.vk.com/token'
    data: Dict[str, Union[int, str]] = {
        'grant_type': 'password'
    }

    def __init__(
        self,
        client_id: int,
        client_hash: str, client: Optional[AIOHTTPClient] = None,
        two_auth: Optional[BaseTwoAuth] = None,
    ):
        self.client = client or AIOHTTPClient()
        self.two_auth = two_auth or TwoAuth()
        self.client_id = client_id
        self.client_hash = client_hash
        self.data.update({
            'client_id': self.client_id,
            'client_secret': self.client_hash
        })

    async def auth(
        self,
        login: str,
        password: str,
        two_auth: bool = False,
        two_auth_code: Optional[int] = None
    ) -> OAuthResponse:
        self.data.update({
            'username': login,
            'password': password,
            '2fa_supported': 1,
            'force_sms': int(two_auth)
        })
        if two_auth_code:
            self.data.update({
                'code': two_auth_code
            })

        response = await self.client.request_json(
            method='post',
            url=self.auth_url,
            data=self.data
        )

        if response.get('validation_type'):
            code = await self.two_auth.get_code()
            return await self.auth(login, password, True, code)
        if not response.get('access_token'):
            raise AuthError(response)

        return OAuthResponse(**response)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.close()
