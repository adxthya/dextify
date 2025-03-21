import discord
from discord.ext import commands
import requests
import random

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def meme(self,ctx):
        result = requests.get("https://meme-api.com/gimme/")
        data = result.json()
        meme = data["url"]
        await ctx.channel.send(meme)

    @commands.command()
    async def quote(self,ctx):
        response  = requests.get("https://zenquotes.io/api/random")
        if(response.status_code != 200):
            await ctx.channel.send("Error fetching quote...")
            print(response.json())
        else:
            quote = response.json()[0]['q']
            await ctx.channel.send(quote)

async def setup(bot):
    await bot.add_cog(Entertainment(bot))
