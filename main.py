import discord
import asyncio
import os
import BotInformation as botinfo
from discord.ext import commands
from discord.ext.commands import bot

description = "Komorio Manager bot"
bot = commands.Bot(command_prefix=':', description=description)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Heroku Test"))

@bot.command()
async def 설명(ctx):
    embed = discord.Embed(title="🔗 봇 설명", description=botinfo.GetBotExplanation(), color=discord.Color.blue())
    embed.set_footer(text="🛠 개발자 : Komorio")
    await ctx.send(embed=embed)

@bot.command()
async def 명령어(ctx):
    description = ""     
    
    for info in botinfo.GetCommands():
        description += info + "\n"

    embed = discord.Embed(title="명령어 목록", description=description ,color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def 프로필(ctx):
    description = ""
    
    for info in botinfo.GetProfile():
        description += info + "\n"

    embed = discord.Embed(title="🤔 프로필", description=description, color=discord.Color.blue())
    await ctx.send(embed=embed)    

@bot.command()
async def 테스트(ctx):
    embed = discord.Embed(title="테스트", description="이것은 테스트 embed",color = discord.Color.blue())
    embed.set_footer(text="하단 설명")
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)