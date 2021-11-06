import discord
from discord.ext import commands
import inspect

# <-- Comandos administrativos --> #
class owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, cog: str):
        self.bot.unload_extension('cogs.'+cog)
        self.bot.load_extension('cogs.'+cog)

def setup(bot):
    bot.add_cog(owner(bot))
