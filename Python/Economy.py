import discord
from discord.ext import commands
from config import settings
import json
import random
import os

client = commands.Bot(command_prefix = '*', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('Экономика готова')
    if not os.path.exists ('Economy.json'):
        with open('Economy.json', 'w') as file:
            file.write ('{}')
            file.close()

        for guild in client.guilds:
            for member in guild.members:
                with open ('Economy.json', 'r') as file:
                    data = json.load(file)
                    file.close()

                with open('Economy.json', 'w') as file:
                    data[str(member.id)] = {
                        "Cash": 0,
                        "Bank": 0
                    }

                    json.dump(data, file, indent = 4)
                    file.close()

@client.command(aliases = ['Баланс', 'баланс'])
async def balance(ctx):
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()

    cash_amount = data[str(ctx.author.id)]["Cash"]
    bank_amount = data[str(ctx.author.id)]["Bank"]
    all = data[str(ctx.author.id)]["Cash"] + data[str(ctx.author.id)]["Bank"]

    EmbedBalance = discord.Embed(
        title = f'Баланс {ctx.author.name}',
        color = 15644428
    )
    EmbedBalance.add_field(name = 'Наличка:', value = f'{cash_amount} <a:Krut:1009827464836554853>', inline = True)
    EmbedBalance.add_field(name = 'На карте:', value = f'{bank_amount} <a:Krut:1009827464836554853>', inline = True)
    EmbedBalance.add_field(name = 'Всего:', value = f'{all} <a:Krut:1009827464836554853>', inline = True)

    await ctx.send(embed = EmbedBalance)

@client.command(aliases = ['Работать', 'работать'])
async def work(ctx):
    amount = random.randint(50, 500)
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()
    with open('Economy.json', 'w') as file:
        data[str(ctx.author.id)]["Cash"] += amount
        json.dump(data, file, indent = 4)

    await ctx.send(f'{ctx.author.mention}, поздравляю, вы получили зарплату в размере {amount} <a:Krut:1009827464836554853>!')

@client.command(aliases = ['карта', 'Карта'])
async def bank(ctx, arg1):
    BankAmount = arg1

    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()
    if BankAmount <= data[str(ctx.author.id)]["Cash"]:
        data[str(ctx.author.id)]["Cash"] -= BankAmount
        data[str(ctx.author.id)]["Bank"] += BankAmount
        await ctx.send(f'{ctx.author.mention}, {BankAmount} <a:Krut:1009827464836554853> успешно переведены на карту!')
    elif BankAmount > data[str(ctx.author.id)]["Cash"]:
        await ctx.send(f'{ctx.author.mention}, извините, но вы указали сумму, которой вам недостаточно для перевода на карту, нажмите на кнопку ниже, если хотите перевести все свои средства на карту')
    else:
        await ctx.send(f'{ctx.author.mention}, пожалуйста, укажите **сумму** для перевода')

client.run(settings['token'])
