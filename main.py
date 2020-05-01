import discord
from discord.ext import commands
import random
import requests
from auth import TOKEN
from time import sleep
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
bot = commands.Bot(command_prefix='#!')

@bot.command(name='numerals')
async def numerals(ctx, word, number):
    word_p = morph.parse(word)[0]
    await ctx.send(f"{number} {word_p.make_agree_with_number(int(number)).word}")


@bot.command(name='alive')
async def alive(ctx, word):
    word_p = morph.parse(word)[0]
    live = morph.parse('живой')[0]
    if 'NOUN' == word_p.tag.POS:
        if 'anim' == word_p.tag.animacy:
            await ctx.send(f"{word.capitalize()} {live.inflect({word_p.tag.gender, word_p.tag.number}).word}")
        else:
            await ctx.send(f"{word.capitalize()} не {live.inflect({word_p.tag.gender, word_p.tag.number}).word}")


@bot.command(name='noun')
async def noun(ctx, word, one, two):
    word_p = morph.parse(word)[0]
    await ctx.send(word_p.inflect({two, one}).word)


@bot.command(name='inf')
async def inf(ctx, word):
    await ctx.send(morph.parse(word)[0].normal_form)







bot.run(TOKEN)