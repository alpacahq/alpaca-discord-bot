# DiscordTradingBot
Creating Discord Bots that a) uses Pandas_TA commands for creating technical analysis plots from Alpaca Market Data and b) sends various types of orders using an Alpaca account.

**Setup**

First, access to an Alpaca account through the following link is required: https://app.alpaca.markets/. This allows access to market data and trading. Your key and secret_key credentials will be used by the bots to interact with Alpaca. Then, create discord bot(s) and a server to run it on. The Bot token credentials will be included in the code.

**Execution**

Use the code from this repo on your local machine, substituting the Alpaca key, Alpaca secret key, and Bot token with your personal credentials.

Then, use the code from the technical analysis or trading bot to run the code on your local computer. If you'd like one bot to have all the plot generator and ordering functionalities, combine the bodies of the two files.

To run commands, activate the bot and type !(command) (args) to run. 

Specific TA format: !show_(indicator type) (ticker)
example: !show_moving_averages tsla






