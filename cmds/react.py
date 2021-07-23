import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def picture(self, ctx):
        random_picture = random.choice(jdata['picture_file'])
        picture = discord.File(random_picture)
        await ctx.send(file=picture)
        
    @commands.command()
    async def urlpicture(self, ctx):
        random_picture = random.choice(jdata['url_picture'])
        await ctx.send(f'{random_picture}')
def setup(bot):
    bot.add_cog(React(bot))