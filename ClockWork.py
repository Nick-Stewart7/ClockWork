import discord
from discord.ext import commands
import datetime
import calendar
from datetime import *
client = discord.Client()
bot_prefix = "/"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: (%s)" % client.user.name)

@client.command(pass_context = True)
async def countdown():
    nowTime = datetime.now()
    weekday = calendar.weekday(2018, 6, 3)
    year = datetime.year
    month = datetime.month
    print(weekday)
    if weekday <= 3:
            dropTime = datetime(2018, 5, 31, 11, 0, 0)
            deltaTime = dropTime - nowTime
    else:
            dropTime = datetime(2018, 6, 7, 11, 0, 0)
            deltaTime = dropTime - nowTime
    embed = discord.Embed()
    embed.add_field(name="time until drop", value=deltaTime, inline=False)
    await client.say(embed=embed)

client.run("NDUyNjczMTA2MjM5MDI5MjQ5.DfTw5g.bc8OsyvTiVMdpPOVd5AGLQFWZkg")