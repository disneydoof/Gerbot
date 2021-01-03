from os import error
import discord
import requests
from discord.ext import commands
import weather
import json
import os
from disputils import BotEmbedPaginator
import help


class Help(commands.Cog):
    """
    Creates the instance of admin including its fields
    @bot - the bot itself
    @last_member - last member to use this
    return - nothing
    """

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    """  
    Fetches a city's weather forecast from the input      
    @self - self obj
    @context - how we'll send messages
    @*args - arguments following the command
    return - nothing
    """

    @commands.command(aliases=["help", "commands"])
    async def HelpSystem(self, context, *args):
        """
        Open the commands json file that has all of our commands
        """
        with open("commands.json") as json_file:
            commands = json.load(json_file)
        """
        Assign the json instance to a variable
        """
        commands_link = commands["commands"]
        """
        Use the start and end position of the commands you want to add to each page
        """
        embeds = [
            discord.Embed(
                title="Page 1",
                description=help.PageData(commands_link, 0, 7),
                color=0x115599,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
            discord.Embed(
                title="Page 2",
                description=help.PageData(commands_link, 8, 15),
                color=0x5599FF,
            ).set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
        ]

        paginator = BotEmbedPaginator(context, embeds)
        await paginator.run()


"""
setup for the command
"""


def setup(bot):
    bot.add_cog(Help(bot))
