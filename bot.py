import discord
import json
import random
import asyncio
import os
from ninja import Ninja
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

players = {}

# ----------------- Eventos ----------------

@bot.event
async def on_ready():
    print(f'Bot online como {bot.user}')

# ----------------- Comandos ----------------

@bot.command()
async def start(ctx, name: str):
    user_id = str(ctx.author.id)
    player = Ninja(name)
    ditctionare = player.to_dict(user_id)

    with open("ninja.json", "w") as f:
        json.dump(ditctionare, f, indent=4)

    await ctx.send(f"Personagem criado! Seja Bem-Vindo ao mundo de naruto {player.name}!")
    
# ----------------- Run ----------------

bot.run(TOKEN)