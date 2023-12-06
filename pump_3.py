# **You must enable bar colors in the options for the script if you wish to see them**
# This indicator is very useful for spotting trends / tops / bottoms.

# This is the ultimate altcoin pump spotting tool. Use on higher timeframes for greatest accuracy. If altcoin is newish (ZEC for example), try 4h rather than 1D or 3D.

# Green = Uptrend
# Red = Downtrend
# Gray = Top/local top, bottom/local bottom, or continuation. You will need some knowledge of price action to determine which condition applies.

# You can use the oscillator at the bottom as a measure of momentum / trend strength. You can draw trendlines on the oscillator on the top/bottom or the interior.




# //@version=2
# //Drop me a line if you decide to use this code in any of your scripts.  Enjoy :D
# study("Pump_Doctor", shorttitle="1337_Volume_Trend")

# lookback = input(14)
# ebc=input(false, title="Enable bar colors")

# cumulativeup = 0
# countup = 0
# cumulativedown = 0
# countdown = 0
# for i=0 to lookback-1
#     if close[i] > open[i]
#         cumulativeup := cumulativeup + volume[i]
#         countup := countup + 1
#     else
#         cumulativedown := cumulativedown + volume[i]
#         countdown := countdown + 1

# averagevolumeup = (cumulativeup / countup)
# averagevolumedown = -(cumulativedown / countdown)

# sigup = (averagevolumeup) <= volume and close > open
# sigdown = (averagevolumedown) >= -volume and close < open
# regup = averagevolumeup >= volume and close > open
# regdown = averagevolumedown <= -volume and close < open
# volplot = close > open ? volume : close < open ? -volume : na
# volcolor = sigup ? lime : sigdown ? #FF0000 : regup ? green : regdown ? #990000 : na



# flow = cumulativeup - cumulativedown
# flowcolor = flow > 0 ? lime : flow <=0 ? red : na



        
# purgatory = (flow > 0 and flow[1] > 0) and sigdown
# purgatory1 = (flow < 0 and flow[1] < 0) and sigup

# barc = ebc ? ((flow > 0 and not sigdown) ? lime : (flow < 0 and not sigup) ? red : purgatory ? silver : purgatory1 ? silver : silver) : na

# plot(flow, color=volcolor, style=histogram, linewidth=1)
# plot(flow, color=flowcolor, linewidth=2)
# barcolor(barc)




