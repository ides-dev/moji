import discord
from discord.ext import commands
import random
import requests
import urllib
from PIL import Image, ImageOps
import io

def create_help(command):
	title = '%s, %s' % (command.name, ', '.join(command.aliases))
	color = random.randint(0, 0xFFFFFF)
	embed = discord.Embed(
		title=title, description=command.description, color=color)
	if command.usage:
		usage = '`%s %s`' % (command.name, command.usage)
		embed.add_field(name='Uso', value=usage)
	return embed

async def getImages(ch):
	url = None
	async for msg in ch.history():
		if msg.attachments:
			for attachment in msg.attachments:
				if attachment.height:
					url = attachment.url
					break
		# Deja de buscar si encuentra algo, ya que el valor de la URL cambió a la del archivo adjunto.
		if url:
			break
	if not url:
		raise commands.CommandError('No se encontraron imágenes en este canal.')
	return url

def request_json(url, params):
	req = requests.get(url, params=params)
	return req.json()


def encode_uri(string):
	return urllib.parse.quote(string, safe='~()*!.\'')

def user_id(string):
  return string.strip(' <@!> ')
  
async def OpsTransform(ctx, seed: int = 0, n1: float = 0, n2: float = 0):
	#seed = 0 if not seed else seed
	#n1 = 0 if not n1 else n1
	#n2 = 0 if not n2 else n2
	nearest = int(round(n1))
	# Como la imagen no la va a sacar de nuestro sistema de archivos, vamos a dejar que HTTP consiga la imagen por nosotros.
	original = await getImages(ctx.channel)
	req = requests.get(original)
	image = req.content
	# Abrir la imagen en bytes, es más fácil para Pillow al momento de leer y escribir.
	imageToTransform = Image.open(io.BytesIO(image)).convert('RGB')
	transformations = {
		0: ImageOps.invert(imageToTransform),
		1: ImageOps.crop(imageToTransform, nearest),
		2: ImageOps.scale(imageToTransform, n1, resample=3),
		3: ImageOps.flip(imageToTransform),
		4: ImageOps.grayscale(imageToTransform),
		5: ImageOps.mirror(imageToTransform),
		# n1 debe ser un valor entre 0 y 128
		6: ImageOps.solarize(imageToTransform, threshold=nearest),
		# n1 debe ser un valor entre 1 y 8
		7: ImageOps.posterize(imageToTransform, bits=nearest),
		# n1 debe ser un valor entre 0 y 255
		8: ImageOps.autocontrast(imageToTransform, cutoff=nearest)
	}
	transformedImage = transformations.get(seed)
	saveLocation = io.BytesIO()
	transformedImage.save(saveLocation, format="png")
	saveLocation.seek(0)
	# Enviar la imagen modificada a Discord
	result = discord.File(saveLocation, filename="hayami_output.png")
	await ctx.send('', file=result)

def parse_mention(args):
	return args.sub('<!@#?&>', '')

regions = [
    ('amsterdam', '🇳🇱 Países Bajos, \nÁmsterdam'),
    ('brazil',  '🇧🇷 Brazil'),
    ('dubai',  '🇦🇪 Emiratos Árabes\nUnidos, Dubai'),
    ('eu-central', '🇪🇺 Europa Central'),
    ('eu-west', '🇪🇺 Europa Occidental'),
	('europe', '🇪🇺 Europa'),
	('frankfurt', '🇩🇪 Fráncfort'),
	('hongkong', '🇨🇳 China, Hong\nKong'),
	('india', '🇮🇳 India'),
	('japan', '🇯🇵 Japón'),
	('london', '🇬🇧 Londres'),
	('russia', '🇷🇺 Rusia'),
	('singapore', '🇸🇬 Singapur'),
	('southafrica', '🇿🇦 Sudáfrica'),
	('south-korea', '🇰🇷 Corea del Sur'),
	('sydney', '🇦🇺 Sídney'),
	('us-central', '🇺🇸 Estados Unidos,\nCentro'),
	('us-east', '🇺🇸 Estados\nUnidos,\nEste'),
	('us-south', '🇺🇸 Estados\nUnidos,\nSur'),
	('us-west', '🇺🇸 Estados Unidos,\nOeste'),
	('vip-amsterdam', '🇳🇱 (VIP) Países\nBajos, Ámsterdam'),
	('vip-us-east', '🇺🇸 (VIP) Estados\nUnidos, Este'),
	('vip-us-west', '🇺🇸 (VIP) Estados\nUnidos, Oeste')
]