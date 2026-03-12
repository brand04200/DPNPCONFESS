import discord
from discord.ext import commands
from src.handlers.confession_handler import ConfessionHandler

class ConfessionCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.handler = ConfessionHandler(bot)

    @commands.command(name='confess')
    async def confess(self, ctx, *, confession: str):
        """Submit a confession."""
        if not confession:
            await ctx.send("Please provide a confession message.")
            return

        await self.handler.handle_confession(ctx, confession)

def setup(bot):
    bot.add_cog(ConfessionCog(bot))