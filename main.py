import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
token = os.environ['DISCORD_BOT_TOKEN']


bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True, help_command=None)

@bot.event
async def on_ready():

    print(f'The bot is ready')


bot.run(token)