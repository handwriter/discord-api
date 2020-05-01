import discord
from discord.ext import commands
import random
import requests
from auth import TOKEN
from time import sleep


bot = commands.Bot(command_prefix='')


@bot.command(name='set_timer')
async def set_timer(ctx, *args):
    num = args
    sleep(int(args[1]) * 3600 + int(args[3]) * 60)
    await ctx.send("Time X has come!")


bot.run(TOKEN)