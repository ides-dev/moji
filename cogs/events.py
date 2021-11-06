# Módulos
import discord
from discord.ext import commands
import traceback
import sys
from utils import funcs

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"""
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Iniciando sesión como {self.bot.user}
{len(self.bot.guilds)} servidores
{len(self.bot.users)} usuarios
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
""")
        await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(',help'))

    # Errores de comando
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        # Comando no encontrado
        if isinstance(error, commands.CommandNotFound):
            return
        # No disponible en MD
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(f'{ctx.command} no está disponible en Mensaje Directo.')
        # Argumento inválido o sin ellos
        elif isinstance(error, (commands.errors.MissingRequiredArgument, commands.errors.BadArgument)):
            helper = funcs.create_help(ctx.command)
            await ctx.send(embed=helper)
        # Error interno
        else:
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

    # Si se ejecuta un comando
    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'[{ctx.author}] {ctx.message.clean_content}')

    # Evento de mensaje
    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignorar los mensajes de bots
        if message.author.bot is True:
            return
        # Se detecta una mención a si mismo
        if self.bot.user in message.mentions:
            await message.channel.send('¿Qué tal? Puedes probar enviando `,help`')


def setup(bot):
    bot.add_cog(Events(bot))
