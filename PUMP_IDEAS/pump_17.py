# Level: 1

# Background

# The Arnaud Legoux Moving Average (ALMA) indicator was recently added to the family of moving averages. It was developed in 2009 by Arnaud Legous and Dimitrios Kouzis Loukas. Since then, this indicator has gained huge popularity among traders.

# ALMA works like any moving average work. However, the calculation of the ALMA is more perfect compared to the moving average. This indicator has minimal lag which makes it a leading indicator in the market. While the SMA, MA, EMA and SMMA signal line is often delayed. The ALMA was designed to address the two critical disadvantages of traditional moving averages, responsiveness and smoothness.

# Function

# L1 ALMA Trend Scalper is simple but powerful. This indicator makes full use of ALMA's rapid response advantage to provide buying and selling points by winding and crossing two short-term moving averages. A mid-term moving average can provide relatively effective support and pressure. Finally, the function of whale pump detection is simply realized through the characteristics of the moving average.

# Key Signal

# trendline --> mid term moving average for support and resistance
# tradingline ---> basic element for fast line and slow line
# fastline ---> fast line for short term
# slowline --> slow line for short term
# pumpstart ---> simple whale pump zone detection


# Pros and Cons

# Pros:

# 1. Simple but clear to see the trend reversals
# 2. Aux middle term moving average help just whether it is a true or fake breakout


# Cons:

# 1. No advanced trading skill is incorporated
# 2. Need improvements on sideways.


# Remarks

# Just be simple but powerful

# Readme

# In real life, I am a prolific inventor. I have successfully applied for more than 60 international and regional patents in the past 12 years. But in the past two years or so, I have tried to transfer my creativity to the development of trading strategies. Tradingview is the ideal platform for me. I am selecting and contributing some of the hundreds of scripts to publish in Tradingview community. Welcome everyone to interact with me to discuss these interesting pine scripts.

# The scripts posted are categorized into 5 levels according to my efforts or manhours put into these works.

# Level 1 : interesting script snippets or distinctive improvement from classic indicators or strategy. Level 1 scripts can usually appear in more complex indicators as a function module or element.

# Level 2 : composite indicator/strategy. By selecting or combining several independent or dependent functions or sub indicators in proper way, the composite script exhibits a resonance phenomenon which can filter out noise or fake trading signal to enhance trading confidence level.

# Level 3 : comprehensive indicator/strategy. They are simple trading systems based on my strategies. They are commonly containing several or all of entry signal, close signal, stop loss, take profit, re-entry, risk management, and position sizing techniques. Even some interesting fundamental and mass psychological aspects are incorporated.

# Level 4 : script snippets or functions that do not disclose source code. Interesting element that can reveal market laws and work as raw material for indicators and strategies. If you find Level 1~2 scripts are helpful, Level 4 is a private version that took me far more efforts to develop.

# Level 5 : indicator/strategy that do not disclose source code. private version of Level 3 script with my accumulated script processing skills or a large number of custom functions. I had a private function library built in past two years. Level 5 scripts use many of them to achieve private trading strategy.


#     // ____  __    ___   ________ ___________  ___________ __  ____ ___ 
#    // / __ )/ /   /   | / ____/ //_/ ____/   |/_  __<  / // / / __ |__ \
#   // / __  / /   / /| |/ /   / ,< / /   / /| | / /  / / // /_/ / / __/ /
#  // / /_/ / /___/ ___ / /___/ /| / /___/ ___ |/ /  / /__  __/ /_/ / __/ 
# // /_____/_____/_/  |_\____/_/ |_\____/_/  |_/_/  /_/  /_/  \____/____/                                              

# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © blackcat1402
# //@version=4

# study("[blackcat] L1 ALMA Trend Scalper", overlay=false)

# //functions
# xrf(values, length) =>
#     r_val = float(na)
#     if length >= 1
#         for i = 0 to length by 1
#             if na(r_val) or not na(values[i])
#                 r_val  :=  values[i]
#                 r_val
#     r_val

# //algorithm
# //define middle term trend line
# trendline =  alma((close-sma(close,40))/sma(close,40)*100,21,0.85,6)
# //plot middle term trend line
# plot(trendline,color=color.blue,linewidth=2)

# //define short term trading line
# tradingline = ema(ema(ema((2*close+high+low)/4,4),4),4)
# //define fast line
# fastline = ( sma((tradingline-xrf(tradingline,1))/xrf(tradingline,1)*100,1))*10
# //define slow line with ALMA()
# slowline = alma( sma((tradingline-xrf(tradingline,1))/xrf(tradingline,1)*100,2),3,0.85,6)*10

# //define whale pump start signal
# pumpstart = fastline>slowline and fastline<0

# //plot fast line and slow line
# pf = plot(fastline,color=color.yellow,linewidth=1)
# ps = plot(slowline,color=color.fuchsia,linewidth=1)
# fill(ps, pf, color=fastline>=slowline?color.yellow:color.fuchsia,transp=20)

# //use yellow color for long entry, fuchsia color as short entry, and lime color background for whale pump zone
# bgcolor(color=pumpstart?color.lime:na, transp=80)
# bgcolor(color=crossover(fastline,slowline)?color.yellow:na, transp=50)
# bgcolor(color=crossunder(fastline,slowline)?color.fuchsia:na, transp=50)

