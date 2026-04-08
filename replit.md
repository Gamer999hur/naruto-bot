# Discord Naruto RPG Bot

A Discord bot built with Python and discord.py, themed around the Naruto universe. Players can create characters, check their status, and use jutsu in a text-based RPG system.

## Tech Stack

- **Language**: Python 3.12
- **Library**: discord.py 2.x
- **Data Storage**: Local JSON files (jutsu.json, players.json, clas.json)

## Project Structure

- `bot.py` — Main bot entry point with commands and event handlers
- `funcoes.py` — Utility/helper functions
- `jutsu.json` — Jutsu definitions (damage and chakra cost)
- `players.json` — Player data storage
- `clas.json` — Clan/class data storage

## Bot Commands

- `.criar_personagem` — Create a new character
- `.status` — View your character's HP, chakra, and level
- `.jutsu <name>` — Use a jutsu

## Environment Variables / Secrets

- `DISCORD_BOT_TOKEN` — Discord bot token (required, set as a Replit secret)

## Running the Bot

The bot runs via the "Start application" workflow using:
```
python3 bot.py
```
