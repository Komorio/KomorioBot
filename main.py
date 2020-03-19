import discord
import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot

description = "Komorio Manager bot"
bot = commands.Bot(command_prefix=':', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Heroku Test"))

@bot.command()
async def 명령어(ctx):
    pass

@bot.command()
async def 테스트(ctx):
    embed = discord.Embed(title="테스트", description="이것은 테스트 embed",color = discord.Color.blue())
    embed.set_footer(text="하단 설명")
    await ctx.send(embed=embed)

# token = os.environ["BOT_TOKEN"]
token = "Njc5MjcyNTA4NTUzNDI5MDMy.XnOVqQ.Jy-hB5oz0kUE7NCI1_f_HgOlFlk"

bot.run(token)