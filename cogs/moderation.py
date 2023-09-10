import discord
from discord.ext import commands
from datetime import datetime

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command()
    @commands.has_any_role("Moderator", "Administrator", "Owner")
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick a user from the server"""
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

    @commands.command()
    async def delete(self, ctx):
        today = datetime.utcnow().date()
        def is_today(message):
            return message.created_at.date() == today
        deleted = await ctx.channel.purge(limit = None, check=is_today)
        await ctx.send(f"Deleted {len(deleted)-1} messages sent today.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))
