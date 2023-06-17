import discord
from discord.ext import commands
import random


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)
client = discord.Client(intents=intents, command_prefix="$")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('nitro'):
        while True:
            nom = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLMNBVCXZ"
            totalgen = 16
            nitro_code = "".join(random.sample(nom,totalgen))
            await message.channel.send(f"https://discord.gift/{nitro_code}")
    


client.run('MTA0MDcwMDc2MzQwOTc2NDM1Mg.G7TeDC.SfxEeLemm9Uz_VoJCzHdvQrT4Xcvzx-ZYJ2zOg')