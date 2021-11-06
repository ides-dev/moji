# ------------------ #
#    Herramientas    #
# ------------------ #
import discord
from discord.ext import commands
from discord.ext.commands import clean_content
class Tools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(Tools(bot))
