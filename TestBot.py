import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot

description = "Test bot"
bot = commands.Bot(command_prefix='!!', description=description)

todoList = []

@bot.event
async def on_ready():
    print(bot.user.id)
    print("Bot status: online")
    print("Bot command prefix : " + bot.command_prefix) 
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Testing"))

@bot.command()
async def add(ctx, todo:str):
    todoList.append(todo)

@bot.command()
async def show(ctx):
    for todo in todoList:
        await ctx.send(todo)

@bot.command()
async def showembed(ctx):
    embed = discord.Embed(title="제목", description="설명", color=0x00ff00)
    embed.set_footer(text="푸터")
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)
