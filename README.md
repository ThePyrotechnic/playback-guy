playback-guy - Play URLs in Discord
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

## Setup

The bot expects a `secret.key` file with the bot's secret key to be in the directory that the script is launched from

## Dependencies

- rust/cargo (required to build songbird-py)
- ffmpeg
- opus
- youtube-dl (can be pip installed - not included in package dependencies in case the user wants to use a different version)

See the Dockerfile for build instructions

