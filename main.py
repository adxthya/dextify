import discord
from discord.ext import commands
from datetime import datetime
import os
import requests

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")    

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")


@bot.command()
@commands.has_any_role("Moderator", "Administrator", "Owner")
async def ban(ctx, member:discord.Member, *, reason: None):
    if reason == None:
        reason = "This user was banned by" + ctx.message.author.name
    await member.ban(reason=reason)
    
@bot.command()
@commands.has_any_role("Moderator", "Administrator", "Owner")
async def kick(ctx, member:discord.Member, *, reason: None):
    if reason == None:
        reason = "This user was banned by" + ctx.message.author.name
    await member.kick(reason=reason)

@bot.command()
async def delete(ctx):
    today = datetime.utcnow().date()
    def is_today(message):
        return message.created_at.date() == today
    deleted = await ctx.channel.purge(limit = None, check=is_today)
    await ctx.send(f"Deleted {len(deleted)-1} messages sent today.")

@bot.command()
async def weather(ctx,*,location):
  data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={os.getenv('API')}&units=metric")
  weather_data = data.json()
  temperature = weather_data["main"]["temp"]
  await ctx.channel.send(f"The temperature is {temperature} degree celcius")

@bot.command()
async def meme(ctx):
  data = requests.get("https://meme-api.com/gimme/")
  meme = data.json()
  memes = meme["url"]
  await ctx.channel.send(memes)
  
bot.run(os.getenv("TOKEN"))

