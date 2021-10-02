#  v1.0.0
#  prints randomly chosen calcifer quotes

import os
import random

import discord
from dotenv import load_dotenv
from calcLines import calcLines

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):

    welcome = f'hello {member.nick}'

    await member.send(welcome)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!howls':
        response = random.choice(calcLines)
        await message.channel.send(response)

    help = 'type `!howls` to use me. maybe i\'ll do more in the future.'
    if message.content == '!help':
         await message.channel.send(help)

client.run(TOKEN)