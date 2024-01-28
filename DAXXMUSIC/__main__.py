import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from DAXXMUSIC import LOGGER, app, userbot
from DAXXMUSIC.core.call import DAXX
from DAXXMUSIC.misc import sudo
from DAXXMUSIC.plugins import ALL_MODULES
from DAXXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("sᴛʀɪɴɢ sᴇssɪᴏɴ ɴᴏᴛ ғɪʟʟᴇᴅ, 𝐏ʟᴇsᴇ ғɪʟʟ ᴀ Pʏʀᴏɢʀᴀᴍ sᴇssɪᴏɴ")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DAXXMUSIC.plugins" + all_module)
    LOGGER("DAXXMUSIC.plugins").info("ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ʟᴏᴀᴅᴇᴅ ʙᴀʙʏ🥳...")
    await userbot.start()
    await DAXX.start()
    try:
        await DAXX.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("DAXXMUSIC").error(
            "𝗣ʟᴢ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛ\ᴄʜᴀɴɴᴇʟ\n\nʀᴅx ʙᴏᴛ sᴛᴏᴘ........"
        )
        exit()
    except:
        pass
    await DAXX.decorators()
    LOGGER("DAXXMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎ᴍᴀᴅᴇ ʙʏ ʀᴅx ʀᴀᴊ☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("DAXXMUSIC").info("sᴛᴏᴘ ʀᴅx ᴍᴜsɪᴄ🎻 ʙᴏᴛ..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
