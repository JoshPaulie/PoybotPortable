import discord
from commandList import printCommandsInDiscord
from getRankData import pull_summoner_data
from randomKanye import generate_inspiration
from timestamp import create_timestamp

print("Loading bot.. {}").format(create_timestamp())

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('g.hello'):
        await message.channel.send("```Hello```")
        print("- {} issued the hello command at {}".format(message.author.name, create_timestamp()))

    if message.content.startswith('g.yo'):
        await message.channel.send("```what's up gamer?```")
        print("- {} issued the yo command at {}".format(message.author.name, create_timestamp()))

    if message.content.startswith('g.rank'):
        print("Rank Pulled!")
        await message.channel.send("```Pulling data... 🤖```")
        await message.channel.send(pull_summoner_data())
        print("- {} issued the rank command at {}".format(message.author.name, create_timestamp()))

    if message.content.startswith('g.help'):
        await message.channel.send(printCommandsInDiscord())
        print(" - {} issued the help command at {}".format(message.author.name, create_timestamp()))

    if message.content.startswith('g.joker'):
        print(" - {} issued the joker command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651996397041877006/clown_2.0.jpg")

    if message.content.startswith('g.fword'):
        print(" - {} issued the fword command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/531913512822243358/651997280290734101/gamer.jpg")

    if message.content.startswith('g.squad'):
        print(" - {} issued the squad command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651997640950546443/IMG_3083.jpeg")

    if message.content.startswith('g.bringe'):
        print(" - {} issued the bringe command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/531913512822243358/651997904751427624/Hudboy.png")

    if message.content.startswith("g.paypig"):
        print(" - {} issued the paypig command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send("https://www.twitch.tv/dekar173")

    if message.content.startswith("g.pecs"):
        print(" - {} issued the pecs command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/179743991137304576/651998903368941609/ripple.gif")

    if message.content.startswith("g.quads"):
        print(" - {} issued the quads command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/179743991137304576/651998926500790311/quadblast.gif")

    if message.content.startswith("g.kanye"):
        print(" - {} issued the kanye command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(generate_inspiration())

    if message.content.startswith("g.whiskeyrad"):
        print(" - {} issued the whiskeyrad command at {}".format(message.author.name, create_timestamp()))
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651996299843076096/Clownrad.png")


client.run('NjUxNTgwMjk1OTQ1OTEyMzQw.Xeb9oA.zhmazOcAy1sXWUrnTRAIewaTreE')
