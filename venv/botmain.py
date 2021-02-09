import discord
import os
from PersonalInfo.MyInfo import TOKEN
from discord.ext import commands
import robin_stocks
from PersonalInfo.MyInfo import usr, pwd

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
        news = robin_stocks.stocks.get_news(split[1])
        print(news)
        await message.channel.send(f"{news[0]['title']}")


client.run(TOKEN)