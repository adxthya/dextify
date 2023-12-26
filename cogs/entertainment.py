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
    async def waifu(self,ctx):
        random_number = random.randint(0, 6)
        url = 'https://api.waifu.im/search'
        tags = ['maid','marin-kitagawa','mori-calliope','raiden-shogun','oppai','selfies','uniform']
        tag = tags[random_number]
        params = {
            'included_tags': [tag]
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            image = data["images"][0]["url"]
            await ctx.channel.send(tag)
            image_message = await ctx.channel.send(image)
            await image_message.add_reaction('😍')
            await image_message.add_reaction('❤️')
        else:
            print('Request failed with status code:', response.status_code)

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