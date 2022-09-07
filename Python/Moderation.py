import discord
from discord.ext import commands
from discord.utils import get
import os
import json
from config import settings

bot = commands.Bot(command_prefix = '*', intents = discord.Intents.all())

Links = [Тут ссылки]
BadWords = [Тут маты]

@bot.event
async def on_ready():
    print ('Кефир готов!')

    if not os.path.exists ('moderation.json'):
        with open('moderation.json', 'w') as file:
            file.write ('{}')
            file.close()

        for guild in bot.guilds:
            for member in guild.members:
                with open ('moderation.json', 'r') as file:
                    data = json.load(file)
                    file.close()

                with open('moderation.json', 'w') as file:
                    data[str(member.id)] = {
                        "Warns": 0,
                        "Caps": 0,
                        "Money": 0
                    }

                    json.dump(data, file, indent = 4)
                    file.close()

@bot.event
async def on_message(message):
    Warn = Links + BadWords
    
    for i in range(0, len(Warn)):
        if Warn[i] in message.content.lower():
            await message.delete()
            with open('moderation.json', 'r') as file:
                data = json.load(file)
                file.close()

            with open ('moderation.json', 'w') as file:
                data[str(message.author.id)]['Warns'] += 1
                json.dump(data, file, indent=4)
                file.close()

            if data[str(message.author.id)]['Warns'] >= 10:
                await message.author.ban(reason="Пользователь превысил количество предупреждений")

    if message.content.isupper():
        with open('moderation.json', 'r') as file:
                data = json.load(file)
                file.close()

        with open('moderation.json', 'w') as file:
            data[str(message.author.id)]["Caps"] += 1
            json.dump(data, file, indent=4)

        if data[str(message.author.id)]["Caps"] >= 2:
            with open('moderation.json', 'w') as file:
                data[str(message.author.id)]["Caps"] = 0
                data[str(message.author.id)]["Warns"] += 1

                json.dump(data, file, indent=4)
                file.close()

                if data[str(message.author.id)]["Warns"] >= 10:
                    await message.author.ban(reason="Пользователь превысил количество предупреждений")

@bot.event
async def on_message(message: discord.Message):
    await bot.process_commands(message)
    if message.author.bot:
        return

@bot.command(name="бан", brief="Банит участника", usage="ban <@user> <reason>")
@commands.has_permissions(administrator = True)
async def ban_(ctx: commands.context.Context, member: discord.Member, *, reason):
    await ctx.guild.ban(user=member, reason=reason)
    message: discord.Message = await ctx.send(f"Пользователь {member} был забанен по причине: {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

@bot.command(name = "разбан", brief = "Разбанивает участника", usage = "unban <@user>")
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Участник {user.mention} разбанен')
        else:
            return

@bot.command(name = "мьют", brief = "Мьютит участника.", usage = "mute <@user> <reason>")
@commands.has_permissions(administrator = True)
async def mute_(ctx: commands.context.Context, member: discord.Member, *, reason):
    role = discord.utils.get(ctx.guild.roles, id = 991023285393313853)
    await member.add_roles(role)
    message: discord.Message = await ctx.send(f"Пользователь {member} был замьючен по причине: {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

@bot.command(name="кик", brief="Кикает участника", usage="kick <@user> <reason>")
@commands.has_permissions(administrator = True)
async def ban_(ctx: commands.context.Context, member: discord.Member, *, reason):
    await ctx.guild.ban(user=member, reason=reason)
    message: discord.Message = await ctx.send(f"Пользователь {member} был кикнут по причине: {reason}.")
    await message.add_reaction("<:662943163090075659:990705130720591872>")

@bot.listen('on_message')
async def whatever_you_want_to_call_it(message):
    msg_content = message.content.lower()
    if any(word in msg_content for word in BadWords):
        await message.delete()
        await message.channel.send(f"{message.author.mention} На этом сервере запрещены маты, не матерись пожалуйста")
    else:
        return

@bot.command(name = "Чистка", brief = "Чистит данный текстовый канал от указонного числа сообщений", usage = "Чистка <кол-во удаленных сообщений>")
@commands.has_permissions(administrator = True)
async def clear_command(ctx: commands.context.Context, amount: int = 5):
    await ctx.message.delete()
    amount_purged = await ctx.channel.purge(limit=amount)
    await ctx.send(f"Было удалено {len(amount_purged)} сообщений!", delete_after = 5)

bot.run(settings['token'])
