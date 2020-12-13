from os import environ as env
import discord
from discord import Game
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / 'bot.env'
load_dotenv(dotenv_path=env_path)
bot = commands.Bot(command_prefix='$')
bot.remove_command("help")
extensions = ['cogs.EMailer']

if __name__ == '__main__':
    print(discord.__version__)
    for extension in extensions:
        bot.load_extension(extension)
        print("[+]: Added Cog " + extension)


@bot.event
async def on_ready():
    await bot.wait_until_ready()
    print('[+]: Logged in at {0}'.format(datetime.now()))
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=Game(name="being a fruity EMail Agent"))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)


bot.run(env.get('DISCORD_TOKEN'))
