#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present <https://github.com/TelegramPlayGround>
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
from pyrogram import raw

from .upgraded_gift_attribute_id import UpgradedGiftAttributeId


class UpgradedGiftAttributeIdModel(UpgradedGiftAttributeId):
    """Identifier of a gift model.

    Parameters:
        sticker_id (``int``):
            Identifier of the sticker representing the model.
    """
    def __init__(
        self,
        sticker_id: int,
    ):
        super().__init__()

        self.sticker_id = sticker_id

    def write(self) -> "raw.types.StarGiftAttributeIdModel":
        return raw.types.StarGiftAttributeIdModel(
            document_id=self.sticker_id
        )
