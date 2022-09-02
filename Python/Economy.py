import discord
from discord.ext import commands
from config import settings
import json
import random

bot = commands.Bot(command_prefix = '*', intents = discord.Intents.all())

@bot.event
async def on_ready(role = discord.Role):
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()

        for guild in bot.guilds:
            for member in guild.members:
                with open ('Economy.json', 'r') as file:
                    data = json.load(file)
                    file.close()

                    with open ('Economy.json', 'w') as file:
                        data[str(member.id)] = {
                            "Cash": 0,
                            "Bank": 0
                        }
                        json.dump(data, file, indent=4)
                        file.close()

@bot.command(aliases = ["работать", "Работать"])
async def work(member: discord.Member, message: discord.Message):
    money = random.randint(50, 500)
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        json.dump(data, file, indent = 4)
        file.close()
    await message.add_reaction ("<:Razban:991591498795724901>")
    await message.channel.send (f"{message.author.mention}, вы получили зарплату в размере {money} <:Ban:990705130720591872>!")
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()
    with open ('Economy.json', 'w') as file:
        data[str(message.author.id)]['Cash'] += money
        json.dump(data, file, indent=4)
        file.close()

@bot.command (name = "Банк", aliases = ["банк"])
async def embed (ctx, arg1, member: discord.Member, message: discord.Message):
    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        file.close()

    deposit = arg1
    embeddeposit = discord.Embed (
        title = f"{deposit} <:Ban:990705130720591872> успешно относены в банк, теперь в банкке {data[str(member.author.id)]['Bank']}"
    )

    if data[str(message.author.id)]['Money'] < deposit:
        await message.channel.send(embed = embed)
        response = await bot.wait_for("button_click")
        if response.channel == ctx.channel:
            if response.respond("Вывести все деньги в банк"):
                await response.respond(embed = embeddeposit)
                with open('Economy.json', 'w') as file:
                    data[str(message.author.id)]['Bank'] += data[str(message.author.id)]['Cash']
                    data[str(message.author.id)]['Money'] = 0
                    json.dump(data, file, indent=4)
                    file.close()
    else:
        await ctx.send (discord.Embed (
            title = f"{deposit} <:Ban:990705130720591872> успешно относены в банк, теперь в банке {data[str(member.author.id)]['Bank']}"
        ))

        with open ('Economy.json', 'r') as file:
            data = json.load(file)
            json.dump(data, file, indent = 4)
            file.close()
        with open ('Economy.json', 'w') as file:
            data[str(message.author.id)]['Bank'] += deposit
            data[str(message.author.id)]['Money'] -= deposit
            json.dump(data, file, indent=4)
            file.close()

@bot.command(aliases = ["Добавить", "добавить"])
async def add(ctx, arg1, arg2, roleID = discord.Role.id):
    price = arg2
    roleID = arg1

    with open('Shop.json', 'r') as file:
        data = json.load(file)
        json.dump(data, file, indent = 4)
        file.close()
    
    with open('Shop.json', 'w') as file:
        data[str(roleID)] = {
            "Price": price
        }
    json.dump(file, data, indent = 4)
    file.close()

@bot.command(aliases = ["Купить", "купить"])
async def buy(ctx, arg1, message: discord.Message):
    member = ctx.message.author

    with open ('Shop.json', 'r') as file:
        bata = json.load(file)
        json.dump(file, bata, indent = 4)
        file.close()

    with open ('Economy.json', 'r') as file:
        data = json.load(file)
        json.dump(file, data, indent = 4)
        file.close()

    if data[str(message.author.id)]['Cash'] < bata[str(message.arg1.role.id)]['Price']:
        ctx.send(f"{message.author.mention}, у вас недостаточно средств")
    elif arg1 != ('Shop.json'):
        await ctx.send(f"{message.author.mention}, такой роли нет в магазине")
    else:
        data[str(message.author.id)]['Cash'] -= bata[str(message.arg1.role.id)]['Price']
        role_1 = member.guild.get_role(arg1)
        await member.add_roles(role_1)
        await message.add_reaction ('<:Povezlo:991599253149458464>')

        await ctx.send(f"{message.author.mention}, поздравляю с покупкой роли {arg1}! 🥳")

bot.run(settings['token'])
