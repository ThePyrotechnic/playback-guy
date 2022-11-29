"""
playback-guy - Play back URLs in Discord
    Copyright (C) 2022  Michael Manis - michaelmanis@tutanota.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import hikari
from songbird import ytdl
from songbird.hikari import Voicebox


_intents = hikari.Intents.ALL

with open("secret.key", "r", encoding="UTF-8") as secret_file:
    _bot = hikari.GatewayBot(intents=_intents, token=secret_file.read())


_track_handle = None
_voice = None


@_bot.listen()
async def _event(event: hikari.GuildMessageCreateEvent) -> None:
    global _track_handle, _voice

    if not event.channel_id == 866165635317628948 or event.is_bot or not event.content:
        return

    if event.content.startswith("!steal"):
        try:
            _, url = event.content.split()
        except ValueError:  # Not enough values to unpack
            return

        requestor_voice_state = _bot.cache.get_voice_state(
            event.guild_id, event.author_id
        )
        bot_voice_state = _bot.cache.get_voice_state(event.guild_id, _bot.get_me().id)

        if requestor_voice_state.channel_id is None:
            await event.message.respond("You must be connected to a voice channel")
            return

        if _track_handle is not None:
            _track_handle.stop()

        is_disconnected = _voice is None or bot_voice_state is None
        is_same_channel = (
            False
            if bot_voice_state is None
            else bot_voice_state.channel_id == requestor_voice_state.channel_id
        )

        if not is_disconnected and not is_same_channel:
            await _bot.voice.disconnect(event.guild_id)
            is_disconnected = True

        if is_disconnected:
            _voice = await Voicebox.connect(
                _bot, event.guild_id, requestor_voice_state.channel_id
            )

        _track_handle = await _voice.play_source(await ytdl(url))

    elif event.content == "!stop":
        if _track_handle is not None:
            _track_handle.stop()


def start():
    _bot.run()
