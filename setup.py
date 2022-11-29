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
import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

git_repo = "https://github.com/thepyrotechnic/playback-guy"

setuptools.setup(
    name="playback-guy",
    version=os.environ["VERSION"],
    author="Michael Manis",
    author_email="michaelmanis@tutanota.com",
    description="Play URLs in discord",
    license_files="LICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=git_repo,
    project_urls={
        "Bug Tracker": f"{git_repo}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "click",
        "hikari",
        "songbird-py"
    ],
    extras_require={
        "dev": ["black"]
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
    entry_points='''
        [console_scripts]
        playback-guy=playback_guy.cli:playback_guy
    ''',
)
