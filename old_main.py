import discord
from modules.get_rank_data import pull_summoner_data
from modules.random_kanye import generate_inspiration
from modules.timestamp import create_timestamp
from modules.random_sentence import generate_sentence
from modules.discordbot_key import get_discord_key

launched_at_time = "Loading bot.. {}".format(create_timestamp())
print(launched_at_time)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('g.hello'):
        await message.channel.send("Hello")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.yo'):
        await message.channel.send("what's up gamer? 😜😝🤤😤🤑🥶🥴")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.rank'):
        await message.channel.send("Pulling data... 🤖"), await message.channel.send(pull_summoner_data())
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.help'):
        await message.author.send(
            '> https://github.com/JoshPaulie/PoybotPortable/wiki/Commands'), await message.add_reaction("📩")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.joker'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651996397041877006/clown_2.0.jpg")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.fword') or message.content.startswith('g.faggot'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/531913512822243358/651997280290734101/gamer.jpg")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.squad'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651997640950546443/IMG_3083.jpeg")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.bringe'):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/531913512822243358/651997904751427624/Hudboy.png")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith("g.paypig"):
        await message.channel.send("https://www.twitch.tv/dekar173")
        await message.add_reaction('🐽')
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith("g.pecs"):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/179743991137304576/651998903368941609/ripple.gif")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith("g.quads"):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/179743991137304576/651998926500790311/quadblast.gif")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith("g.kanye"):
        quote = generate_inspiration()
        await message.channel.send(quote)
        print(repr(message.content), message.author.name, create_timestamp(), "\n\n Quote:\n", quote, "\n")

    if message.content.startswith("g.whiskeyrad"):
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/177125557954281472/651996299843076096/Clownrad.png")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.tellmeabout'):
        sentence = generate_sentence()
        await message.channel.send(sentence)
        print(repr(message.content), message.author.name, create_timestamp(), "-", sentence)

    if message.content.startswith('g.github'):
        await message.author.send("> https://github.com/JoshPaulie/PoybotPortable")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.changelog'):
        await message.author.send("> https://github.com/JoshPaulie/PoybotPortable/wiki/Changelog")
        print(repr(message.content), message.author.name, create_timestamp())

    if message.content.startswith('g.mine') or message.content.startswith('g.ip'):
        minecraft_info = open("/resources/minecraft.txt").read()
        await message.author.send(minecraft_info), await message.add_reaction("📩")
        print(repr(message.content), message.author.name, create_timestamp())


client.run(get_discord_key())
