# >  Imagen  < #
import discord
import io
import requests
import math
from PIL import Image, ImageOps
from discord.ext import commands
import utils

class picture(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='avatar', aliases=['icon', 'pfp'])
    async def _avatar(self, ctx, arg1):
        user = ctx.message.author
        if arg1:
            arg1 = utils.parse_mention(arg1)
            search = discord.utils.get(self.bot.users, id=arg1)
            if search:
                user = search
            else:
                return

        if user.is_avatar_animated() is True:
            gif = user.avatar_url_as(format='gif', size=2048)
            links = '[gif](%s)' % gif
        else:
            png = user.avatar_url_as(format='png', size=2048)
            jpg = user.avatar_url_as(format='jpg', size=2048)
            webp = user.avatar_url_as(format='webp', size=2048)
            links = '[png](%s) - [jpg](%s) - [webp](%s)' % (png, jpg, webp)

        embed = discord.Embed(description=links, color=user.color)
        embed.set_image(url=user.avatar_url)
        embed.set_footer(text=user)
        await ctx.send(embed=embed)

    @commands.command(name='invert', aliases=['inv', 'negativo'])
    async def _invert(self, ctx):
        await utils.OpsTransform(ctx, 0)

    @commands.command(name='crop', aliases=['cut'])
    async def _crop(self, ctx, factor):
        n = int(factor)
        await utils.OpsTransform(ctx, 1, n)

def setup(bot):
    bot.add_cog(picture(bot))
