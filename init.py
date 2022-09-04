import discord
from discord.ext import tasks, commands
import asyncio
from colorama import Fore, Style
import requests, json, websocket
import time

Red = Fore.LIGHTRED_EX
Orange = Fore.LIGHTYELLOW_EX
Green = Fore.LIGHTGREEN_EX
Reset = Fore.RESET

# Load Config File
f = open('config.json', 'r')
config = json.loads(f.read())

token = config["token"]
dankCommands = config["dankCommands"]

channel_id = config["channel_id"]
guild_id = config["guild_id"]

def warn(string):
    print(f"{Orange}[ Warning ] {string}{Reset}")

async def timeout(time):
    warn("Sleeping for {} seconds".format(time))
    await asyncio.sleep(time)

def show(string):
    print(f"{Green}[ Success ] {string}{Reset}")