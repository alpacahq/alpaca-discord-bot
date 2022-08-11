import asyncio

from alpaca_trade_api.rest import REST, TimeFrame

import pandas_ta as ta
from matplotlib import pyplot as plt
import matplotlib.colors 
from datetime import date
from datetime import datetime, timedelta

from config import ALPACA_KEY, ALPACA_SECRET, DISCORD_TOKEN


rest_api = REST(ALPACA_KEY, ALPACA_SECRET, 'https://paper-api.alpaca.markets')


import os
import discord
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


intents = discord.Intents.default()

client = discord.Client(Intents = intents)
client = commands.Bot(command_prefix = '!', case_insensitive=True) 


#to get the console to tell you when the bot is ready to use
@client.event
async def on_ready():
    print('TA Plotter is ready')


def retrieve_data(arg1):
    # retrieve daily bar data for SPY in a dataframe
    d = datetime.today() - timedelta(days=180)
    d2 = datetime.today() - timedelta(days=2)
    dstr = d.strftime("20%y-%m-%d")
    d2str = d2.strftime("20%y-%m-%d")
    return rest_api.get_bars(arg1, TimeFrame.Day, dstr, d2str).df


# METHODS GENERATING THE VARIOUS TECHNICAL PLOTS

def gen_moving_averages(arg1):
    stock_bars = retrieve_data(arg1)

    df_sma20 = stock_bars.ta.ema(length=20)
    df_sma50 = stock_bars.ta.sma(length=50)
    df_sma80 = stock_bars.ta.sma(length=80)

    df_hma20 = stock_bars.ta.hma(length=20)
    df_hma50 = stock_bars.ta.hma(length=50)

    

    fig, ax = plt.subplots()
    plt.title(arg1.upper() + " Moving Averages")

    ax.plot(stock_bars["close"], '-k')
    ax.plot(df_sma20, 'lightsteelblue', label="sma20")
    ax.plot(df_sma50, 'royalblue', label="sma50")
    ax.plot(df_sma80, 'violet', label="sma80")
    ax.plot(df_hma20, 'wheat', label="hma20")
    ax.plot(df_hma50, 'lightcoral', label="hma50")
    ax.legend(loc="upper left")

    plt.savefig("output.png")

def gen_volatility(arg1):
  stock_bars = retrieve_data(arg1)
  
  df_acc50 = stock_bars.ta.accbands()
  df_rvi = stock_bars.ta.rvi()

  fig, dx = plt.subplots()
  title = arg1.upper() + " acc bands"
  plt.title(title)
  dx.plot(df_acc50, 'rosybrown', label="acc50")
  dx.plot(stock_bars["close"], '-k')
  dx.legend(loc="upper left")
  plt.savefig("output4.png")

  fig, ex = plt.subplots()
  title = arg1.upper() + " relative volatility index"
  plt.title(title)
  ex.plot(df_rvi, 'violet', label="rvi50")
  ex.legend(loc="upper left")
  plt.savefig("output5.png")
  
  
def gen_momentum(arg1):
    stock_bars = retrieve_data(arg1)

    df_macd = stock_bars.ta.macd()
    df_rsi = stock_bars.ta.rsi()
    
    fig, bx = plt.subplots()
    title = arg1 + ' Momentum'
    plt.title(title)
    bx.plot(df_macd, 'aquamarine', label="macd")
    bx.legend(loc="upper left")
    plt.savefig("output2.png")

    fig, cx = plt.subplots()
    title2 = arg1 + ' Relative Strength'
    plt.title(title2)
    cx.plot(df_rsi, 'salmon', label="RSI")
    cx.legend(loc="upper left")
    plt.savefig("output3.png")

def gen_trend(arg1):
    stock_bars = retrieve_data(arg1)

    df_vortex = stock_bars.ta.vortex()
    df_adx = stock_bars.ta.adx()
    
    fig, bx = plt.subplots()
    title = arg1 + ' vortex'
    plt.title(title)
    bx.plot(df_vortex, 'aquamarine', label="vortex")
    bx.legend(loc="upper left")
    plt.savefig("output2.png")

    fig, cx = plt.subplots()
    title2 = arg1 + ' adx'
    plt.title(title2)
    cx.plot(df_adx, 'salmon', label="adx")
    cx.legend(loc="upper left")
    plt.savefig("output3.png")


#COMMANDS INVOKING THE VARIOUS TECHNICAL PLOTS


@client.command()
async def show_moving_averages(ctx, ticker):
    gen_moving_averages(ticker)
    #await ctx.send_file(ctx.message.channel, f['output.png'], f['output2.png'], f['output3.png'])
    await ctx.send(file=discord.File('output.png'))
    #await ctx.send(file=discord.File['output.png'], file1=discord.File['output2.png'], file2=discord.File['output3.png'])


@client.command()
async def show_momentum(ctx, ticker):
    gen_momentum(ticker)
    await ctx.send(file=discord.File('output2.png'))
    await ctx.send(file=discord.File('output3.png'))
    #await ctx.send(file=discord.File['output3.png'])

@client.command()
async def show_volatility(ctx, ticker):
    gen_volatility(ticker)
    await ctx.send(file=discord.File('output4.png'))
    await ctx.send(file=discord.File('output5.png'))

@client.command()
async def show_trend(ctx, ticker):
    gen_trend(ticker)
    await ctx.send(file=discord.File('output2.png'))
    await ctx.send(file=discord.File('output3.png'))
    #await ctx.send(file=discord.File['output3.png'])

client.run(DISCORD_TOKEN)