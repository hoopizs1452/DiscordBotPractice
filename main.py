import discord
from discord.ext import commands
from discord import file
import keep_alive
import json
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='>')

for filename in os.listdir('/home/runner/DiscordBotPractice/cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

@bot.event
async def on_ready():
    print(">>Bot is Online<<")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')
    welcome = bot.get_channel(int(jdata['Welcome_channel']))
    await welcome.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} leave!')
    leave = bot.get_channel(int(jdata['Leave_channel']))
    await leave.send(f'{member} leave!')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unoaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done.')

if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(os.environ['TOKEN'])#jdata['TOKEN']
