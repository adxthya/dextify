import discord
from discord.ext import commands
import openai

openai.api_key = 'anything'
openai.base_url = "http://localhost:3040/v1/"

class Gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def query(self,ctx,query=None):
        if(query):
            loading_message = await ctx.send("Fetching data...")
            completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": query},
            ],
            )
            message = completion.choices[0].message.content
            await loading_message.edit(content=message)
        else:
            await ctx.send("Send a query following the command")

async def setup(bot):
    await bot.add_cog(Gpt(bot))
