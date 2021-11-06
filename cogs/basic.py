# Módulos
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash import SlashCommand
from discord_slash import SlashContext

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # ping
    @commands.command(name='ping', aliases=['pong', 'ms'],
        description='Muestro mi latencia actual.')
    async def _ping(self, ctx):
        await ctx.send(f'Pong! `{round(self.bot.latency, 2)}ms`')
    # say
    @commands.command(name='say', aliases=['s'],
        description='Recibo argumentos ya establecidos por el usuario, y los envío de vuelta.',
        usage='<argumentos>')
    async def _say(self, ctx, *, text: str):
        await ctx.send(text)

def setup(bot):
    bot.add_cog(Basic(bot))
