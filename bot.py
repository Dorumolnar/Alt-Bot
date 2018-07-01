import discord
from discord.ext import commands
import random
import asyncio

bot = commands.Bot(">")

@bot.event
async def on_ready():
    print("The free alt BOT is running af")


class MainCommands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("PING 32ms lol trolololo")

@commands.cooldown(1, 3600, commands.BucketType.user)
@bot.command(pass_context=True)
async def minecraft(ctx):
    msg = ["http://zipansion.com/1v3XS", "http://zipansion.com/1v3YO", "http://zipansion.com/1v3Ze", "http://zipansion.com/1v3ao", "http://zipansion.com/1v3bb",
           "http://zipansion.com/1v3cv", "http://zipansion.com/1v3eY", "http://zipansion.com/1v3fc", "http://zipansion.com/1v3gS", "http://zipansion.com/1v3hO",
           "http://zipansion.com/1v3jh", "http://zipansion.com/1v3kf", "http://zipansion.com/1v3mC", "http://zipansion.com/1v3nV", "http://zipansion.com/1v3q0",
           "http://zipansion.com/15753215/optifine-cape-gg", "http://zipansion.com/15753215/vip-hypixel-gg"]
    await bot.say(random.choice(msg))
    await asyncio.sleep(0.6)
    await bot.say("Thanks for using our bot and enjoy your free alt! One more alt in 1 hour. The bot wont show that but its a bug and idk how to fix it - xDoruYT")

@commands.cooldown(1, 3600, commands.BucketType.user)
@bot.command(pass_context=True)
async def spotify(ctx):
    msg = ["http://zipansion.com/1pvio", "http://zipansion.com/1pvkw", "http://zipansion.com/1pvn6", "http://zipansion.com/1pvok",
           "http://zipansion.com/1pvrU", "http://zipansion.com/1pvuB", "http://zipansion.com/1pvwh", "http://zipansion.com/1pw4R",
           "http://zipansion.com/1pw9n", "http://zipansion.com/1pwC2", "http://zipansion.com/1pwE1", "http://zipansion.com/1pwFZ"]
    await bot.say("Spotify is in work")
    """await asyncio.sleep(0.3)
    await bot.say("Thanks for using our bot and enjoy your free alt! One more alt in 1 hour. The bot wont show that but its a bug and idk how to fix it - xDoruYT")"""

@commands.cooldown(1, 3600, commands.BucketType.user)
@bot.command(pass_context=True, hidden=True)
async def steamkey(ctx):
    msg = "zipansion.com/1q1ww"
    await bot.say(msg)
    await asyncio.sleep(0.3)
    await bot.say("The steam key may not work because OTHERS may claimed the key..")

@bot.command(pass_context=True)
async def invite(ctx):
    await bot.say("Here is the link to invite me in your server: https://discordapp.com/oauth2/authorize?client_id=460840000049774593&scope=bot&permissions=1")

bot.run("NDYwODQwMDAwMDQ5Nzc0NTkz.DhKmOQ.qj3oHtqZjjluCLyBLIenlzLwiyk")
