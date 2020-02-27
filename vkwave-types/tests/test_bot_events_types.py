from vkwave_types.bot_events import get_event_object


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


def test_message_new_event():
    event = get_event_object(
        {
            "type": "message_new",
            "object": {
                "message": {
                    "date": 1582576963,
                    "from_id": 578716413,
                    "id": 305,
                    "out": 0,
                    "peer_id": 578716413,
                    "text": "bruh",
                    "conversation_message_id": 304,
                    "fwd_messages": [
                        {
                            "date": 1582576949,
                            "from_id": 578716413,
                            "text": "meh",
                            "attachments": [
                                {
                                    "type": "photo",
                                    "photo": {
                                        "id": 457239498,
                                        "album_id": -15,
                                        "owner_id": 578716413,
                                        "sizes": [
                                            {
                                                "type": "m",
                                                "url": "https://sun9-35.userapi.com/c854128/v854128095/1e466e/VMLEDep08VE.jpg",
                                                "width": 106,
                                                "height": 130,
                                            },
                                            {
                                                "type": "o",
                                                "url": "https://sun9-23.userapi.com/c854128/v854128095/1e4671/JjKjO1FADdM.jpg",
                                                "width": 130,
                                                "height": 160,
                                            },
                                            {
                                                "type": "p",
                                                "url": "https://sun9-57.userapi.com/c854128/v854128095/1e4672/QfGZzArpY0o.jpg",
                                                "width": 200,
                                                "height": 246,
                                            },
                                            {
                                                "type": "q",
                                                "url": "https://sun9-9.userapi.com/c854128/v854128095/1e4673/AQQRKSJmK4o.jpg",
                                                "width": 320,
                                                "height": 393,
                                            },
                                            {
                                                "type": "r",
                                                "url": "https://sun9-34.userapi.com/c854128/v854128095/1e4674/LX2HRyrU0p0.jpg",
                                                "width": 510,
                                                "height": 627,
                                            },
                                            {
                                                "type": "s",
                                                "url": "https://sun9-55.userapi.com/c854128/v854128095/1e466d/hqLt9EKYNUo.jpg",
                                                "width": 61,
                                                "height": 75,
                                            },
                                            {
                                                "type": "x",
                                                "url": "https://sun9-5.userapi.com/c854128/v854128095/1e466f/m0EQYpPSYDQ.jpg",
                                                "width": 491,
                                                "height": 604,
                                            },
                                            {
                                                "type": "y",
                                                "url": "https://sun9-42.userapi.com/c854128/v854128095/1e4670/fmZMqDUIzzg.jpg",
                                                "width": 650,
                                                "height": 799,
                                            },
                                        ],
                                        "text": "",
                                        "date": 1581199955,
                                        "access_key": "94a5e81e6c436a13ee",
                                    },
                                }
                            ],
                            "conversation_message_id": 303,
                            "peer_id": 578716413,
                            "id": 304,
                        }
                    ],
                    "important": False,
                    "random_id": 0,
                    "attachments": [
                        {
                            "type": "photo",
                            "photo": {
                                "id": 457239018,
                                "album_id": -6,
                                "owner_id": 578716413,
                                "sizes": [
                                    {
                                        "type": "m",
                                        "url": "https://sun9-60.userapi.com/c206620/v206620889/3dc7e/1V1Vr0O4iHQ.jpg",
                                        "width": 130,
                                        "height": 123,
                                    },
                                    {
                                        "type": "o",
                                        "url": "https://sun9-19.userapi.com/c206620/v206620889/3dc80/HqP_QEDFMlQ.jpg",
                                        "width": 130,
                                        "height": 123,
                                    },
                                    {
                                        "type": "p",
                                        "url": "https://sun9-23.userapi.com/c206620/v206620889/3dc81/jQHNAzH9Mdo.jpg",
                                        "width": 200,
                                        "height": 189,
                                    },
                                    {
                                        "type": "q",
                                        "url": "https://sun9-16.userapi.com/c206620/v206620889/3dc82/PHCmaBA4Oh4.jpg",
                                        "width": 320,
                                        "height": 303,
                                    },
                                    {
                                        "type": "r",
                                        "url": "https://sun9-36.userapi.com/c206620/v206620889/3dc83/VngkKLfGEMA.jpg",
                                        "width": 394,
                                        "height": 373,
                                    },
                                    {
                                        "type": "s",
                                        "url": "https://sun9-53.userapi.com/c206620/v206620889/3dc7d/_BQKJGQpCGU.jpg",
                                        "width": 75,
                                        "height": 71,
                                    },
                                    {
                                        "type": "x",
                                        "url": "https://sun9-34.userapi.com/c206620/v206620889/3dc7f/nmakgKHhLi8.jpg",
                                        "width": 394,
                                        "height": 373,
                                    },
                                ],
                                "text": "",
                                "date": 1579116704,
                                "post_id": 1,
                            },
                        }
                    ],
                    "is_hidden": False,
                },
                "client_info": {
                    "button_actions": [
                        "text",
                        "vkpay",
                        "open_app",
                        "location",
                        "open_link",
                    ],
                    "keyboard": True,
                    "inline_keyboard": True,
                    "lang_id": 0,
                },
            },
            "group_id": 191949777,
            "event_id": "2e0cd793ca2c4c41b511dd8d97500523a7fc1b16",
        }
    )
    assert event.object.message.text == "bruh"
    assert event.object.message.peer_id == 578716413
    assert event.object.message.peer_id == event.object.message.from_id
    assert event.object.message.random_id == 0
    assert event.object.client_info.button_actions[0] == "text"
    assert event.object.message.attachments[0].type == "photo"
    assert event.object.message.attachments[0].photo.album_id == -6
    assert event.object.message.attachments[0].photo.sizes[0].type == "m"
    assert event.object.message.attachments[0].photo.sizes[0].width == 130
    assert event.object.message.fwd_messages[0].text == "meh"
    assert event.object.message.fwd_messages[0].date == 1582576949
    assert event.object.message.fwd_messages[0].attachments[0].type == "photo"
    assert (
        event.object.message.fwd_messages[0].attachments[0].photo.sizes[0].height == 130
    )


def test_message_typing_state():
    event = get_event_object(
        {
            "type": "message_typing_state",
            "object": {"state": "typing", "from_id": 578716413, "to_id": -191949777,},
            "group_id": 191949777,
            "event_id": "514f17d95071fa73607a7e3f122b29f03008abc5",
        }
    )

    assert event.object.state == "typing"
    assert event.object.from_id == 578716413
    assert event.object.to_id == -191949777


def test_message_deny():
    event = get_event_object(
        {
            "type": "message_deny",
            "object": {"user_id": 578716413},
            "group_id": 191949777,
            "event_id": "08fd9e8f52a43c6966f7c117d5e402ab39cc4017",
        }
    )
    assert event.object.user_id == 578716413


def test_message_allow():
    event = get_event_object(
        {
            "type": "message_allow",
            "object": {"user_id": 578716413, "key": ""},
            "group_id": 191949777,
            "event_id": "235695438e43d0765f36efd3355a96ae14556bff",
        }
    )
    assert event.object.user_id == 578716413
    assert event.object.key == ""


def test_group_change_settings():
    event = get_event_object(
        {
            "type": "group_change_settings",
            "object": {
                "user_id": 578716413,
                "changes": {
                    "video": {"old_value": 2, "new_value": 1},
                    "audio": {"old_value": 1, "new_value": 0},
                },
            },
            "group_id": 191949777,
            "event_id": "bda43f669fa88d77c7e97941e13c8bf4f8d3c24d",
        }
    )
    assert event.object.user_id == 578716413
    assert event.object.changes["video"].old_value == 2
    assert event.object.changes["audio"].new_value == 0


def test_photo_new():
    event = get_event_object(
        {
            "type": "photo_new",
            "object": {
                "id": 457239017,
                "album_id": 269275165,
                "owner_id": -191949777,
                "user_id": 100,
                "sizes": [
                    {
                        "type": "s",
                        "url": "https://sun9-2.userapi.com/c206528/v206528324/8472a/RQawjPZIYgU.jpg",
                        "width": 75,
                        "height": 39,
                    },
                    {
                        "type": "m",
                        "url": "https://sun9-43.userapi.com/c206528/v206528324/8472b/FbuiUSD6Yl4.jpg",
                        "width": 130,
                        "height": 68,
                    },
                    {
                        "type": "x",
                        "url": "https://sun9-40.userapi.com/c206528/v206528324/8472c/25QwEBUr-pk.jpg",
                        "width": 604,
                        "height": 317,
                    },
                    {
                        "type": "y",
                        "url": "https://sun9-61.userapi.com/c206528/v206528324/8472d/IACnZVerm2w.jpg",
                        "width": 807,
                        "height": 424,
                    },
                    {
                        "type": "z",
                        "url": "https://sun9-7.userapi.com/c206528/v206528324/8472e/oQTbEkF0bJA.jpg",
                        "width": 1200,
                        "height": 630,
                    },
                    {
                        "type": "o",
                        "url": "https://sun9-71.userapi.com/c206528/v206528324/8472f/q6fqWjr4G0k.jpg",
                        "width": 130,
                        "height": 87,
                    },
                    {
                        "type": "p",
                        "url": "https://sun9-35.userapi.com/c206528/v206528324/84730/FTTxgdvUdqs.jpg",
                        "width": 200,
                        "height": 133,
                    },
                    {
                        "type": "q",
                        "url": "https://sun9-19.userapi.com/c206528/v206528324/84731/fo8Raqqe4rs.jpg",
                        "width": 320,
                        "height": 213,
                    },
                    {
                        "type": "r",
                        "url": "https://sun9-44.userapi.com/c206528/v206528324/84732/nZOJUBM8OOw.jpg",
                        "width": 510,
                        "height": 340,
                    },
                ],
                "text": "",
                "date": 1582726155,
            },
            "group_id": 191949777,
            "event_id": "89c4ea0168f6a1367ea33a328fc2ec7336c3cd1d",
        }
    )
    assert event.object.album_id == 269275165
    assert event.object.sizes[-1].type == "r"


def test_photo_comment_new():
    event = get_event_object(
        {
            "type": "photo_comment_new",
            "object": {
                "id": 1,
                "from_id": 578716413,
                "parents_stack": [],
                "date": 1582726164,
                "text": "а",
                "thread": {"count": 0},
                "photo_owner_id": -191949777,
                "photo_id": 457239017,
            },
            "group_id": 191949777,
            "event_id": "08c7a3b598c159427a79421fa51e60423066c5c6",
        }
    )
    assert event.type == "photo_comment_new"
    assert event.object.thread.count == 0
    assert event.object.text == "а"


def test_photo_comment_delete():
    event = get_event_object(
        {
            "type": "photo_comment_delete",
            "object": {
                "owner_id": -191949777,
                "id": 1,
                "deleter_id": 578716413,
                "photo_id": 457239017,
                "user_id": 578716413,
            },
            "group_id": 191949777,
            "event_id": "ed2ab84413adebeec1921c0c85fe7dc276810d9d",
        }
    )

    assert event.event_id == "ed2ab84413adebeec1921c0c85fe7dc276810d9d"
    assert event.object.deleter_id == 578716413
    assert event.object.photo_id == 457239017
