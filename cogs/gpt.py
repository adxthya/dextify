import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1/chat/completions"

class Gpt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def query(self, ctx, *, query=None):
        if query:
            loading_message = await ctx.send("Fetching data...")

            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
            }

            data = {
                "model": "llama3-8b-8192",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant. Keep responses concise."},
                    {"role": "user", "content": query},
                ],
            }

            response = requests.post(GROQ_BASE_URL, headers=headers, json=data)

            if response.status_code == 200:
                message = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
            else:
                message = f"Error: {response.status_code} - {response.text}"

            await loading_message.edit(content=message)
        else:
            await ctx.send("Send a query following the command.")

async def setup(bot):
    await bot.add_cog(Gpt(bot))
