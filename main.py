#!/usr/bin/env python

from random import randrange, choice, randint
import discord
import asyncio
import time
from requests import get

TOKEN_AUTH = "" # YOUR TOKEN HERE
ip = "" # YOUR IP HERE, LEAVE BLANK IF YOU DONT USE A VPN

client = discord.Client()
@client.event
async def on_ready():
    print(client.guilds)
    
@client.event
async def on_reaction_add(reaction, user):
    print("Someone reacted")
    if reaction.emoji == "🎉":
        if reaction.author.bot:
            print(f"Detected giveaway, sleeping")
            await asyncio.sleep(round(randint(5,10)))
            await reaction.message.add_reaction("🎉")
            ban.append(reaction.message.id)
            print(f"Reacted!")

@client.event
async def on_message(message):
    if "bot" in message.content.lower():
        print(f"PanicSleep: {message.content.lower()}")
        time.sleep(60)
        print("PanicSleepEnd")
        return

      
if get('https://api.ipify.org').text != str(ip):
    client.run(TOKEN_AUTH, bot=False)
else:
    print("HOME IP")
    quit()
