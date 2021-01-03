import discord
import requests
from discord.ext import commands
import json
import os.path
from os import path


class Professor_Scraper(commands.Cog):
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
    deletes the role that is selected
    @self - self obj
    @context - how we'll send messages
    @prof_name - Professor name that will be searched
    @class_code - Code used to select 5 reviews
    return - nothing
    """

    @commands.command(pass_context=True, aliases=["class-review", "cr"])
    async def get_professor_rating(self, context, prof_name, class_code):
        command_prefix = "!class-review"
        command_name = "professor review"
        alias = "class-review"
        example = "!class-review matthew-gerber cop3502"
        prof_name = prof_name.replace("-", " ")
        if (
            path.isfile(
                "professor_classes_data/" + prof_name + "/" + class_code + ".json"
            )
            == False
        ):
            profs = ", ".join(os.listdir("professor_classes_data"))

            print(profs)
        else:
            base_dir = "professor_classes_data/" + prof_name + "/"

            with open(
                "professor_classes_data/" + prof_name + "/" + class_code + ".json", "r"
            ) as loop:
                reviews = json.load(loop)
            class_message = discord.Embed(
                title=prof_name + " - " + class_code + " reviews",
                description="Reviews",
            )
            for i in range(0, len(reviews[class_code]["class_data"])):
                class_name = reviews[class_code]["class_data"][i]["class_name"]
                quality = reviews[class_code]["class_data"][i]["quality"]
                comment = reviews[class_code]["class_data"][i]["comment"]
                difficulty = reviews[class_code]["class_data"][i]["difficulty"]
                would_take_again = reviews[class_code]["class_data"][i][
                    "would_take_again"
                ]
                date = reviews[class_code]["class_data"][i]["date"]
                class_message.add_field(
                    name="Review " + str(i + 1),
                    value="Review posted on: "
                    + date
                    + "\nWould take again: "
                    + would_take_again
                    + "\nQuality: "
                    + str(quality)
                    + "\ndifficulty: "
                    + str(difficulty)
                    + "\nComment: "
                    + comment
                    + "\n",
                )
            class_message.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/715261258622042162/776881557968388136/gerber-attack.gif"
            ),
            await context.send(embed=class_message)


def setup(bot):
    bot.add_cog(Professor_Scraper(bot))
