import typing

from vkwave.api import APIOptionsRequestContext
from vkwave.vkscript import execute


@execute
def _get_all_posts_execute(api: APIOptionsRequestContext, wall_owner_id: int, _offset: int):
    calls = 0
    all_posts = []
    offset = _offset

    while calls < 25:
        response = api.wall.get(owner_id=wall_owner_id, count=100, offset=offset)
        all_posts += response.items
        offset += 100
        calls += 1
    return all_posts, offset


class Fetcher:
    @classmethod
    async def get_all_wall_posts_iter(
        cls, api: APIOptionsRequestContext, wall_owner_id: int
    ) -> typing.AsyncIterator[typing.List[dict]]:
        offset = 0

        result = (
            await _get_all_posts_execute(
                api=api,
                wall_owner_id=wall_owner_id,
                _offset=offset,
                return_raw_response=True,
            )
        )["response"]
        executed, offset = result
        yield executed

        while executed:
            result = (
                await _get_all_posts_execute(
                    api=api,
                    wall_owner_id=wall_owner_id,
                    _offset=offset,
                    return_raw_response=True,
                )
            )["response"]
            executed, offset = result
            if executed:
                yield executed
