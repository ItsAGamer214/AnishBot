import os
import random
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get
from itertools import cycle
import json
import random

#^ basic imports for other features of discord.py and python ^
intents = discord.Intents.all()

client = commands.Bot(command_prefix='do ', intents= intents)
client.sniped_messages = None


@client.event
async def on_ready():
    print("bot online")  #will print "bot online" in the console when the bot is online


@client.command()
async def ping(ctx):
    await ctx.send(
        "pong!"
    )  #simple command so that when you type "!ping" the bot will respond with "pong!"


@client.command()
async def kick(ctx, member: discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send(
            "kicked " + member.mention
        )  #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")


@client.event
async def on_message_delete(message):

    client.sniped_messages = message

    print(message.content)
    print(message.author)

    if message.content == "":
        if message.attachments == []:
            pass
        else:
            print("test")
            f = open("logs.txt", "a")
            await f.write(message.attachments[0].url + "\n")
            await f.write(str(message.author) + "\n")
            await f.write(str(message.created_at) + "\n" + "\n")
            f.close()

    else:
        f = open("logs.txt", "a")
        f.write(message.content + "\n")
        f.write(str(message.author) + "\n")
        f.write(str(message.created_at) + "\n" + "\n")
        f.close()


@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


@client.command()
async def snipe(ctx):

    message = client.sniped_messages

    if client.sniped_messages is None:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    if message.content == "":
        if message.attachments == []:  # checks if there are any attachments
            pass  # if there are no attachments it will just move on to the next one
        else:  # simple else statement
            if message.author.id == 748516369087332436:  # checks if the bot sent the picture, if it #did it will not send it (replace 748516369087332436 with your bots id)
                return  # does nothing if the bot sended it

            else:  # another simple else statement
                await ctx.send(
                    message.attachments[0]
                )  # gets the last attachment sent, and only sends the url
                return  # breaks the command so that the bot will not keep on looking for attachments

    else:

        #makes the message look nice
        if message.channel == ctx.message.channel:

            embed = discord.Embed(description=message.content,
                                  color=discord.Color.purple(),
                                  timestamp=message.created_at)
            embed.set_author(
                name=f"{message.author.name}#{message.author.discriminator}",
                icon_url=message.author.avatar_url)
            embed.set_footer(text=f"Deleted in: #{message.channel.name}")

            await ctx.channel.send(embed=embed)


@client.command()
async def me(ctx):
    await ctx.send("Maybe i will")


@client.command()
async def remove(ctx):

    if str(ctx.message.author) == "TheLegend27#8183":
        messages = await ctx.channel.history(limit=50).flatten()
        await ctx.message.delete()
        for x in messages:
            if "name='AnishBot'" in str(x):
                await x.delete()


@client.command()
async def kritanu(ctx):
    print(ctx.message.guild)

    if ctx.message.author == "TheLegend27#8183" or ctx.message.author == "Surbeast#0055":

        await ctx.guild.ban("Krit#4288", reason="DIE")


@client.command()
async def pranav(ctx):
    await ctx.send("yea fs pranav is hot as hell")





#@client.command()
#async def eightball(ctx, message):

#  if message == "":
#    await ctx.send("What do you want me to predict?")

#  responses = [
#	"It is certain",
#	"It is decidedly so",
#	"Without a doubt",
#	"Yes – definitely",
#		"You may rely on it",
#		"As I see it",
#		"yes",
#		"Most Likely",
#		"Outlook good",
#		"Yes",
#		"Signs point to yes"
#	];
#   result = responses[random.randint(0,10)]
#  await ctx.send(result)



