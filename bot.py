# nin.py
import os
import discord
from discord.ext import tasks, commands

TOKEN = os.getenv("DISCORD_TOKEN")  # read from env

GUILD_ID = 601117178896580608
CHANNEL_ID = 1138130467057565747

intents = discord.Intents.default()
# only enable if necessary:
# intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    greet_loop.start()

@tasks.loop(minutes=10)
async def greet_loop():
    guild = bot.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hi there! 👋")

if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set DISCORD_TOKEN environment variable before running.")
    bot.run(TOKEN)
