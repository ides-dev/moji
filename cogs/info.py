# ----------------- #
#    Información    #
# ----------------- #
import discord
from discord.ext import commands
import random
from utils import funcs
class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='commands', aliases=['cmds'])
    async def _commands(self, ctx, command: str=None):
        await ctx.send(ctx.author.mention + ', checa esto: https://ides.neocities.org/hayami_cmds.html')

    @commands.command(name='help', aliases=['h'])
    async def _help(self, ctx):
        color = random.randint(0, 0xFFFFFF)
        embed = discord.Embed(title='Ayuda', color=color)
        embed.add_field(name='Lista de comandos', value=',commands', inline=False)
        embed.add_field(name='Enlace de invitación',
            value='[(✿◡‿◡)](https://discord.com/api/oauth2/authorize?client_id=675768552451604503&permissions=104721985&scope=bot)', inline=False)
        await ctx.send(embed=embed)

    @commands.command(name='user', aliases=['member'])
    async def _user(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
        else:
            user = ctx.message.author

        tag = user
        if user.bot is True: tag += ' (BOT)'
        embed = discord.Embed(title=tag, color=user.color)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name='Fecha de creación', value=user.created_at, inline=False)
        embed.add_field(name='Miembro desde', value=user.joined_at, inline=False)
        embed.add_field(name='Roles', value=user.roles, inline=False)
        embed.set_footer(text='ID: '+str(user.id))
        await ctx.send(embed=embed)

    @commands.command(name='server', aliases=['guild'])
    async def _server(self, ctx):
        guild = ctx.message.guild
        region = str(guild.region)
        for old, new in funcs.regions:
            region = region.replace(old, new)
        embed = discord.Embed(title=guild.name,
            description=guild.description, color=0x7289da)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name='Creador', value=guild.owner, inline=True)
        embed.add_field(name='Región', value=region)
        embed.add_field(name='Miembros', value=len(guild.members))
        embed.add_field(name='Canales', value=len(guild.channels))
        embed.add_field(name='Emojis', value=len(guild.emojis))
        embed.add_field(name='Roles', value=len(guild.roles))
        embed.add_field(name='Fecha de creación',
            value=guild.created_at, inline=False)
        embed.set_footer(text='ID: '+str(guild.id))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
