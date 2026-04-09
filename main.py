import discord
import json
import random
import asyncio
import os
from utils import database
from models.ninja import Ninja
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

async def verifyNinja(ctx):
    user_id = str(ctx.author.id)
    dados = database.LoadDadosFrom("data/ninja.json")
    if not user_id in dados:
        await ctx.send("Você não tem um personagem ainda! Use .start (nome do ninja) para começar sua jornada!")
        return None
    return dados[user_id]


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
    dados = database.LoadDadosFrom("data/ninja.json")
    if user_id in dados:
        await ctx.send("Você já tem um personagem!")
        return

    player = Ninja(name)
    ditctionare = player.to_dict()
    dados[user_id] = ditctionare

    database.WriteDadosIn("data/ninja.json", dados)
    await ctx.send(f"Personagem criado com sucesso! Bem-vindo {player.name}")


@bot.command()
async def perfil(ctx):
    user_id = str(ctx.author.id)
    player = await verifyNinja(ctx)
    if not player:
        return
    elif player:
        embed = discord.Embed(
            title="Perfil do Ninja",
            description="Informações do seu personagem",
            color=discord.Color.orange()
        )

        embed.add_field(name="Nome", value=player['name'], inline=True)
        embed.add_field(name="Hp", value=player['hp'], inline=True)
        embed.add_field(name="Clã", value=player['cla'], inline=True)
        embed.add_field(name="Chakra", value=player['chakra'], inline=True)

        embed.set_footer(text="Use !jutsus para ver seus jutsus.")

        await ctx.send(embed=embed)


# ----------------- Run ----------------

bot.run(TOKEN)