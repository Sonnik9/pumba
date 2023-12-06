# this is just a study to investigate the pumps and dumps that have been happened in a crypto market and it should not be used as an indicator. this is also my very first Pine Script that I've written and I am sure it is not perfect. actually I am curious to know when (I mean the exact time of the day) most pumps and dumps happen as a self investigation. the method that is used to define pumps and dumps is not good (and I know that) but I will modify it for better result in next version.

# to use this study, you should define whether you want to display pumps or dumps or both and also you should define percent of change (threshold).
# Авг 9, 2019
# Информация о релизе:
# I've made a few minor changes to the script and updated it. now it is in Pine Script version 4.0 syntax and the diagram is in histogram format.

# I am still in the process of developing a better solution to find pumps and dumps and even more important; when they are going to happen.

# Thanks for your attention,
# Апр 13, 2020
# Информация о релизе:
# some minor code formatting corrections


# //
# // @version=4
# // © Ehsan Haghpanah, (ehsanha)
# // Algorithmic Trading Research
# //
# // Pump and Dump Indicator (v0.1), 
# // note: pump and dump ticks must also be identified 
# // according to previous bars
# //

# study(title = "Pump|Dump Ticker", shorttitle = "Pump|Dump Ticker", overlay = false)

# // 
# // -- study parameter(s)
# display = input(title = "Display Options", defval = "Pumps", options = ["Pumps", "Dumps", "Both"])
# numeric_delta = input(15, "% Change", type = input.float)
# percent_delta = numeric_delta / 100

# //
# // -- study logic and calculation(s)
# change = (high - low)
# pump = ((close > open) and ((change / low) > percent_delta)) ? 1 : 0
# dump = ((close < open) and ((change / low) > percent_delta)) ? 1 : 0
# // pump series
# op = if display == "Pumps"
#     pump
# else
#     if display == "Dumps"
#         0
#     else
#         pump
# // dump series
# od = if display == "Dumps"
#     dump
# else
#     if display == "Pumps"
#         0
#     else
#         dump

# //
# // -- drawing and visualization
# plot(op, color = color.green,   linewidth = 2, title = "Tick", style = plot.style_histogram)
# plot(od, color = color.red,     linewidth = 2, title = "Tick", style = plot.style_histogram)