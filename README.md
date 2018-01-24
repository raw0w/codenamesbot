# Codenames Discord Bot [wip]

Discord bot that simulates Codenames boardgame. 

## What is Spyfall?

**CODENAMES** is a game of guessing which code names (words) in a set are related to a hint-word given by another player.

There are [rules on English](http://czechgames.com/files/rules/codenames-rules-en.pdf) and [rules on Russian](https://tesera.ru/images/items/657300/codenames_rules_ru_1_5.pdf)

----------
## Setup
- Place your bot's token in the end of Codenames_bot.py:
```sh
bot.run("place_your_token_here")
```
- [Add bot](https://discordapp.com/developers/applications/me) on your Discord server;

- Turn it on
```sh
python Codenames_bot.py
```


## Requirements

- Python 3.4.2+
- [discord.py](https://github.com/Rapptz/discord.py) library
- [Pillow](https://github.com/python-pillow/Pillow) library
- `asyncio` library
- `random` library 

Usually `pip` will handle these for you.

## List of commands

!codenames start

!codenames rules

!codenames suggest

## List to-do

- add rules
- make possible variants '0' and 'inf' and logic for them
- optimize code
- localize in English


