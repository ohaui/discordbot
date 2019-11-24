import discord
import random
import pybooru
from resources.booruapi import getLinkBoorus
from resources.answersAskList import answersSosiList, randomSosiList, asksSosiList
from discord.ext import commands
from resources.random_cat import getCat, myGetCat, myGetlen, myCatPicDir
client = commands.Bot(command_prefix='.')
TOKEN = open("resources\TOKEN.txt", "r")# token
user = discord.user
client.remove_command('help')




#########################

@client.event
async def on_ready():
    print('logged on in as {}'.format(client.user.name))
    print('id : {}'.format(client.user.id))
    print('discordpy version is {}'.format(discord.__version__))
    await client.change_presence(activity=discord.Game('Работягу! .help'))


@client.event
async def on_message(message):
    content = message.content
    if any(word in content.lower() for word in answersSosiList):
        await message.channel.send('{} {}'.format(message.author.mention, random.choice(asksSosiList)))
    await client.process_commands(message)
    if str(message.author) == '':
        await message.channel.send('↑↑↑↑↑↑↑↑↑↑↑↑ \nклоун сказал')


@client.command(pass_context=True)
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except:
        await ctx.send("ТЫ СУКА ЗАЙДИ В ВОЙС, А ПОТОМ МЕНЯ ЗОВИ")


@client.command(pass_context=True)
async def leave(ctx):
    try:
        server = ctx.message.guild.voice_client
        await server.disconnect()
    except:
        await ctx.send("ЕБЛО ТУПОЕ Я НАХУЙ СЕЙЧАС НЕ В ВОЙСЕ ЧУДИЩЕ ТЫ СЛЕПОЕ БЛЯТЬ")


@client.command(pass_context=True)
async def Cat(ctx):
    await ctx.send(getCat())


@client.command(pass_context=True)
async def myCat(ctx):
    file = discord.File('{}\{}'.format(myCatPicDir, myGetCat()), myGetCat())
    await ctx.send("", file=file)


@client.command(pass_context=True)
async def myCatHowMuch(ctx):
    await ctx.send(myGetlen())


@client.command(pass_context=True)
async def help(ctx):
    HELPCOMMANDS = open("resources\HELPCOMMANDS.txt")
    await ctx.send(HELPCOMMANDS.read())
    HELPCOMMANDS.close()


@client.command(pass_context=True)
async def danbooru(ctx):
    mention = ctx.message.author.mention
    try:
        content = ctx.message.content
        replacedcontent = content.replace('.danbooru', '')
        post_data = getLinkBoorus(replacedcontent)
        if post_data[0] == None:
            await ctx.send('{}, в этом посте нет картинки, попробуй снова'.format(mention))
            print('NO PICTURE IN THIS POST')
        else:
            await ctx.send(post_data[0] + '\n####################################################\nartist - {}\nscore - {}'.format(post_data[2],post_data[1]))
            print('the picture from danbooru was sent successfully!')
    except pybooru.exceptions.PybooruHTTPError:
        await ctx.send('{}, нельзя запросить больше 2-ух тегов!'.format(mention))
    except IndexError:
        await ctx.send('{}, нет такого тега, либо арта с такими тегами не существует'.format(mention))
    except discord.HTTPException:
        await ctx.send('{}, тот тег заблокирован, либо возникла другая ошибка'.format(mention))
    except pybooru.exceptions.PybooruError:
        await ctx.send('{}, бот не подключен к VPN'.format(mention))
    except TypeError:
        await ctx.send('{}, параметр к тегу задан неверно, либо другая ошибка'.format(mention))
    except Exception as e:
        print(e)
client.run(TOKEN.read())
