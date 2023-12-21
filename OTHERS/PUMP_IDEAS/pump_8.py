# My very first indicator in Pine Script with two alert conditions for trading bots.
# It's based on "Pump Catcher" by @joepegler

# I modified some parts, hopefully improved the usability and enabled alerts, so you can use it to trigger bots like 3commas via webhooks.

# Pump Alerts 🚀 attempts to "detect moments of abnormal and accelerating increase in volume" AKA "pumps". Small and big pumps.
# I recommend using it on small timeframes like 1 to 15 min and tinkering with the lookback period as well as threshold values.
# Other than that it's pretty self-explanatory and beginner-friendly.

# Free and Open Source. Let me know how you use it!





# //@version=4
# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // based on "Pump Catcher" study by @joepegler
# // https://www.tradingview.com/u/herrkaschel

# study("Pump Alerts", precision=2)
# length = input(title="Lookback period (1 - 4999)", type=input.integer, defval=420, minval=1, maxval=4999)
# bigPumpThreshold = input(title="Big Pump Threshold (0.01 - 99.99)", type=input.float, defval=10, minval=0.01, maxval=99.99, step=0.01)
# smallPumpThreshold = input(title="Small Pump Threshold (0.01 - 99.99)", type=input.float, defval=0.5, minval=0.01, maxval=99.99, step=0.01)

# mav = sma(volume, length)  // Average volume within lookback period
# difference = mav - mav[1]  // Difference between average lookback period volume and latest candle
# volumeIncreasing = difference > 0  // Is the volume increasing? 
# valueIncreasing = close > close[1]  // Is the value increasing? 
# increasing = valueIncreasing and volumeIncreasing
# vroc = increasing ? difference * (100 / mav[1]) : 0  // If it's increasing then set the rate, otherwise set it to 0

# // To normalise the data express the current rate of change as a % of the maximum rate of change the asset has ever had.
# historicMax = 0.0
# firstVrocNormalizedValue = 10  // Because ICO coins generally kickoff trading with a lot of volatility
# historicMax := vroc > historicMax[1] ? vroc : nz(historicMax[1], firstVrocNormalizedValue)
# vrocNormalized = vroc / historicMax * 100

# plot(vrocNormalized, color=#F2F2F2, linewidth=1)
# hline(smallPumpThreshold, title='Small Pump Threshold', color=color.lime, linewidth=1)
# hline(bigPumpThreshold, title='Big Pump Threshold', color=color.red, linewidth=1)

# alertcondition(vrocNormalized >= smallPumpThreshold, title="Small Pump")
# alertcondition(vrocNormalized >= bigPumpThreshold, title="Big Pump")



