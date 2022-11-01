import json

from vkwave.types.user_events import (
    ChangedChatSettingsType,
    MessageFlag,
    PlatformEnum,
    TimeoutUserEnum,
    get_event_object,
)


def test_deleted_message_event():
    event = get_event_object(
        [
            2,
            666,
            131200,
            2000000005,
        ]
    )
    assert event.object.message_id == 666
    assert event.object.peer_id == 2000000005
    assert event.object.flags == [MessageFlag.DELETED, MessageFlag.DELETED_ALL, 131200]


def test_message_new_event():
    event = get_event_object(
        [
            4,
            174167,
            2629633,
            2000000005,
            1582466146,
            "Всем привет я тест",
            {
                "from": "253866502",
                "mentions": [431631325],
                "marked_users": [[1, [431631325]]],
            },
            {"reply": '{"conversation_message_id":93222}', "fwd": "0_0"},
            0,
        ],
    )
    assert event.object.text == "Всем привет я тест"
    assert event.object.peer_id == 2000000005
    assert event.object.message_data.mentions[0] == 431631325
    assert json.loads(event.object.extra_message_data["reply"])["conversation_message_id"] == 93222
    assert event.object.message_id == 174167


def test_friend_online():
    event = get_event_object([8, 132583811, 4, 1637776094, 2274003, 0, 0])
    assert event.object.user_id == 132583811
    assert event.object.platform == PlatformEnum.ANDROID
    assert event.object.timestamp == 1637776094
    assert event.object.app_id == 2274003
    assert event.object.is_mobile == 0


def test_read_outgoing_messages():
    event = get_event_object([7, 349964901, 173672, 0])
    assert event.object.message_id == 173672
    assert event.object.peer_id == 349964901
    assert event.object.count == 0


def test_friend_offline():
    event = get_event_object([9, -448252266, 0, 1582464656, 2274003, 0, 0])
    assert event.object.is_timeout == TimeoutUserEnum.LEAVED_FROM_SITE
    assert event.object.timestamp == 1582464656


def test_chat_flags_reset():
    event = get_event_object([10, 2000000222, 131200])
    assert event.object.peer_id == 2000000222
    assert event.object.flags == [MessageFlag.DELETED, MessageFlag.DELETED_ALL, 131200]


def test_change_chat_setting():
    event = get_event_object([52, 3, 2000000222, 132583811])
    assert event.object.type == ChangedChatSettingsType.NEW_ADMINISTRATOR
    assert event.object.peer_id == 2000000222
    assert event.object.extra == 132583811


def test_message_with_keyboard():
    event = get_event_object(
        [
            4,
            188794,
            490832562,
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
                                "action": {
                                    "type": "text",
                                    "payload": "",
                                    "label": "helloworld",
                                },
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
    assert event.object.flags == [
        MessageFlag.OUTBOX,
        MessageFlag.FROM_CHAT,
        MessageFlag.FROM_FRIEND,
        MessageFlag.DELETED,
        MessageFlag.ATTACHMENT,
        MessageFlag.CANCEL_SPAM,
        MessageFlag.HIDDEN,
        490832562,  # sum
    ]

    assert event.object.text == "123"
    assert not event.object.message_data.keyboard.one_time
    assert event.object.message_data.keyboard.buttons[0][0].action.label == "helloworld"
    assert event.object.message_data.keyboard.buttons[0][0].action.type.value == "text"


def test_changed_unread_count():
    event = get_event_object([80, 10, 0, 0, 0, 0, 0])

    assert event.object.unread_count == 10
    assert event.object.unread_unmuted_count == 0
    assert event.object.show_only_muted is False
    assert event.object.business_notify_unread_count == 0
    assert event.object.header_unread_count == 0
    assert event.object.header_unread_unmuted_count == 0


def test_reset_flag_event():
    event = get_event_object([3, 3281383, 8, 2000000148])
    assert event.object.message_id == 3281383
    assert event.object.flags == [MessageFlag.IMPORTANT, 8]
    assert event.object.peer_id == 2000000148


def test_edit_message_event():
    event = get_event_object(
        [
            5,
            3281388,
            8211,
            2000000222,
            1637748433,
            "test edit",
            {"from": "132583811"},
            {},
            1401012148,
            4629,
            1637748440,
        ]
    )
    assert event.object.message_id == 3281388
    assert event.object.flags == [
        MessageFlag.UNREAD,
        MessageFlag.OUTBOX,
        MessageFlag.FROM_CHAT,
        MessageFlag.FROM_CHAT2,
        8211,
    ]
    assert event.object.peer_id == 2000000222
    assert event.object.text == "test edit"
    assert event.object.message_data.from_id == "132583811"
