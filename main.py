import discord
import asyncio
import os
import BotInformation as botinfo
import SchoolMenu as schoolMenu
import Todo as todo
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
async def 급식(ctx):
    description = ""
    index = 0
    for menu in schoolMenu.GetLunchMenu():
        description += menu + "\n \n"
        index += 1    

    if index != 0:
        embed = discord.Embed(title="🍚 오늘 급식", description=description, color=discord.Color.green())
    else :
        embed = discord.Embed(title="😔 밥이 없다", description="오늘은 밥이 없는 날.", color=discord.Color.teal())
    
    await ctx.send(embed=embed)    

@bot.command()
async def 오늘할일(ctx):
    todayTodos = todo.GetTodayTodo()
    index = 0

    for todayTodo in todayTodos:
        index += 1
        embed = discord.Embed(title="📚 오늘 할 일 : " + todayTodo[0], description=todayTodo[1], color=discord.Color.dark_teal())
        embed.set_footer(text=todayTodo[2])
        await ctx.send(embed=embed)

    if index == 0:
        embed = discord.Embed(title="🤗 짜쟌 할 일이 없네요", description="그럴리 없는데...🤔", color=discord.Color.dark_teal())
        await ctx.send(embed=embed)



@bot.command()
async def 오늘할일추가(ctx, todoTitle, description):
    todo.AddTodayTodo(todoTitle, description)
    embed = discord.Embed(title="📚 추가된 오늘 할 일 : " + todoTitle, description=description, color=discord.Color.dark_blue())
    await ctx.send(embed=embed)

@bot.command()
async def 내일할일추가(ctx, todoTitle, description):
    todo.AddTodayTodo(todoTitle, description)
    embed = discord.Embed(title="📚 추가된 내일 할 일 : " + todoTitle, description=description, color=discord.Color.blue())
    await ctx.send(embed=embed)


@bot.command()
async def 테스트(ctx):
    embed = discord.Embed(title="오늘 할일", description="오늘 할일 : ",color = discord.Color.dark_teal())
    embed.set_footer(text="하단 설명")
    await ctx.send(embed=embed)

token = os.environ["BOT_TOKEN"]
bot.run(token)