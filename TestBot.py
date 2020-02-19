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
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Heroku Test"))

@bot.command()
async def show(ctx):
    embed = discord.Embed(title="Test", description="Descriptions", color=0x00ff00)
    embed.set_footer(text="footer")
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)
