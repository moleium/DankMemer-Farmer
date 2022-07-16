# Credit to Pineapple#1000 and MOLE#2165 On Discord

import discord, os, asyncio

from discord.ext import commands

from colorama import Fore, Style

token = "your token here"

#Bot prefix, like ?help

prefix = "?"

def endSong(guild, path):

    os.remove(path)

#Clear Command

def Clear():

    os.system('clear')

#Colors

def RandomColor():

    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))

    return randcolor

def RandString():

    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

#Prefix

client = discord.Client()

client = commands.Bot(command_prefix=prefix,self_bot=True)

#Dep

@client.command(name='dankmemer', aliases=['dank', 'dmc'])

async def dankmemer(ctx):

    await ctx.message.delete()

    count = 0

    while True:

        try:

            count += 1

            await ctx.send('pls dep max', delete_after=0.1)

            

            await ctx.send('pls beg', delete_after=0.1)

            print(f'{Fore.BLUE}[DANK-MEMER]'+Fore.RESET)

            await asyncio.sleep(45)

        except Exception as e:

            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

#Farm

@client.command(name='dank-farm', aliases=['dankfarm'])

async def _fish_dank(ctx): # b'\xfc'

    await ctx.message.delete()

    count = 0

    while True:

        try:

            count += 1

            await ctx.send('pls fish', delete_after=0.1)

            await ctx.send('pls hunt', delete_after=0.1)

            await ctx.send('pls dig', delete_after=0.1)

            print(f'{Fore.BLUE}[AUTO-FARM] {Fore.GREEN}Farm number: {count} sent'+Fore.RESET)

            await asyncio.sleep(46)

        except Exception as e:

            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

           

#onReady

@client.event

async def on_ready():

	print(f"You are Online :)")

client.run(token,bot=False)
