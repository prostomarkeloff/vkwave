import json

from vkwave.types.user_events import ChangedChatSettingsType, TimeoutUserEnum, get_event_object


def test_message_new_event():
    event = get_event_object(
        [
            4,
            174167,
            2629633,
            2000000005,
            1582466146,
            "Всем привет я тест",
            {"from": "253866502", "mentions": [431631325], "marked_users": [[1, [431631325]]],},
            {"reply": '{"conversation_message_id":93222}', "fwd": "0_0"},
            0,
        ],
    )
    assert event.object.text == "Всем привет я тест"
    assert event.object.peer_id == 2000000005
    assert event.object.message_data.mentions[0] == 431631325
    assert json.loads(event.object.extra_message_data["reply"])["conversation_message_id"] == 93222
    assert event.object.message_id == 174167


def test_friend_offline_test():
    event = get_event_object([9, -448252266, 0, 1582464656, 2274003, 0, 0])
    assert event.object.is_timeout == TimeoutUserEnum.LEAVED_FROM_SITE
    assert event.object.timestamp == 1582464656


def test_read_outgoing_messages():
    event = get_event_object([7, 349964901, 173672, 0])
    assert event.object.message_id == 173672
    assert event.object.peer_id == 349964901
    assert event.object.count == 0


def test_change_chat_setting():
    event = get_event_object([52, 11, -191949777, 0])
    assert event.object.type == ChangedChatSettingsType.SHOW_OR_REMOVED_KEYBOARD
    assert event.object.peer_id == -191949777


def test_message_with_keyboard():
    event = get_event_object(
        [
            4,
            188794,
            1,
            -191949777,
            1582730565,
            "123",
            {
                "title": " ... ",
                "keyboard": {
                    "one_time": False,
                    "buttons": [
                        [
                            {
                                "action": {"type": "text", "payload": "", "label": "helloworld",},
                                "color": "default",
                            }
                        ]
                    ],
                },
            },
            {},
            0,
        ],
    )

    assert event.object.message_id == 188794
    assert event.object.event_id == 4
    assert event.object.flags == 1
    assert event.object.text == "123"
    assert not event.object.message_data.keyboard.one_time
    assert event.object.message_data.keyboard.buttons[0][0].action.label == "helloworld"
    assert event.object.message_data.keyboard.buttons[0][0].action.type == "text"


def test_changed_unread_count():
    event = get_event_object([80, 10, 0])

    assert event.object.count == 10
    assert event.object.count_with_notifications == 0
