# Bars of largest range (volatility)

# * see moments of strongest price action immediately
# * colored & upDown by candle color
# * amplifier: you see only the bull runs, and subsequent dumps

# Very nice on the 5 years scale of BITSTAMP:BTCUSD - nothing comparable to 2013 has happened yet.

# Internals:
# squared_range = pow(high-low, 2)

# That is essentially it already. The rest are details:
# * gauge with (in case of Bitcoin exponentially rising) price
# * show in red for negative candles
# * take even higher polynomial (than 2) to show only the very largest values
# * allow some user input (but there is not much more that can be chosen here.)

# Sorry for such a simple formula - but sometimes the easiest things are powerful.

# Please give feedback. www.tradingview.com/u/akd and/or in the cryptocurrency chat. Thanks.


# //@version=3
# study("WhenWasThePriceAction")

# // by @akd
# // begun on 2017 May 29th
# // my very first PineScript
# // version v0.1.0
# // Please give feedback. https://www.tradingview.com/u/akd Thanks

# donation_text   = "Like this? You can donate to [BTC]"
# donation_address= "14NxQ61xhnoqaDxs3Xb5Ps5pJQhJDXezEh"


# squared_range = pow(high-low, 2)  
# // this is it already, essentially. 
# // The rest are details: 
# // * gauge with (in case of Bitcoin exponentially rising) price
# // * show in red for negative candles
# // * take even higher polynomial (than 2) to show only the very largest values
# // * allow some user input (but there is not much more that can be chosen here.)


# average_price_length = input(title="price averager how many bars (not so important)", type=integer, defval=10)
# average_price = ema((high+low)/2, average_price_length)

# linewidth=input(title="line width", type=integer, defval=2)

# upOrDown = sign(close[0]-open[0])
# color = upOrDown > 0 ? green : red

# showNegativesBelow = input(title="show negative values below", type=bool, defval=true)

# amplifier = input(title="amplifier for strongest signals", type=float, defval=1, minval=0, maxval=5, step=0.2)

# whatToPlot = (pow(squared_range / average_price / average_price, amplifier)) * (showNegativesBelow ? upOrDown : 1)

# plot(whatToPlot, color=color, linewidth=linewidth, style=histogram)

# ignoreAnswer = input(title=donation_text, type=string, defval=donation_address)

