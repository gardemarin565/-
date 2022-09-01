import discord
import asyncio
import json
from discord.ext import commands
from config import settings
from discord.utils import get
import requests

client = commands.Bot(command_prefix="*", intents = discord.Intents.all())

@client.event
async def on_ready():
    print ("Кефир готов")

@client.command(name="рофл")
async def reg(ctx):
    await ctx.send(f"{ctx.author.mention}, тебе бан <:Ban:990705130720591872>")

@client.command(name = "Лис")
async def reg(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xF3A016, title = 'Лис')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@client.command(name="Кот")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0xb5b8a5, title = 'Кот')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@client.command(name="Птица")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/bird')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0x76756D, title = 'Птица')
    embed.set_image(url = json_data['link'])
    await ctx.send(embed = embed)

@client.command(name="Панда")
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/panda')
    json_data = json.loads(response.text)

    embed = discord.Embed(color = 0x8C9394, title = 'Панда') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)

client.run(settings['token'])
