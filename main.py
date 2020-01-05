import discord
from discord.ext import commands
from modules.timestamp import create_timestamp
from modules.random_emoji import generate_emoji
from modules.get_rank_data import pull_summoner_data
from modules.random_kanye import generate_inspiration
from modules.random_sentence import generate_sentence
from modules.discordbot_key import get_discord_key
from modules.days_until_2020 import season_2020_start
import random
import datetime
from pathlib import Path
from modules.random_game import generate_random_game

pb_dir = Path('C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\')

client = discord.Client()
bot = commands.Bot(command_prefix="g.", case_insensitive=True)


def log(message: discord.Message):
    print(message.content, message.author.name, create_timestamp())

start_time = datetime.datetime.now()

@bot.event
async def on_ready():
    end_time = datetime.datetime.now()
    difference = end_time - start_time
    seconds_in_day = 24 * 60 * 60
    boot_time = divmod(difference.days * seconds_in_day + difference.seconds, 60)
    print('Connected! Launch time: {}s |'.format(boot_time[1]), create_timestamp())
    game = discord.Game(generate_random_game())
    await bot.change_presence(status=discord.Status.online, activity=game,afk=False)



@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author.bot:
        pass
    else:
        if 'daniel'in message.content:
            message_string = message.content
            await message.channel.send('>>> Beef Protection Act (BPA) Compliant Message from {}:\n{}'.format(message.author,message_string.replace('daniel','`[REDACTED]`')))
            await message.delete()
        elif 'Daniel'in message.content:
            message_string = message.content
            await message.channel.send('>>> Beef Protection Act (BPA) Compliant Message from {}:\n{}'.format(message.author, message_string.replace('Daniel', '`[REDACTED]`')))
            await message.delete()
    return


@bot.command(name='hello', aliases=['hi', 'hey', 'ho'])
async def hello(ctx: commands.Context):
    '''Simple greeting and first command'''
    message = ctx.message
    await message.channel.send("Hello there {}, I'm Poybot 2! {}".format(message.author.name, generate_emoji()))
    log(message)


@bot.command(name='yo', aliases=['yuh'])
async def yo(ctx: commands.Context):
    '''Better commands'''
    message = ctx.message
    await message.channel.send('What\'s up gamer {}? {}'.format(message.author.name, generate_emoji()))
    log(message)


@bot.command(name='rank', aliases=['ranks'])
async def rank(ctx: commands.Context):
    '''Pulls summoner ranks for list of gooners'''
    message = ctx.message
    await message.channel.send('Pulling rank data.. 🤖')
    await message.channel.send(pull_summoner_data())
    log(message)


@bot.command(name='joker', aliases=['clown'])
async def joker(ctx: commands.Context):
    '''sad man'''
    message = ctx.message
    await message.channel.send(
        'https://cdn.discordapp.com/attachments/177125557954281472/651996397041877006/clown_2.0.jpg')
    log(message)


@bot.command(name='fword')  # I do not condone this command
async def fword(ctx: commands.Context):
    '''Small child with heart of stone'''
    message = ctx.message
    await message.channel.send(
        'https://cdn.discordapp.com/attachments/531913512822243358/651997280290734101/gamer.jpg')
    log(message)


@bot.command(name='squad')
async def squad(ctx: commands.Context):
    '''When I roll up 🎶'''
    message = ctx.message
    await message.channel.send(
        "https://cdn.discordapp.com/attachments/177125557954281472/651997640950546443/IMG_3083.jpeg")
    log(message)


@bot.command(name='bringe')
async def bringe(ctx: commands.Context):
    '''Better cringe'''
    message = ctx.message
    await message.channel.send(
        'https://cdn.discordapp.com/attachments/531913512822243358/651997904751427624/Hudboy.png')
    log(message)


@bot.command(name='paypig')
async def foo(ctx: commands.Context):
    '''Link to Dekar's stream'''
    message = ctx.message
    await message.channel.send("https://www.twitch.tv/dekar173")
    await message.add_reaction('🐽')
    log(message)


@bot.command(name='pecs',aliases=['quads'])
async def foo(ctx: commands.Context):
    '''Soft porn [also g.quads]'''
    message = ctx.message
    await message.channel.send(
        'https://cdn.discordapp.com/attachments/179743991137304576/651998903368941609/ripple.gif {}\nhttps://cdn.discordapp.com/attachments/179743991137304576/651998926500790311/quadblast.gif {}'.format(generate_emoji(),generate_emoji()))
    log(message)


@bot.command(name='kanye')
async def kanye(ctx: commands.Context):
    '''Random quote from long list of curated Yezzus quotes. 🙏'''
    message = ctx.message
    quote = generate_inspiration()
    await message.channel.send(quote)
    # Another weird logging exception.
    print(message.content, message.author.name, create_timestamp(), quote)


@bot.command(name='tellmeabout')
async def tellmeabout(ctx: commands.Context, arg):
    '''Takes an input, replies w/ random adj and noun'''
    message = ctx.message
    sentence = generate_sentence(arg)
    await message.channel.send(sentence)
    # Logging UwU
    print(message.content, '-', message.author.name, '-', sentence)


@bot.command(name='github')
async def foo(ctx: commands.Context):
    '''View source code 🐍'''
    message = ctx.message
    await message.channel.send(
        '> https://github.com/JoshPaulie/PoybotPortable')
    log(message)


@bot.command(name='minecraft', aliases=['ip', 'minecrap', 'minecwaft', 'winecraft', 'mindcraft'])
async def minecraft(ctx: commands.Context):
    '''Messages user Goon Server information'''
    message = ctx.message
    minecraft_info = open("C:\\Users\\joshp\\PycharmProjects\\PoybotPortable\\resources\\minecraft.txt").read()
    await message.author.send(minecraft_info), await message.add_reaction("📩"), await message.add_reaction("<:golden_apple:655789383869267978>")
    log(message)


@bot.command(name="s20", aliases=["s2020", "s10", "season10"])
async def s20(ctx: commands.Context):
    '''[Temporary Command] Days until "Season 2020"'''
    message = ctx.message
    await message.channel.send(season_2020_start())
    log(message)

@bot.command(name='conbar', aliases=["conbon","jew"])
async def conbar(ctx: commands.Context):
    '''Days until Conrad's Bar Mitzvah'''
    start_date = datetime.datetime(2020, 3, 13)
    today_date = datetime.datetime.today()
    date_difference = start_date - today_date
    message = ctx.message
    await message.channel.send("There's only {} days until Conrad's Bar Mitzvah! *March 13rd!* 🔯".format(date_difference.days))
    log(message)

# Template
@bot.command(name="foo")
async def foo(ctx: commands.Context):
    '''Template command'''
    message = ctx.message
    await message.channel.send("Hey siri, define 'foo'")
    log(message)

bot.run(get_discord_key())
