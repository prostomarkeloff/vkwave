from vkwave_types.bot_events import *


def test_group_join_event():
    event = get_event_object(
        {
            "type": "group_join",
            "object": {"user_id": 1, "join_type": "approved"},
            "group_id": 123,
        }
    )
    assert event.object.join_type == "approved"
    assert event.object.user_id == 1
    assert event.group_id == 123

