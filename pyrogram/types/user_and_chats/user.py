#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

import html
from datetime import datetime
from typing import List, Optional, Union

import pyrogram
from pyrogram import enums, utils
from pyrogram import raw
from pyrogram import types
from ..object import Object
from ..update import Update


class Link(str):
    HTML = "<a href={url}>{text}</a>"
    MARKDOWN = "[{text}]({url})"

    def __init__(self, url: str, text: str, style: enums.ParseMode):
        super().__init__()

        self.url = url
        self.text = text
        self.style = style

    @staticmethod
    def format(url: str, text: str, style: enums.ParseMode):
        if style == enums.ParseMode.MARKDOWN:
            fmt = Link.MARKDOWN
        else:
            fmt = Link.HTML

        return fmt.format(url=url, text=html.escape(text))

    # noinspection PyArgumentList
    def __new__(cls, url, text, style):
        return str.__new__(cls, Link.format(url, text, style))

    def __call__(self, other: str = None, *, style: str = None):
        return Link.format(self.url, other or self.text, style or self.style)

    def __str__(self):
        return Link.format(self.url, self.text, self.style)


class User(Object, Update):
    """A Telegram user or bot.

    Parameters:
        id (``int``):
            Unique identifier for this user or bot.

        is_self(``bool``, *optional*):
            True, if this user is you yourself.

        is_contact(``bool``, *optional*):
            True, if this user is in your contacts.

        is_mutual_contact(``bool``, *optional*):
            True, if you both have each other's contact.

        is_deleted(``bool``, *optional*):
            True, if this user is deleted.

        is_bot (``bool``, *optional*):
            True, if this user is a bot.

        is_verified (``bool``, *optional*):
            True, if this user has been verified by Telegram.

        is_restricted (``bool``, *optional*):
            True, if this user has been restricted. Bots only.
            See *restriction_reason* for details.

        is_scam (``bool``, *optional*):
            True, if this user has been flagged for scam.

        is_fake (``bool``, *optional*):
            True, if this user has been flagged for impersonation.

        is_support (``bool``, *optional*):
            True, if this user is part of the Telegram support team.

        is_premium (``bool``, *optional*):
            True, if this user is a premium user.

        is_contact_require_premium (``bool``, *optional*):
            True, if this user requires premium to send messages to him.

        is_close_friend (``bool``, *optional*):
            True, if this user is a close friend.

        is_stories_hidden (``bool``, *optional*):
            True, if this user has hidden stories.

        is_stories_unavailable (``bool``, *optional*):
            True, if this user stories is unavailable.

        is_business_bot (``bool``, *optional*):
            True, if this bot can connect to business account.

        first_name (``str``, *optional*):
            User's or bot's first name.

        last_name (``str``, *optional*):
            User's or bot's last name.

        status (:obj:`~pyrogram.enums.UserStatus`, *optional*):
            User's last seen & online status. ``None``, for bots.

        last_online_date (:py:obj:`~datetime.datetime`, *optional*):
            Last online date of a user. Only available in case status is :obj:`~pyrogram.enums.UserStatus.OFFLINE`.

        next_offline_date (:py:obj:`~datetime.datetime`, *optional*):
            Date when a user will automatically go offline. Only available in case status is :obj:`~pyrogram.enums.UserStatus.ONLINE`.

        username (``str``, *optional*):
            User's or bot's username.

        usernames (List of :obj:`~pyrogram.types.Username`, *optional*):
            The list of user's collectible (and basic) usernames if available.

        language_code (``str``, *optional*):
            IETF language tag of the user's language.

        emoji_status (:obj:`~pyrogram.types.EmojiStatus`, *optional*):
            Emoji status.

        dc_id (``int``, *optional*):
            User's or bot's assigned DC (data center). Available only in case the user has set a public profile photo.
            Note that this information is approximate; it is based on where Telegram stores a user profile pictures and
            does not by any means tell you the user location (i.e. a user might travel far away, but will still connect
            to its assigned DC). More info at `FAQs </faq#what-are-the-ip-addresses-of-telegram-data-centers>`_.

        phone_number (``str``, *optional*):
            User's phone number.

        photo (:obj:`~pyrogram.types.ChatPhoto`, *optional*):
            User's or bot's current profile photo. Suitable for downloads only.

        restrictions (List of :obj:`~pyrogram.types.Restriction`, *optional*):
            The list of reasons why this bot might be unavailable to some users.
            This field is available only in case *is_restricted* is True.

        reply_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
            Chat reply color.

        profile_color (:obj:`~pyrogram.types.ChatColor`, *optional*):
            Chat profile color.

        added_to_attachment_menu (``bool``, *optional*):
            True, if this user added the bot to the attachment menu.

        active_users_count (``int``, *optional*):
            The number of recently (monthly) active users of the bot.

        inline_need_location (``bool``, *optional*):
            True, if the bot supports inline `user location <https://core.telegram.org/bots/inline#location-based-results>`_ requests. Returned only in get_me.

        inline_query_placeholder (``str``, *optional*):
            Placeholder for inline queries (displayed on the application input field).

        can_be_edited (``bool``, *optional*):
            True, if the current user can edit this bot's profile picture.

        can_be_added_to_attachment_menu (``bool``, *optional*):
            True, if the bot can be added to attachment or side menu.

        can_join_groups (``bool``, *optional*):
            True, if the bot can be invited to groups. Returned only in get_me.

        can_read_all_group_messages (``bool``, *optional*):
            True, if privacy mode is disabled for the bot. Returned only in get_me.

        has_main_web_app (``bool``, *optional*):
            True, if the bot has a main Web App. Returned only in get_me.

        paid_message_star_count (``int``, *optional*):
            Number of Telegram Stars that must be paid by user for each sent message to the user.

        raw (:obj:`~pyrogram.raw.base.User` | :obj:`~pyrogram.raw.base.UserStatus`, *optional*):
            The raw user or user status object, as received from the Telegram API.

        mention (``str``, *property*):
            Generate a text mention for this user.
            You can use ``user.mention()`` to mention the user using their first name (styled using html), or
            ``user.mention("another name")`` for a custom name. To choose a different style
            ("html" or "md"/"markdown") use ``user.mention(style="md")``.

        full_name (``str``, *property*):
            Full name of the other party in a private chat, for private chats and bots.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        is_self: bool = None,
        is_contact: bool = None,
        is_mutual_contact: bool = None,
        is_deleted: bool = None,
        is_bot: bool = None,
        is_verified: bool = None,
        is_restricted: bool = None,
        is_scam: bool = None,
        is_fake: bool = None,
        is_support: bool = None,
        is_premium: bool = None,
        is_contact_require_premium: bool = None,
        is_close_friend: bool = None,
        is_stories_hidden: bool = None,
        is_stories_unavailable: bool = None,
        is_business_bot: bool = None,
        first_name: str = None,
        last_name: str = None,
        status: "enums.UserStatus" = None,
        last_online_date: datetime = None,
        next_offline_date: datetime = None,
        username: str = None,
        usernames: List["types.Username"] = None,
        language_code: str = None,
        emoji_status: Optional["types.EmojiStatus"] = None,
        dc_id: int = None,
        phone_number: str = None,
        photo: "types.ChatPhoto" = None,
        restrictions: List["types.Restriction"] = None,
        reply_color: "types.ChatColor" = None,
        profile_color: "types.ChatColor" = None,
        added_to_attachment_menu: bool = None,
        active_users_count: int = None,
        inline_need_location: bool = None,
        inline_query_placeholder: str = None,
        can_be_edited: bool = None,
        can_be_added_to_attachment_menu: bool = None,
        can_join_groups: bool = None,
        can_read_all_group_messages: bool = None,
        has_main_web_app: bool = None,
        paid_message_star_count: int = None,
        raw: Union["raw.base.User", "raw.base.UserStatus"] = None
    ):
        super().__init__(client)

        self.id = id
        self.is_self = is_self
        self.is_contact = is_contact
        self.is_mutual_contact = is_mutual_contact
        self.is_deleted = is_deleted
        self.is_bot = is_bot
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_support = is_support
        self.is_premium = is_premium
        self.is_contact_require_premium = is_contact_require_premium
        self.is_close_friend = is_close_friend
        self.is_stories_hidden = is_stories_hidden
        self.is_stories_unavailable = is_stories_unavailable
        self.is_business_bot = is_business_bot
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.last_online_date = last_online_date
        self.next_offline_date = next_offline_date
        self.username = username
        self.usernames = usernames
        self.language_code = language_code
        self.emoji_status = emoji_status
        self.dc_id = dc_id
        self.phone_number = phone_number
        self.photo = photo
        self.restrictions = restrictions
        self.reply_color = reply_color
        self.profile_color = profile_color
        self.added_to_attachment_menu = added_to_attachment_menu
        self.active_users_count = active_users_count
        self.inline_need_location = inline_need_location
        self.inline_query_placeholder = inline_query_placeholder
        self.can_be_edited = can_be_edited
        self.can_be_added_to_attachment_menu = can_be_added_to_attachment_menu
        self.can_join_groups = can_join_groups
        self.can_read_all_group_messages = can_read_all_group_messages
        self.has_main_web_app = has_main_web_app
        self.paid_message_star_count = paid_message_star_count
        self.raw = raw

    @property
    def full_name(self) -> str:
        return " ".join(filter(None, [self.first_name, self.last_name])) or None

    @property
    def mention(self):
        return Link(
            f"tg://user?id={self.id}",
            self.first_name or "Deleted Account",
            self._client.parse_mode
        )

    @staticmethod
    def _parse(client, user: "raw.base.User") -> Optional["User"]:
        if user is None or isinstance(user, raw.types.UserEmpty):
            return None

        return User(
            id=user.id,
            is_self=user.is_self,
            is_contact=user.contact,
            is_mutual_contact=user.mutual_contact,
            is_deleted=user.deleted,
            is_bot=user.bot,
            is_verified=user.verified,
            is_restricted=user.restricted,
            is_scam=user.scam,
            is_fake=user.fake,
            is_support=user.support,
            is_premium=user.premium,
            is_contact_require_premium=user.contact_require_premium,
            is_close_friend=user.close_friend,
            is_stories_hidden=user.stories_hidden,
            is_stories_unavailable=user.stories_unavailable,
            is_business_bot=user.bot_business,
            first_name=user.first_name,
            last_name=user.last_name,
            **User._parse_status(user.status, user.bot),
            username=user.username or (user.usernames[0].username if user.usernames else None),
            usernames=types.List([types.Username._parse(r) for r in user.usernames]) or None,
            language_code=user.lang_code,
            emoji_status=types.EmojiStatus._parse(client, user.emoji_status),
            dc_id=getattr(user.photo, "dc_id", None),
            phone_number=user.phone,
            photo=types.ChatPhoto._parse(client, user.photo, user.id, user.access_hash),
            restrictions=types.List([types.Restriction._parse(r) for r in user.restriction_reason]) or None,
            reply_color=types.ChatColor._parse(getattr(user, "color", None)),
            profile_color=types.ChatColor._parse_profile_color(getattr(user, "profile_color", None)),
            added_to_attachment_menu=getattr(user, "attach_menu_enabled", None),
            active_users_count=getattr(user, "bot_active_users", None),
            inline_need_location=getattr(user, "bot_inline_geo", None),
            inline_query_placeholder=getattr(user, "bot_inline_placeholder", None),
            can_be_edited=getattr(user, "bot_can_edit", None),
            can_be_added_to_attachment_menu=getattr(user, "bot_attach_menu", None),
            can_join_groups=getattr(user, "bot_nochats", None),
            can_read_all_group_messages=getattr(user, "bot_chat_history", None),
            has_main_web_app=getattr(user, "bot_has_main_app", None),
            paid_message_star_count=getattr(user, "send_paid_messages_stars", None),
            raw=user,
            client=client
        )

    @staticmethod
    def _parse_status(user_status: "raw.base.UserStatus", is_bot: bool = False):
        if isinstance(user_status, raw.types.UserStatusOnline):
            status, date = enums.UserStatus.ONLINE, user_status.expires
        elif isinstance(user_status, raw.types.UserStatusOffline):
            status, date = enums.UserStatus.OFFLINE, user_status.was_online
        elif isinstance(user_status, raw.types.UserStatusRecently):
            status, date = enums.UserStatus.RECENTLY, None
        elif isinstance(user_status, raw.types.UserStatusLastWeek):
            status, date = enums.UserStatus.LAST_WEEK, None
        elif isinstance(user_status, raw.types.UserStatusLastMonth):
            status, date = enums.UserStatus.LAST_MONTH, None
        else:
            status, date = enums.UserStatus.LONG_AGO, None

        last_online_date = None
        next_offline_date = None

        if is_bot:
            status = None

        if status == enums.UserStatus.ONLINE:
            next_offline_date = utils.timestamp_to_datetime(date)

        if status == enums.UserStatus.OFFLINE:
            last_online_date = utils.timestamp_to_datetime(date)

        return {
            "status": status,
            "last_online_date": last_online_date,
            "next_offline_date": next_offline_date
        }

    @staticmethod
    def _parse_user_status(client, user_status: "raw.types.UpdateUserStatus"):
        return User(
            id=user_status.user_id,
            **User._parse_status(user_status.status),
            raw=user_status,
            client=client
        )

    async def archive(self):
        """Bound method *archive* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.archive_chats(123456789)

        Example:
            .. code-block:: python

               await user.archive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.archive_chats(self.id)

    async def unarchive(self):
        """Bound method *unarchive* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unarchive_chats(123456789)

        Example:
            .. code-block:: python

                await user.unarchive()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unarchive_chats(self.id)

    async def block(self):
        """Bound method *block* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.block_user(123456789)

        Example:
            .. code-block:: python

                await user.block()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.block_user(self.id)

    async def unblock(self):
        """Bound method *unblock* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.unblock_user(123456789)

        Example:
            .. code-block:: python

                await user.unblock()

        Returns:
            True on success.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.unblock_user(self.id)

    async def get_common_chats(self):
        """Bound method *get_common_chats* of :obj:`~pyrogram.types.User`.

        Use as a shortcut for:

        .. code-block:: python

            await client.get_common_chats(123456789)

        Example:
            .. code-block:: python

                await user.get_common_chats()

        Returns:
            List of :obj:`~pyrogram.types.Chat`: On success, a list of the common chats is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """

        return await self._client.get_common_chats(self.id)
