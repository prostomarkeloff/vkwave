from typing import Optional, Sequence, AsyncGenerator

from vkwave.api import APIOptionsRequestContext
from vkwave.http import AbstractHTTPClient, AbstractWSClient
from .errors import StreamingAPIError
from .model import StreamingClientData, Rule, StreamingMessage


class StreamingClient:
    def __init__(
        self,
        api_context: APIOptionsRequestContext,
        http_client: AbstractHTTPClient,
        ws_client: AbstractWSClient,
    ):
        self._api: APIOptionsRequestContext = api_context
        self._http_client = http_client
        self._ws_client = ws_client
        self._data: Optional[StreamingClientData] = None

    async def add_rule(self, value: str, tag: str):
        await self._req_server("POST", data={"rule": Rule(value=value, tag=tag).dict()})

    async def get_rules(self) -> Sequence[Rule]:
        response = await self._req_server("GET")
        if response.get("rules") is None:
            return []
        return [Rule.parse_obj(rule) for rule in response.get("rules")]

    async def delete_rule(self, tag: str):
        await self._req_server("DELETE", data={"tag": tag})

    async def delete_all_rules(self):
        rules = await self.get_rules()
        for rule in rules:
            await self.delete_rule(tag=rule.tag)

    async def _get_server(self, force: bool = False):
        if not self._data or force:
            self._data = await StreamingClientData.get(self._api)
        return self._data.key, self._data.endpoint

    async def _req_server(self, method: str, data: Optional[dict] = None) -> dict:
        key, endpoint = await self._get_server()
        url = f"https://{endpoint}/rules?key={key}"

        r = await self._http_client.request_send_json(method, url, json=data)
        code = r.get("code")
        if code != 200:
            error = r.get("error", {})
            raise StreamingAPIError(
                code=error.get("error_code"), message=error.get("message"),
            )

        return r

    async def stream(self) -> AsyncGenerator[None, StreamingMessage]:
        key, endpoint = await self._get_server()
        await self._ws_client.connect(f"https://{endpoint}/stream?key={key}")
        async for data in self._ws_client.stream_json():
            if data["code"] != 100:
                raise StreamingAPIError(
                    code=data["code"], message=data["service_message"],
                )
            yield StreamingMessage(**data)
