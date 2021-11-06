# Módulos
import discord
from discord.ext import commands
import random
import utils

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 8ball
    @commands.command(name='8ball', aliases=['question', '8b'])
    async def ball(self, ctx, *, question: str):
        answers = ['Si.', 'No.', 'Tal vez~', '¡Por supuesto!', 'No entiendo.', 'Meh.',
                   'Quieren que lo baneen dice.', 'No cuentes con ello', 'Espero que no', '¡VAMOS!',
                   'No estoy seguro.', 'Pregunta de nuevo.', 'Si... y no.', '¡Solo soy un bot! o(TヘTo)',
                   'Ni siquiera lo pienses.', 'Ahora no.', 'Sospechoso... <(￣︶￣)>', 'No lo pidas a gritos.',
                   'Perspectivamente bueno.', 'No puedo predecirlo ahora.', 'Hola, que tal.',
                   'Concentrate y pregunta de nuevo.', 'Si, lo soy.', 'Calla.', 'Tenía.',
                   'Si, pero no, pero si, pero no... difícil decisión.', 'Pregunta eso a mi creador.',
                   '...Esa pregunta no me dejó dormir por 10 noches seguidas.', 'En la friendzone. ',
                   'No tiene nada de malo, tranquilo. ヽ(*・ω・)ﾉ',
                   '¿Tú que piensas sobre eso? 🤔', 'Juega juegos friv.', 'Difícil de predecir. (x_x)',
                   'Wumpus te observa.', 'A', 'E']
        await ctx.send('🎱 %s' % random.choice(answers))
    # talk
    @commands.command(name='talk', aliases=['hey'])
    async def talk(self, ctx, *, text: str):
        text = utils.encode_uri(text)
        request = utils.request_json('https://chatbotapi.glitch.me/api', {'tipo': 'get', 'texto': text})
        await ctx.send(request['resultado'])

def setup(bot):
    bot.add_cog(Fun(bot))