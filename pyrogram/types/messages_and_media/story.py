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

from datetime import datetime
from typing import BinaryIO, Callable, Dict, List, Optional, Union

import pyrogram
from pyrogram import enums, raw, types, utils
from pyrogram.errors import ChannelInvalid, ChannelPrivate

from ..object import Object
from ..update import Update


class Story(Object, Update):
    """A story.

    Parameters:
        id (``int``):
            Unique story identifier.

        from_user (:obj:`~pyrogram.types.User`, *optional*):
            Sender of the story.

        sender_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Sender of the story, sent on behalf of a chat.

        date (:py:obj:`~datetime.datetime`, *optional*):
            Date the story was sent.

        chat (:obj:`~pyrogram.types.Chat`, *optional*):
            Conversation the story belongs to.

        forward_from (:obj:`~pyrogram.types.User`, *optional*):
            For forwarded stories, sender of the original story.

        forward_sender_name (``str``, *optional*):
            For stories forwarded from users who have hidden their accounts, name of the user.

        forward_from_chat (:obj:`~pyrogram.types.Chat`, *optional*):
            For stories forwarded from channels, information about the original channel.

        forward_from_story_id (``int``, *optional*):
            For stories forwarded from channels, identifier of the original story in the channel.

        expire_date (:py:obj:`~datetime.datetime`, *optional*):
            Date the story will be expired.

        media (:obj:`~pyrogram.enums.MessageMediaType`, *optional*):
            The media type of the Story.
            This field will contain the enumeration type of the media message.
            You can use ``media = getattr(story, story.media.value)`` to access the media message.

        has_protected_content (``bool``, *optional*):
            True, if the story can't be forwarded.

        photo (:obj:`~pyrogram.types.Photo`, *optional*):
            Story is a photo, information about the photo.

        video (:obj:`~pyrogram.types.Video`, *optional*):
            Story is a video, information about the video.

        edited (``bool``, *optional*):
           True, if the Story has been edited.

        pinned (``bool``, *optional*):
           True, if the Story is pinned.

        public (``bool``, *optional*):
           True, if the Story is shared with public.

        close_friends (``bool``, *optional*):
           True, if the Story is shared with close_friends only.

        contacts (``bool``, *optional*):
           True, if the Story is shared with contacts only.

        selected_contacts (``bool``, *optional*):
           True, if the Story is shared with selected contacts only.

        caption (``str``, *optional*):
            Caption for the Story, 0-1024 characters.

        caption_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the caption.

        views (``int``, *optional*):
            Stories views.

        forwards (``int``, *optional*):
            Stories forwards.

        outgoing (``bool``, *optional*):
            Whether the story is incoming or outgoing.
            Story received from others are incoming (*outgoing* is False).
            Story sent from yourself are outgoing (*outgoing* is True).

        privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
            Story privacy.

        allowed_users (List of ``int`` | ``str``, *optional*):
            List of user_ids or chat_ids whos allowed to view the story.

        disallowed_users (List of ``int`` | ``str``, *optional*):
            List of user_ids whos denied to view the story.

        reactions (List of :obj:`~pyrogram.types.Reaction`):
            List of the reactions to this story.

        reactions_count (``int``, *optional*):
            Reactions count.

        skipped (``bool``, *optional*):
            The story is skipped.
            A story can be skipped in case it was skipped.

        deleted (``bool``, *optional*):
            The story is deleted.
            A story can be deleted in case it was deleted or you tried to retrieve a story that doesn't exist yet.

        media_areas (List of :obj:`~pyrogram.types.MediaArea`, *optional*):
            List of media areas.

        raw (:obj:`~pyrogram.raw.types.StoryItem`, *optional*):
            The raw story object, as received from the Telegram API.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: int,
        from_user: Optional["types.User"] = None,
        sender_chat: Optional["types.Chat"] = None,
        date: Optional[datetime] = None,
        chat: Optional["types.Chat"] = None,
        forward_from: Optional["types.User"] = None,
        forward_sender_name: Optional[str] = None,
        forward_from_chat: Optional["types.Chat"] = None,
        forward_from_story_id: Optional[int] = None,
        expire_date: Optional[datetime] = None,
        media: Optional["enums.MessageMediaType"] = None,
        has_protected_content: Optional[bool] = None,
        photo: Optional["types.Photo"] = None,
        video: Optional["types.Video"] = None,
        edited: Optional[bool] = None,
        pinned: Optional[bool] = None,
        public: Optional[bool] = None,
        close_friends: Optional[bool] = None,
        contacts: Optional[bool] = None,
        selected_contacts: Optional[bool] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List["types.MessageEntity"]] = None,
        views: Optional[int] = None,
        forwards: Optional[int] = None,
        outgoing: Optional[bool] = None,
        privacy: Optional["enums.StoriesPrivacyRules"] = None,
        allowed_users: Optional[List[Union[int, str]]] = None,
        disallowed_users: Optional[List[Union[int, str]]] = None,
        reactions: Optional[List["types.Reaction"]] = None,
        reactions_count: Optional[int] = None,
        skipped: Optional[bool] = None,
        deleted: Optional[bool] = None,
        media_areas: Optional[List["types.MediaArea"]] = None,
        raw: Optional["raw.types.StoryItem"] = None
    ):
        super().__init__(client)

        self.id = id
        self.from_user = from_user
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.forward_from = forward_from
        self.forward_sender_name = forward_sender_name
        self.forward_from_chat = forward_from_chat
        self.forward_from_story_id = forward_from_story_id
        self.expire_date = expire_date
        self.media = media
        self.has_protected_content = has_protected_content
        self.photo = photo
        self.video = video
        self.edited = edited
        self.pinned = pinned
        self.public = public
        self.close_friends = close_friends
        self.contacts = contacts
        self.selected_contacts = selected_contacts
        self.caption = caption
        self.caption_entities = caption_entities
        self.views = views
        self.forwards = forwards
        self.outgoing = outgoing
        self.privacy = privacy
        self.allowed_users = allowed_users
        self.disallowed_users = disallowed_users
        self.reactions = reactions
        self.reactions_count = reactions_count
        self.skipped = skipped
        self.deleted = deleted
        self.media_areas = media_areas
        self.raw = raw

    @staticmethod
    async def _parse(
        client: "pyrogram.Client",
        story: "raw.types.StoryItem",
        peer: "raw.base.Peer",
        users: Dict[int, "raw.base.User"],
        chats: Dict[int, "raw.base.Chat"],
    ) -> "Story":
        if isinstance(peer, raw.types.InputPeerSelf):
            if client.me:
                peer_id = client.me.id
                users.update({peer_id: client.me.raw})
            else:
                r = await client.invoke(raw.functions.users.GetUsers(id=[raw.types.InputPeerSelf()]))
                peer_id = r[0].id
                users.update({r[0].id: r[0]})
        elif hasattr(peer, "user_id"):
            peer_id = peer.user_id

            if peer_id not in users:
                r = await client.invoke(raw.functions.users.GetUsers(id=[raw.types.InputPeerSelf(), peer]))
                users.update({i.id: i for i in r})
        elif hasattr(peer, "channel_id"):
            peer_id = peer.channel_id

            if peer_id not in chats:
                r = await client.invoke(raw.functions.channels.GetChannels(id=[peer]))
                chats.update({peer_id: r.chats[0]})
        else:
            raise ValueError(f"Invalid peer type: {type(peer)}")

        from_user = types.User._parse(client, users.get(peer_id, None))
        sender_chat = types.Chat._parse_channel_chat(client, chats[peer_id]) if not from_user else None
        chat = sender_chat if not from_user else types.Chat._parse_user_chat(client, users.get(peer_id, None))

        if isinstance(story, raw.types.StoryItemDeleted):
            return Story(client=client, id=story.id, deleted=True, from_user=from_user, sender_chat=sender_chat, chat=chat)
        if client.fetch_stories and isinstance(story, raw.types.StoryItemSkipped):
            try:
                r = await client.invoke(
                    raw.functions.stories.GetStoriesByID(
                        peer=await client.resolve_peer(chat.id),
                        id=[story.id]
                    )
                )

                users.update({i.id: i for i in r.users})
                chats.update({i.id: i for i in r.chats})

                if r.stories:
                    story = r.stories[0]
            except (ChannelPrivate, ChannelInvalid):
                return Story(client=client, id=story.id, skipped=True, from_user=from_user, sender_chat=sender_chat, chat=chat)
        if isinstance(story, raw.types.MessageMediaStory):
            if client.me and client.me.is_bot:
                return Story(client=client, id=story.id, from_user=from_user, sender_chat=sender_chat, chat=chat)

            if not getattr(story, "story", None):
                if client.fetch_stories:
                    try:
                        r = await client.invoke(
                            raw.functions.stories.GetStoriesByID(
                                peer=await client.resolve_peer(chat.id),
                                id=[story.id]
                            )
                        )

                        users.update({i.id: i for i in r.users})
                        chats.update({i.id: i for i in r.chats})

                        if r.stories:
                            story = r.stories[0]
                    except (ChannelPrivate, ChannelInvalid):
                        pass
            else:
                story = story.story

        if client.fetch_stories and getattr(story, "min", None):
            try:
                r = await client.invoke(
                    raw.functions.stories.GetStoriesByID(
                        peer=await client.resolve_peer(chat.id),
                        id=[story.id]
                    )
                )

                users.update({i.id: i for i in r.users})
                chats.update({i.id: i for i in r.chats})

                if r.stories:
                    story = r.stories[0]
            except (ChannelPrivate, ChannelInvalid):
                pass

        if not getattr(story, "media", None):
            return Story(client=client, id=story.id, deleted=True, from_user=from_user, sender_chat=sender_chat, chat=chat)

        photo = None
        video = None
        privacy = None
        allowed_users = None
        disallowed_users = None
        media_type = None
        views = None
        forwards = None
        reactions = None
        reactions_count = None

        forward_from = None
        forward_sender_name = None
        forward_from_chat = None
        forward_from_story_id = None

        forward_header = story.fwd_from  # type: raw.types.StoryFwdHeader

        if forward_header:
            fwd_raw_peer_id = utils.get_raw_peer_id(forward_header.from_peer)
            fwd_peer_id = utils.get_peer_id(forward_header.from_peer)

            if fwd_peer_id > 0:
                forward_from = types.User._parse(client, users[fwd_raw_peer_id])
            else:
                forward_from_chat = types.Chat._parse_channel_chat(client, chats[fwd_raw_peer_id])
                forward_from_story_id = forward_header.story_id

        if story.views:
            views=getattr(story.views, "views_count", None)
            forwards=getattr(story.views, "forwards_count", None)
            reactions=[
                types.Reaction._parse_count(client, reaction)
                for reaction in getattr(story.views, "reactions", [])
            ] or None
            reactions_count = getattr(story.views, "reactions_count", None)

        if isinstance(story.media, raw.types.MessageMediaPhoto):
            photo = types.Photo._parse(client, story.media.photo, story.media.ttl_seconds)
            media_type = enums.MessageMediaType.PHOTO
        else:
            doc = story.media.document
            attributes = {type(i): i for i in doc.attributes}
            video_attributes = attributes.get(raw.types.DocumentAttributeVideo, None)
            video = types.Video._parse(client, doc, video_attributes, alternative_videos=getattr(story.media, "alt_documents", []))
            media_type = enums.MessageMediaType.VIDEO

        privacy_map = {
            raw.types.PrivacyValueAllowAll: enums.StoriesPrivacyRules.PUBLIC,
            raw.types.PrivacyValueAllowContacts: enums.StoriesPrivacyRules.CONTACTS,
            raw.types.PrivacyValueAllowCloseFriends: enums.StoriesPrivacyRules.CLOSE_FRIENDS,
            raw.types.PrivacyValueDisallowAll: enums.StoriesPrivacyRules.SELECTED_USERS,
        }

        for priv in story.privacy:
            privacy = privacy_map.get(type(priv), None)

            if isinstance(priv, raw.types.PrivacyValueAllowUsers):
                allowed_users = types.List(types.User._parse(client, users.get(user_id, None)) for user_id in priv.users)
            elif isinstance(priv, raw.types.PrivacyValueAllowChatParticipants):
                allowed_users = types.List(types.Chat._parse_chat_chat(client, chats.get(chat_id, None)) for chat_id in priv.chats)
            elif isinstance(priv, raw.types.PrivacyValueDisallowUsers):
                disallowed_users = types.List(types.User._parse(client, users.get(user_id, None)) for user_id in priv.users)
            elif isinstance(priv, raw.types.PrivacyValueDisallowChatParticipants):
                disallowed_users = types.List(types.Chat._parse_chat_chat(client, chats.get(chat_id, None)) for chat_id in priv.chats)

        entities = [e for e in (types.MessageEntity._parse(client, entity, {}) for entity in story.entities) if e]

        return Story(
            id=story.id,
            from_user=from_user,
            sender_chat=sender_chat,
            date=utils.timestamp_to_datetime(story.date),
            chat=chat,
            forward_from=forward_from,
            forward_sender_name=forward_sender_name,
            forward_from_chat=forward_from_chat,
            forward_from_story_id=forward_from_story_id,
            expire_date=utils.timestamp_to_datetime(story.expire_date),
            media=media_type,
            has_protected_content=story.noforwards,
            photo=photo,
            video=video,
            edited=story.edited,
            pinned=story.pinned,
            public=story.public,
            close_friends=story.close_friends,
            contacts=story.contacts,
            selected_contacts=story.selected_contacts,
            caption=story.caption,
            caption_entities=entities or None,
            views=views,
            forwards=forwards,
            outgoing=getattr(story, "out", None),
            privacy=privacy,
            allowed_users=allowed_users,
            disallowed_users=disallowed_users,
            reactions=reactions,
            reactions_count=reactions_count,
            media_areas=types.List(
                [
                    await types.MediaArea._parse(client, area, chats)
                    for area in getattr(story, "media_areas", [])
                ]
            ) or None,
            raw=story,
            client=client
        )

    @property
    def link(self) -> Optional[str]:
        if not self.chat.username:
            return None

        return f"https://t.me/{self.chat.username}/s/{self.id}"

    async def reply_text(
        self,
        text: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        entities: List["types.MessageEntity"] = None,
        link_preview_options: "types.LinkPreviewOptions" = None,
        disable_notification: bool = None,
        schedule_date: datetime = None,
        protect_content: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,

        disable_web_page_preview: bool = None,
    ) -> "types.Message":
        """Bound method *reply_text* of :obj:`~pyrogram.types.Story`.

        An alias exists as *reply*.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_message(
                chat_id=story.chat.id,
                text="hello",
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_text("hello")

        Parameters:
            text (``str``):
                Text of the message to be sent.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in message text, which can be specified instead of *parse_mode*.

            link_preview_options (:obj:`~pyrogram.types.LinkPreviewOptions`, *optional*):
                Options used for link preview generation for the message.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent message from forwarding and saving.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            On success, the sent Message is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_message(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            disable_notification=disable_notification,
            schedule_date=schedule_date,
            protect_content=protect_content,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,

            disable_web_page_preview=disable_web_page_preview,
        )

    reply = reply_text

    async def reply_animation(
        self,
        animation: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        has_spoiler: bool = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        thumb: Union[str, BinaryIO] = None,
        file_name: str = None,
        disable_notification: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_animation* :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_animation(
                chat_id=story.chat.id,
                animation=animation,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_animation(animation)

        Parameters:
            animation (``str``):
                Animation to send.
                Pass a file_id as string to send an animation that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get an animation from the Internet, or
                pass a file path as string to upload a new animation that exists on your local machine.

            caption (``str``, *optional*):
                Animation caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            has_spoiler (``bool``, *optional*):
                Pass True if the animation needs to be covered with a spoiler animation.

            duration (``int``, *optional*):
                Duration of sent animation in seconds.

            width (``int``, *optional*):
                Animation width.

            height (``int``, *optional*):
                Animation height.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the animation file sent.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            file_name (``str``, *optional*):
                File name of the animation sent.
                Defaults to file's path basename.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_animation(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            animation=animation,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            duration=duration,
            width=width,
            height=height,
            thumb=thumb,
            file_name=file_name,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_audio(
        self,
        audio: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        duration: int = 0,
        performer: str = None,
        title: str = None,
        thumb: Union[str, BinaryIO] = None,
        file_name: str = None,
        disable_notification: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_audio* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_audio(
                chat_id=story.chat.id,
                audio=audio,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_audio(audio)

        Parameters:
            audio (``str``):
                Audio file to send.
                Pass a file_id as string to send an audio file that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get an audio file from the Internet, or
                pass a file path as string to upload a new audio file that exists on your local machine.

            caption (``str``, *optional*):
                Audio caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            duration (``int``, *optional*):
                Duration of the audio in seconds.

            performer (``str``, *optional*):
                Performer.

            title (``str``, *optional*):
                Track name.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the music file album cover.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            file_name (``str``, *optional*):
                File name of the audio sent.
                Defaults to file's path basename.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_audio(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            audio=audio,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumb=thumb,
            file_name=file_name,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_cached_media(
        self,
        file_id: str,
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        disable_notification: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None
    ) -> Optional["types.Message"]:
        """Bound method *reply_cached_media* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_cached_media(
                chat_id=story.chat.id,
                file_id=file_id,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_cached_media(file_id)

        Parameters:
            file_id (``str``):
                Media to send.
                Pass a file_id as string to send a media that exists on the Telegram servers.

            caption (``bool``, *optional*):
                Media caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_cached_media(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            file_id=file_id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup
        )

    async def reply_media_group(
        self,
        media: List[Union[
            "types.InputMediaPhoto",
            "types.InputMediaVideo",
            "types.InputMediaAudio",
            "types.InputMediaDocument"
        ]],
        paid_message_star_count: int = None,
        disable_notification: bool = None,
    ) -> List["types.Message"]:
        """Bound method *reply_media_group* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_media_group(
                chat_id=story.chat.id,
                media=list_of_media,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_media_group(list_of_media)

        Parameters:
            media (``list``):
                A list containing either :obj:`~pyrogram.types.InputMediaPhoto` or
                :obj:`~pyrogram.types.InputMediaVideo` objects
                describing photos and videos to be sent, must include 2–10 items.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

        Returns:
            On success, a :obj:`~pyrogram.types.Messages` object is returned containing all the
            single messages sent.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_media_group(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            media=media,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
        )

    async def reply_photo(
        self,
        photo: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        has_spoiler: bool = None,
        ttl_seconds: int = None,
        view_once: bool = None,
        disable_notification: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_photo* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_photo(
                chat_id=story.chat.id,
                photo=photo,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_photo(photo)

        Parameters:
            photo (``str``):
                Photo to send.
                Pass a file_id as string to send a photo that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a photo from the Internet, or
                pass a file path as string to upload a new photo that exists on your local machine.

            caption (``str``, *optional*):
                Photo caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            has_spoiler (``bool``, *optional*):
                Pass True if the photo needs to be covered with a spoiler animation.

            ttl_seconds (``int``, *optional*):
                Self-Destruct Timer.
                If you set a timer, the photo will self-destruct in *ttl_seconds*
                seconds after it was viewed.

            view_once (``bool``, *optional*):
                Self-Destruct Timer.
                If True, the photo will self-destruct after it was viewed.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_photo(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            photo=photo,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            ttl_seconds=ttl_seconds,
            view_once=view_once,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_sticker(
        self,
        sticker: Union[str, BinaryIO],
        disable_notification: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_sticker* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_sticker(
                chat_id=story.chat.id,
                sticker=sticker,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_sticker(sticker)

        Parameters:
            sticker (``str``):
                Sticker to send.
                Pass a file_id as string to send a sticker that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a .webp sticker file from the Internet, or
                pass a file path as string to upload a new sticker that exists on your local machine.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_sticker(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            sticker=sticker,
            disable_notification=disable_notification,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_video(
        self,
        video: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        has_spoiler: bool = None,
        ttl_seconds: int = None,
        duration: int = 0,
        width: int = 0,
        height: int = 0,
        video_start_timestamp: int = None,
        video_cover: Union[str, BinaryIO] = None,
        thumb: Union[str, BinaryIO] = None,
        file_name: str = None,
        supports_streaming: bool = True,
        disable_notification: bool = None,
        no_sound: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_video* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_video(
                chat_id=story.chat.id,
                video=video,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_video(video)

        Parameters:
            video (``str``):
                Video to send.
                Pass a file_id as string to send a video that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a video from the Internet, or
                pass a file path as string to upload a new video that exists on your local machine.

            caption (``str``, *optional*):
                Video caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            has_spoiler (``bool``, *optional*):
                Pass True if the video needs to be covered with a spoiler animation.

            ttl_seconds (``int``, *optional*):
                Self-Destruct Timer.
                If you set a timer, the video will self-destruct in *ttl_seconds*
                seconds after it was viewed.

            duration (``int``, *optional*):
                Duration of sent video in seconds.

            width (``int``, *optional*):
                Video width.

            height (``int``, *optional*):
                Video height.

            video_start_timestamp (``int``, *optional*):
                Video startpoint, in seconds.

            video_cover (``str`` | ``BinaryIO``, *optional*):
                Video cover.
                Pass a file_id as string to attach a photo that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a photo from the Internet,
                pass a file path as string to upload a new photo that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the video sent.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            file_name (``str``, *optional*):
                File name of the video sent.
                Defaults to file's path basename.

            supports_streaming (``bool``, *optional*):
                Pass True, if the uploaded video is suitable for streaming.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            no_sound (``bool``, *optional*):
                Pass True, if the uploaded video is a video message with no sound.
                Doesn't work for external links.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_video(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            video=video,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            ttl_seconds=ttl_seconds,
            duration=duration,
            width=width,
            height=height,
            video_start_timestamp=video_start_timestamp,
            video_cover=video_cover,
            thumb=thumb,
            file_name=file_name,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            no_sound=no_sound,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_video_note(
        self,
        video_note: Union[str, BinaryIO],
        duration: int = 0,
        length: int = 1,
        thumb: Union[str, BinaryIO] = None,
        disable_notification: bool = None,
        view_once: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_video_note* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_video_note(
                chat_id=story.chat.id,
                video_note=video_note,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await story.reply_video_note(video_note)

        Parameters:
            video_note (``str``):
                Video note to send.
                Pass a file_id as string to send a video note that exists on the Telegram servers, or
                pass a file path as string to upload a new video note that exists on your local machine.
                Sending video notes by a URL is currently unsupported.

            duration (``int``, *optional*):
                Duration of sent video in seconds.

            length (``int``, *optional*):
                Video width and height.

            thumb (``str`` | ``BinaryIO``, *optional*):
                Thumbnail of the video sent.
                The thumbnail should be in JPEG format and less than 200 KB in size.
                A thumbnail's width and height should not exceed 320 pixels.
                Thumbnails can't be reused and can be only uploaded as a new file.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            view_once (``bool``, *optional*):
                Self-Destruct Timer.
                If True, the video note will self-destruct after it was viewed.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_video_note(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            video_note=video_note,
            duration=duration,
            length=length,
            thumb=thumb,
            disable_notification=disable_notification,
            view_once=view_once,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def reply_voice(
        self,
        voice: Union[str, BinaryIO],
        caption: str = "",
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        duration: int = 0,
        disable_notification: bool = None,
        view_once: bool = None,
        paid_message_star_count: int = None,
        reply_markup: Union[
            "types.InlineKeyboardMarkup",
            "types.ReplyKeyboardMarkup",
            "types.ReplyKeyboardRemove",
            "types.ForceReply"
        ] = None,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional["types.Message"]:
        """Bound method *reply_voice* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_voice(
                chat_id=story.chat.id,
                voice=voice,
                reply_parameters=types.ReplyParameters(
                    chat_id=chat_id,
                    story_id=story.id
                )
            )

        Example:
            .. code-block:: python

                await message.reply_voice(voice)

        Parameters:
            voice (``str``):
                Audio file to send.
                Pass a file_id as string to send an audio that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get an audio from the Internet, or
                pass a file path as string to upload a new audio that exists on your local machine.

            caption (``str``, *optional*):
                Voice message caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            duration (``int``, *optional*):
                Duration of the voice message in seconds.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            view_once (``bool``, *optional*):
                Self-Destruct Timer.
                If True, the voice note will self-destruct after it was listened.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardMarkup` | :obj:`~pyrogram.types.ReplyKeyboardRemove` | :obj:`~pyrogram.types.ForceReply`, *optional*):
                Additional interface options. An object for an inline keyboard, custom reply keyboard,
                instructions to remove reply keyboard or to force a reply from the user.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the sent :obj:`~pyrogram.types.Message` is returned.
            In case the upload is deliberately stopped with :meth:`~pyrogram.Client.stop_transmission`, None is returned
            instead.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_voice(
            chat_id=self.chat.id,
            reply_parameters=types.ReplyParameters(
                chat_id=self.chat.id,
                story_id=self.id
            ),
            voice=voice,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            view_once=view_once,
            paid_message_star_count=paid_message_star_count,
            reply_markup=reply_markup,
            progress=progress,
            progress_args=progress_args
        )

    async def copy(
        self,
        chat_id: Union[int, str],
        caption: str = None,
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None,
        period: int = None,
        privacy: "enums.StoriesPrivacyRules" = None,
        allowed_users: List[int] = None,
        disallowed_users: List[int] = None,
        protect_content: bool = None
    ) -> "types.Story":
        """Bound method *copy* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.copy_story(
                chat_id=story.chat.id,
                from_chat_id=from_chat_id,
                story_id=story.id
            )

        Example:
            .. code-block:: python

                await story.copy(chat_id)

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal stories you can simply use "me" or "self".

            caption (``string``, *optional*):
                New caption for story, 0-1024 characters after entities parsing.
                If not specified, the original caption is kept.
                Pass "" (empty string) to remove the caption.

            period (``int``, *optional*):
                How long the story will posted, in secs.
                only for premium users.

            privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
                Story privacy.
                Defaults to :obj:`~pyrogram.enums.StoriesPrivacyRules.PUBLIC`

            allowed_users (List of ``int``, *optional*):
                List of user_id or chat_id of chat users who are allowed to view stories.
                Note: chat_id available only with :obj:`~pyrogram.enums.StoriesPrivacyRules.SELECTED_USERS`.
                Works with :obj:`~pyrogram.enums.StoriesPrivacyRules.CLOSE_FRIENDS`
                and :obj:`~pyrogram.enums.StoriesPrivacyRules.SELECTED_USERS` only

            disallowed_users (List of ``int``, *optional*):
                List of user_id whos disallow to view the stories.
                Note: Works with :obj:`~pyrogram.enums.StoriesPrivacyRules.PUBLIC`
                and :obj:`~pyrogram.enums.StoriesPrivacyRules.CONTACTS` only

            protect_content (``bool``, *optional*):
                Protects the contents of the sent story from forwarding and saving.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the new caption, which can be specified instead of *parse_mode*.

        Returns:
            :obj:`~pyrogram.types.Story`: On success, the copied story is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        if caption is None:
            caption = self.caption or ""
            caption_entities = self.caption_entities

        return await self._client.send_story(
            chat_id=chat_id,
            media=await self.download(in_memory=True),
            caption=caption,
            period=period,
            protect_content=protect_content,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            privacy=privacy,
            allowed_users=allowed_users,
            disallowed_users=disallowed_users
        )

    async def delete(self):
        """Bound method *delete* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.delete_stories(
                story_ids=story.id
            )

        Example:
            .. code-block:: python

                await story.delete()

        Returns:
            True on success, False otherwise.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.delete_stories(chat_id=self.chat.id, story_ids=self.id)

    async def edit_media(
        self,
        media: Union[str, BinaryIO] = None,
    ) -> "types.Story":
        """Bound method *edit_media* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_story_media(
                chat_id=story.chat.id,
                story_id=story.id,
                media=media
            )

        Example:
            .. code-block:: python

                await story.edit_media("new_video.mp4")

        Parameters:
            media (``str`` | ``BinaryIO``, *optional*):
                New story media.
                Pass a file_id as string to send a photo that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a photo from the Internet,
                pass a file path as string to upload a new photo that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

        Returns:
            On success, the edited :obj:`~pyrogram.types.Story` is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.edit_story_media(
            chat_id=self.chat.id,
            story_id=self.id,
            media=media
        )

    async def edit_caption(
        self,
        caption: str,
        parse_mode: Optional["enums.ParseMode"] = None,
        caption_entities: List["types.MessageEntity"] = None
    ) -> "types.Story":
        """Bound method *edit_caption* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_story_caption(
                story_id=story.id,
                caption="hello"
            )

        Example:
            .. code-block:: python

                await story.edit_caption("hello")

        Parameters:
            caption (``str``):
                New caption of the story.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

        Returns:
            On success, the edited :obj:`~pyrogram.types.Story` is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.edit_story_caption(
            chat_id=self.chat.id,
            story_id=self.id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities
        )

    async def edit_privacy(
        self,
        privacy: "enums.StoriesPrivacyRules" = enums.StoriesPrivacyRules.PUBLIC,
        allowed_users: List[Union[int, str]] = None,
        disallowed_users: List[Union[int, str]] = None,
    ) -> "types.Story":
        """Bound method *edit_privacy* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.edit_story_privacy(
                story_id=story.id,
                privacy=enums.StoriesPrivacyRules.PUBLIC
            )

        Example:
            .. code-block:: python

                await story.edit_privacy(enums.StoriesPrivacyRules.PUBLIC)

        Parameters:
            privacy (:obj:`~pyrogram.enums.StoriesPrivacyRules`, *optional*):
                Story privacy. Defaults to :obj:`~pyrogram.enums.StoriesPrivacyRules.PUBLIC`.

            allowed_users (List of ``int`` | ``str``, *optional*):
                List of user_id or chat_id of chat users who are allowed to view stories.
                Note: chat_id available only with :obj:`~pyrogram.enums.StoriesPrivacyRules.SELECTED_USERS`.
                Works with :obj:`~pyrogram.enums.StoriesPrivacyRules.CLOSE_FRIENDS`
                and :obj:`~pyrogram.enums.StoriesPrivacyRules.SELECTED_USERS` only

            disallowed_users (List of ``int`` | ``str``, *optional*):
                List of user_id whos disallow to view the stories.
                Note: Works with :obj:`~pyrogram.enums.StoriesPrivacyRules.PUBLIC`
                and :obj:`~pyrogram.enums.StoriesPrivacyRules.CONTACTS` only

        Returns:
            On success, the edited :obj:`~pyrogram.types.Story` is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.edit_story_privacy(
            chat_id=self.chat.id,
            story_id=self.id,
            privacy=privacy,
            allowed_users=allowed_users,
            disallowed_users=disallowed_users,
        )

    async def react(self, emoji: Union[int, str] = None) -> bool:
        """Bound method *react* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.send_reaction(
                chat_id=story.chat.id,
                story_id=story.id,
                emoji="🔥"
            )

        Example:
            .. code-block:: python

                await story.react(emoji="🔥")

        Parameters:
            emoji (``int`` | ``str``, *optional*):
                Reaction emoji.
                Pass None as emoji (default) to retract the reaction.

        Returns:
            ``bool``: On success, True is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.send_reaction(
            chat_id=self.chat.id,
            story_id=self.id,
            emoji=emoji
        )

    async def forward(
        self,
        chat_id: Union[int, str],
        message_thread_id: int = None,
        disable_notification: bool = None,
        schedule_date: datetime = None,
        paid_message_star_count: int = None,
    ) -> Optional["types.Message"]:
        """Bound method *forward* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.forward_story(
                chat_id=chat_id,
                from_chat_id=story.chat.id,
                story_id=story.id
            )

        Example:
            .. code-block:: python

                await story.forward(chat_id)

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_thread_id (``int``, *optional*):
                Unique identifier of a message thread to which the message belongs.
                For supergroups only.

            disable_notification (``bool``, *optional*):
                Sends the message silently.
                Users will receive a notification with no sound.

            schedule_date (:py:obj:`~datetime.datetime`, *optional*):
                Date when the message will be automatically sent.

            paid_message_star_count (``int``, *optional*):
                The number of Telegram Stars the user agreed to pay to send the messages.

        Returns:
            On success, the forwarded Message is returned.

        Raises:
            RPCError: In case of a Telegram RPC error.
        """
        return await self._client.forward_story(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            story_id=self.id,
            message_thread_id=message_thread_id,
            disable_notification=disable_notification,
            schedule_date=schedule_date,
            paid_message_star_count=paid_message_star_count,
        )

    async def download(
        self,
        file_name: str = "",
        in_memory: bool = False,
        block: bool = True,
        progress: Callable = None,
        progress_args: tuple = ()
    ) -> Optional[Union[str, BinaryIO]]:
        """Bound method *download* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.download_media(story)

        Example:
            .. code-block:: python

                await story.download()

        Parameters:
            file_name (``str``, *optional*):
                A custom *file_name* to be used instead of the one provided by Telegram.
                By default, all files are downloaded in the *downloads* folder in your working directory.
                You can also specify a path for downloading files in a custom location: paths that end with "/"
                are considered directories. All non-existent folders will be created automatically.

            in_memory (``bool``, *optional*):
                Pass True to download the media in-memory.
                A binary file-like object with its attribute ".name" set will be returned.
                Defaults to False.

            block (``bool``, *optional*):
                Blocks the code execution until the file has been downloaded.
                Defaults to True.

            progress (``Callable``, *optional*):
                Pass a callback function to view the file transmission progress.
                The function must take *(current, total)* as positional arguments (look at Other Parameters below for a
                detailed description) and will be called back each time a new file chunk has been successfully
                transmitted.

            progress_args (``tuple``, *optional*):
                Extra custom arguments for the progress callback function.
                You can pass anything you need to be available in the progress callback scope; for example, a Message
                object or a Client instance in order to edit the message with the updated progress status.

        Other Parameters:
            current (``int``):
                The amount of bytes transmitted so far.

            total (``int``):
                The total size of the file.

            *args (``tuple``, *optional*):
                Extra custom arguments as defined in the ``progress_args`` parameter.
                You can either keep ``*args`` or add every single extra argument in your function signature.

        Returns:
            On success, the absolute path of the downloaded file as string is returned, None otherwise.

        Raises:
            RPCError: In case of a Telegram RPC error.
            ``ValueError``: If the message doesn't contain any downloadable media
        """
        return await self._client.download_media(
            message=self,
            file_name=file_name,
            in_memory=in_memory,
            block=block,
            progress=progress,
            progress_args=progress_args,
        )

    async def read(self) -> List[int]:
        """Bound method *read* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.read_chat_stories(
                chat_id=chat_id,
                max_id=story_id
            )

        Example:
            .. code-block:: python

                await story.read()

        Returns:
            List of ``int``: On success, a list of read stories is returned.
        """
        return await self._client.read_chat_stories(
            chat_id=self.chat.id,
            max_id=self.id
        )

    async def view(self) -> bool:
        """Bound method *view* of :obj:`~pyrogram.types.Story`.

        Use as a shortcut for:

        .. code-block:: python

            await client.view_stories(
                chat_id=chat_id,
                story_id=story_id
            )

        Example:
            .. code-block:: python

                await story.view()

        Returns:
            True on success, False otherwise.
        """
        return await self._client.view_stories(
            chat_id=self.chat.id,
            story_id=self.id
        )
