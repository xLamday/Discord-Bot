import discord
from discord.ext import commands
import aiohttp
import os
from dotenv import load_dotenv
from webhooks.examplesimple import test_simple

load_dotenv()
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
token = os.environ['DISCORD_BOT_TOKEN']


bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True, help_command=None)

@bot.event
async def on_ready():

    print(f'The bot is ready')
    commands = await bot.tree.sync()
    try:
        print("Trying to sync commands...")
        print(f"Synchronized {len(commands)} commands")
    except Exception as error:
        print(error)



def has_permissions(ctx):
    return discord.utils.get(ctx.author.roles, name="YOUR PERMISSION NAME") is not None

@bot.command(name="embed_simple")
async def embed_simple(ctx: commands.Context):
    if has_permissions(ctx):
        try:
            await test_simple()
        except Exception as error:
            print(error)
    else:
        ctx.send("You do not have the permission to execute this command", ephemeral=True)



bot.run(token)