from init import *
from slashCommands import *

prefix = "?"

client = discord.Client
client = commands.Bot(command_prefix=prefix, self_bot=True)

@client.event
async def on_ready():
    
    print(f"Loggined in as {client.user.name}\n---")

@client.command()
async def farm(ctx, deposit=False):

    while True:
        triggerSlashCommand("fish", dankCommands["fish"], channel_id, guild_id)
        Hunt(channel_id, guild_id)

        await timeout(5)
        Beg(channel_id, guild_id)
        Dig(channel_id, guild_id)

        if deposit == True:
            await timeout(5)
            Deposit(channel_id, guild_id)

        await timeout(42)

client.run(token, bot=False)
