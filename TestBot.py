import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

description = "Test bot"
bot = commands.Bot(command_prefix='!!', description=description)

@bot.event
async def on_ready():
    print(bot.user.id)
    print("Bot status: online")
    print("Bot command prefix : " + bot.command_prefix) 
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Testing"))

@bot.command()
async def add(ctx, left:int, right:int):
    await ctx.send(left + right)

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run('Njc5MjcyNTA4NTUzNDI5MDMy.Xku73w.e8l7mNhIxcG2Yy4aiscAxBrBUCI')
