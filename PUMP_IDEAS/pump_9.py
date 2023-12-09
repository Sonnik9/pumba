# This is using an EMA and RSI with slightly modified settings to give good entry and exit points while looking at Bitcoin. I use this on a 4-hour chart and with other indicators to find good positions to enter a trade or exit if things are turning red.

# If you click on the EMA line it will color the bars of the chart based on if they are above or below the EMA - This is just visually helpful for me to see the active trend.

# Make sure you hover over or click on the EMA line to see the colors of the candles change - it's not visible by default or without doing this.
# Май 27, 2021
# Информация о релизе:
# Fixed code that was causing the long and short alerts to fire at opposite times.
# Thanks to @pacbrother for catching this.
# Июн 1, 2021
# Информация о релизе:
# Removed offset=-1 which was displaying the L or S earlier than the alert would call it.
# I still don't recommend you use this at your only alert to enter or exit a trade. I just use this as a visual confirmation with other indicators.

# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © mmoiwgg

# //@version=4
# study(title="EMA+RSI Pump & Drop Swing Sniper (With Alerts)", shorttitle="EMA+RSI Swing", overlay=true)
# emaLength = input(title="EMA Length", type=input.integer, defval=50, minval=0)
# emarsiSource = input(close, title="EMA+RSI Source")
# condSource = input(high, title="Long+Short Condition Source")
# emaVal = ema(emarsiSource, emaLength)
# rsiLength = input(title="RSI Length", type=input.integer, defval=25, minval=0)
# rsiVal = rsi(emarsiSource, rsiLength)

# // Conditions
# shortCond = crossover(emaVal, condSource)
# longCond = crossunder(emaVal, condSource)

# // Plots Colors
# colors = emarsiSource > emaVal and rsiVal > 14 ? color.green : color.red
# emaColorSource = input(close, title="Line Color Source")
# emaBSource = input(close, title="Line Color B Source")

# // Plots
# plot(emaVal, color=emaColorSource[1] > emaVal and emaBSource > emaVal ? color.green : color.red, linewidth=3)
# plotcandle(open, high, low, close, color=colors)
# plotshape(series=shortCond, location=location.abovebar, style=shape.labeldown, color=color.red, size=size.tiny, text="S", textcolor=color.white, transp=0)
# plotshape(series=longCond, location=location.belowbar, style=shape.labelup, color=color.green, size=size.tiny, text="L", textcolor=color.white, transp=0)

# // Alert Conditions
# alertcondition(longCond, title='Long', message='Go Long')
# alertcondition(shortCond, title='Short', message='Go Short')
