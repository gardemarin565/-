import discord
from discord.ext import commands
from discord.utils import get
from config import settings

client = commands.Bot(command_prefix = '*', intents=discord.Intents.all())

@client.event
async def on_ready():
    print ('Аудит готов')

@client.event
async def on_message_delete(message):
    EmbedDelete = discord.Embed(
        title = 'Удалено сообщение',
        description= f'{message.author.mention} удалил(а) сообщение',
        timestamp=message.created_at,
        color = 11909285
    )
    EmbedDelete.add_field(name = 'Содержимое сообщения:', value = f'{message.content}', inline = True)

    await get(message.guild.text_channels, id = 1015961905849970770).send(embed = EmbedDelete)

@client.event
async def on_message_update(message):
    EmbedEdit = discord.Embed(
        title = 'Отредактировано сообщение!',
        description = f'{message.author.mention} отредактировал(а) сообщение!',
        timestamp = message.created_at,
        color = 11909285
    )
    EmbedEdit.add_field(name = 'Содержимое сообщения:', value = f'{message.content}', inline = True)
    EmbedEdit.add_field(name = 'Автор сообщения:', value = f'{message.author.mention}', inline = True)
    await get(message.guild.text_channels, id = 1015961905849970770).send(embed = EmbedEdit)

client.run(settings['token'])