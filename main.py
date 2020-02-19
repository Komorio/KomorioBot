import discord
import asyncio
import os
import dbmanager
from discord.ext import commands
from discord.ext.commands import bot

description = "Komorio Manager bot"
bot = commands.Bot(command_prefix='>', description=description)

todoList = []

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Heroku Test"))

@bot.command()
async def AddTodo(ctx, todo, limitdate):
    dbmanager.AddTodo(todo, limitdate)    
    embed = discord.Embed(title=todo, description=limitdate, color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def ShowAllTodo(ctx):
    for data in dbmanager.GetAllData():
        embed = discord.Embed(title=data[0], description=data[1], color=0x00ff00)
        await ctx.send(embed=embed)

@bot.command()
async def DeleteTodo(ctx, todoName):
    embed = discord.Embed(title=todoName, color=0xff0000)
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)
