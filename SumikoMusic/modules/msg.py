# SumikoMusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from SumikoMusic.config import SOURCE_CODE
from SumikoMusic.config import ASSISTANT_NAME
from SumikoMusic.config import PROJECT_NAME
from SumikoMusic.config import SUPPORT_GROUP
from SumikoMusic.config import UPDATES_CHANNEL
class Messages(): 
      START_MSG = "**𝐇𝐞𝐲 👋 [{}](tg://user?id={})!**\n\n★𝐈'𝐦 𝐕𝐜 𝐁𝐨𝐭❤️🔥.𝐈 𝐂𝐚𝐧 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐈𝐧 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐕𝐨𝐢𝐜𝐞 𝐂𝐡𝐚𝐭.
𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐏𝐥𝐚𝐲 𝐌𝐮𝐬𝐢𝐜 𝐅𝐫𝐞𝐞𝐥𝐲!/help - 𝐓𝐨 𝐆𝐞𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.✅" 
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}

✰ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

✰ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**𝗦𝗲𝘁𝘁𝗶𝗻𝗴 𝗨𝗽**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
""",
f"""
**𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒**

**🎶 𝗦𝗼𝗻𝗴 𝗣𝗹𝗮𝘆𝗶𝗻𝗴 🎵**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**🎶 𝗣𝗹𝗮𝘆𝗯𝗮𝗰𝗸 🎵**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",

f"""
**🎶 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗠𝘂𝘀𝗶𝗰 𝗣𝗹𝗮𝘆 🎵**

🔥 For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

🔥 If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
""",

f"""
**🎶 𝗠𝗼𝗿𝗲 𝗧𝗼𝗼𝗹𝘀 🎵**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
""",
f"""
**🎶 𝗦𝗼𝗻𝗴 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 🎵**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**🔥 𝗦𝗲𝗮𝗿𝗰𝗵 𝗧𝗼𝗼𝗹𝘀 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
""",

f"""
**🔥🎶 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗙𝗼𝗿 𝗦𝘂𝗱𝗼 𝗨𝘀𝗲𝗿𝘀 🎵🔥**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups

"""
      ]
