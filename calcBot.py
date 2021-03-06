#  v2.0.0
#  prints randomly chosen calcifer quotes

# TODO:
    # mute users based on keywords in a message
    # create emotes
    # return lyrics to a song
    # remove default help command & replace it with custom
    # implement cogs

import os
import random
import discord

from discord.ext import commands
from dotenv import load_dotenv
from constants import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

helpCmd = commands.DefaultHelpCommand(no_category = 'Commands')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = commandPrefix, intents=intents, help_command=helpCmd)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    await client.change_presence(status=discord.Status.online, activity=discord.Game('powering the castle'))

@client.event
async def on_member_join(member):

    welcome = f'hello {member.nick}'

    await member.send(welcome)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

# !howls
@client.command(help = help.howls)
async def howls(ctx):
    response = random.choice(calcLines)
    await ctx.send(response)

# !createEmote
@client.command()
async def createEmote(ctx, img):
    await ctx.send('placeholder')

# !getLyrics
# @client.command()
# async def getLyrics(ctx, title, artist):
#     return

client.run(TOKEN)