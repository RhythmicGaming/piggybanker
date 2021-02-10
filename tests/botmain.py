import discord
import os
from discord.ext import commands
from PersonalInfo.MyInfo import TOKEN
import robin_stocks
from PersonalInfo.MyInfo import usr, pwd

HELP_DICT = {'hello':'$hello bot will respond hello!',
             'hist':'$hist written $hist TICKER INTERVAL SPAN where interval can be 5minute, hour, day, month etc; span is the length of time in question, when used without a span default is week',
             'check':'$check takes a ticker symbol and returns its current list price',
             'check-details':'$check-details takes a ticker and returns a detailed report',
             'headline':'$headline takes in a ticker and returns the last published headline relevant to the name'}
client = discord.Client()
bot = commands.Bot(command_prefix='$')


#login with your(my) creds
login = robin_stocks.login(usr, pwd)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hist'):
        split = message.content.split()

        #for piece in split:
            #await message.channel.send(f"{piece}")
        if not split[3]:
            split[3] = 'week'
        list_prices = robin_stocks.stocks.get_stock_historicals(split[1], interval=split[2], span=split[3])
        for price in list_prices:
            await message.channel.send(f"{price}")
    if message.content.startswith('$check'):
        split = message.content.split()
        this_price = robin_stocks.stocks.get_latest_price(f'{split[1]}')
        await message.channel.send(f'{this_price}')

    if message.content.startswith('$check-details'):
        split = message.content.split()
        this_price = robin_stocks.stocks.get_latest_price(f'{split[1]}')
        await message.channel.send(f'{split[1]} {this_price[0]}')

    if message.content.startswith('$headline'):
        split = message.content.split()
        if len(split) > 1:
            news = robin_stocks.stocks.get_news(split[1])
            if news != []:
                await message.channel.send(f"{news[0]['title']}")
            else:
                await message.channel.send(f"No recent events are found for {split[1]}")
        else:
            await message.channel.send(f"Please include a ticker symbol to be searched")

    if message.content.startswith('$help'):
        split = message.content.split()
        print(split)
        if len(split) != 1:
            if 'list' in split:
                for k in HELP_DICT.keys():
                    await message.channel.send(f"{k}")
            else:
                if split[1] in HELP_DICT.keys():
                    await message.channel.send(f"{split[1]}: {HELP_DICT[f'{split[1]}']}")
                else:
                    await message.channel.send("invalid help command")

        else:
            await message.channel.send(f"Welcome to RobinTheHood a discord bot for all your market needs to begin type a command starting with $ or try $help list")


client.run(TOKEN)