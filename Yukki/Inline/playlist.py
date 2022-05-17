from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]


def playlist_markup(user_name, user_id, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]


def play_genre_playlist(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Metal",
                callback_data=f"play_playlist {user_id}|{type}|Metal",
            ),
            InlineKeyboardButton(
                text="Remix",
                callback_data=f"play_playlist {user_id}|{type}|Remix",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Pop", callback_data=f"play_playlist {user_id}|{type}|Pop"
            ),
            InlineKeyboardButton(
                text="Lofi",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Sad", callback_data=f"play_playlist {user_id}|{type}|Sad"
            ),
            InlineKeyboardButton(
                text="Poppunk",
                callback_data=f"play_playlist {user_id}|{type}|Poppunk",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Hiphop",
                callback_data=f"play_playlist {user_id}|{type}|Hiphop",
            ),
            InlineKeyboardButton(
                text="Lainnya",
                callback_data=f"play_playlist {user_id}|{type}|Lainnya",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Tutup", callback_data="close"),
        ],
    ]


def add_genre_markup(user_id, type, videoid):
    return [
        [
            InlineKeyboardButton(
                text="✚ Poppunk",
                callback_data=f"add_playlist {videoid}|{type}|Poppunk",
            ),
            InlineKeyboardButton(
                text="✚ Sad",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✚ Pop",
                callback_data=f"add_playlist {videoid}|{type}|Pop",
            ),
            InlineKeyboardButton(
                text="✚ Lofi",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✚ Metal",
                callback_data=f"add_playlist {videoid}|{type}|Metal",
            ),
            InlineKeyboardButton(
                text="✚ Remix",
                callback_data=f"add_playlist {videoid}|{type}|Remix",
            ),
        ],
        [
            InlineKeyboardButton(
                text="✚ Hiphop",
                callback_data=f"add_playlist {videoid}|{type}|Hiphop",
            ),
            InlineKeyboardButton(
                text="✚ Lainnya",
                callback_data=f"add_playlist {videoid}|{type}|Lainnya",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close"),
        ],
    ]


def check_genre_markup(type, videoid, user_id):
    return [
        [
            InlineKeyboardButton(
                text="Poppunk", callback_data=f"check_playlist {type}|Poppunk"
            ),
            InlineKeyboardButton(
                text="Sad", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Pop", callback_data=f"check_playlist {type}|Pop"
            ),
            InlineKeyboardButton(
                text="Lofi", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Metal", callback_data=f"check_playlist {type}|Metal"
            ),
            InlineKeyboardButton(
                text="Remix", callback_data=f"check_playlist {type}|Remix"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Hiphop", callback_data=f"check_playlist {type}|Hiphop"
            ),
            InlineKeyboardButton(
                text="Lainnya", callback_data=f"check_playlist {type}|Lainnya"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    return [
        [
            InlineKeyboardButton(
                text="Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]


def paste_queue_markup(url):
    return [
        [
            InlineKeyboardButton(text="▶️", callback_data="resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data="pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data="skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data="stopcb"),
        ],
        [
            InlineKeyboardButton(
                text="Periksa Daftar Putar Antrian", url=f"{url}"
            )
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]


def fetch_playlist(user_name, type, genre, user_id, url):
    return [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="Periksa Daftar Putar Antrian", url=f"{url}"
            )
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]


def delete_playlist_markuup(type, genre):
    return [
        [
            InlineKeyboardButton(
                text="Ya! Hapus",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="Tidak!", callback_data="close"),
        ]
    ]
