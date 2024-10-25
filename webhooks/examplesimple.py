import aiohttp
import asyncio
from discord import * 
import os
from dotenv import load_dotenv
load_dotenv

async def test_simple():
     async with aiohttp.ClientSession() as session:
        if 'WEBHOOK_ID' in os.environ and 'WEBHOOK_TOKEN' in os.environ:
            webhook_id = os.environ['WEBHOOK_ID']
            webhook_token = os.environ['WEBHOOK_TOKEN']
            webhook = Webhook.partial(webhook_id, webhook_token, session=session)
            await webhook.send(embed=Embed(
                 title = "Test",
                colour = Colour.blue(),
                 description = """This is a test"""
            ))
        else:
            print("Variables webhook_id or webhook_token not found")
        