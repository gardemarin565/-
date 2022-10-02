import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import get
from discord.ui import 

from Config import settings

client = commands.Bot(command_prefix = '*', intents = discord.Intents.all())

@client.command(name = 'Тикет')
async def ticket(message):
    EmbedTicket1 = discord.Embed(
        title = 'Тикет',
        description = 'Нажми на кнопку ниже, чтобы связаться с техподдержкой сервера',
        color = 11909285
    )
    button = Button(label = 'Помощь', style = discord.ButtonStyle.gray, emoji = '<:Razban:991591498795724901>')
    view = View()
    button.callback = button_callback
    async def button_callback(interaction):
        channel = await client.create_guild('запрос-1', type = guild_text, nsfw = False)
    view.add_item(button)

client.run(settings['token'])