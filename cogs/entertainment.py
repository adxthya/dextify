import discord
from discord.ext import commands
import requests

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def meme(ctx):
        result = requests.get("https://meme-api.com/gimme/")
        data = result.json()
        meme = data["url"]
        await ctx.channel.send(meme)

async def setup(bot):
    await bot.add_cog(Entertainment(bot))