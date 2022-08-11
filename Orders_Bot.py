#SETUP
import pip
import discord
import discord.ext
from discord.ext import commands, tasks
# pip.main(['install', 'alpaca_trade_api'])

from alpaca_trade_api.rest import REST, TimeFrame

API_KEY = '***'
SECRET_KEY = '***'
rest_api = REST(API_KEY, SECRET_KEY, 'https://paper-api.alpaca.markets')

TOKEN = '***'

intents = discord.Intents.default()

client = discord.Client(Intents=intents)
client = commands.Bot(command_prefix='!', case_insensitive=True)


#to get the console to tell you when the bot is ready to use
@client.event
async def on_ready():
    print('TA Plotter is ready')


#commands to place orders
@client.command()
async def market_buy_by_quantity(ctx, ticker, qty):
    rest_api.submit_order(symbol=ticker,
                          qty=qty,
                          type="market",
                          side="buy",
                          time_in_force="day")


@client.command()
async def market_buy_by_price(ctx, ticker, price):
    rest_api.submit_order(symbol=ticker,
                          notional=price,
                          type="market",
                          side="buy",
                          time_in_force="day")

@client.command()
async def limit_buy_by_quantity(ctx, ticker, qty, limitprice):
    rest_api.submit_order(symbol=ticker,
                          qty=qty,
                          type="limit",
                          side="buy",
                          time_in_force="day",
                          limit_price = limitprice)
  
@client.command()
async def limit_buy_by_price(ctx, ticker, price, limitprice):
    rest_api.submit_order(symbol=ticker,
                          notional=price,
                          type="limit",
                          side="buy",
                          time_in_force="day",
                          limit_price = limitprice)

@client.command()
async def sell_by_price(ctx, ticker, price):
    rest_api.submit_order(symbol=ticker,
                          notional=price,
                          type="market",
                          side="sell",
                          time_in_force="day")

  
@client.command()
async def sell_by_quantity(ctx, ticker, qty):
    rest_api.submit_order(symbol=ticker,
                          qty=qty,
                          type="market",
                          side="sell",
                          time_in_force="day")


@client.command()
async def limit_sell_by_quantity(ctx, ticker, qty, limitprice):
    rest_api.submit_order(symbol=ticker,
                          qty=qty,
                          type="limit",
                          side="sell",
                          time_in_force="day",
                          limit_price = limitprice)
  
@client.command()
async def limit_sell_by_price(ctx, ticker, price, limitprice):
    rest_api.submit_order(symbol=ticker,
                          notional=price,
                          type="limit",
                          side="sell",
                          time_in_force="day",
                          limit_price = limitprice)


client.run(TOKEN)
