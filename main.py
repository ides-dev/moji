#!/usr/bin/env python
# Importa los módulos necesarios
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Carga el archivo .env
load_dotenv()
# Configura el prefijo y otros parámetros para los comandos
bot = commands.Bot(command_prefix=',', case_insensitive=True, help_command=None)
# Carga de cogs
for filename in os.listdir('./cogs/'):
    if filename.endswith('.py') is True:
        bot.load_extension('cogs.'+filename[:-3])
        print(f'Cog "{filename[:-3]}" cargado')

# Inicia sesión con el Token secreto
bot.run(os.getenv('DISCORD_TOKEN'))