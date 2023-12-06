# Volume can be a very useful tool if used correctly. Relative volume is designed to filter out the noise and highlight anomalies assisting traders in tracking institutional movements. This tool can be used to identify stop loss hunters and organized dumps. It uses a variety of moving averages to hide usual activity and features an LSMA line to show trend. Trend columns are shown to highlight activity and can be seen at bottom of the volume columns, this is done using ZLSMA and LSMA.
# snapshot
# The above chart shows an example of 2 indicators being used on the 15 min chart. The bottom indicator is set to the 1 min chart. Traders can see a large dump on the 1 min chart as institutions wipe out any tight stop losses. Next they buy back in scooping up all those long positions.
# snapshot
# This is an example layout using a split screen setup and multiple timeframes ranging from 1 min to 30 mins. This gives a clear indication of trends and make it easy to pickup on institutional behaviour. Tip: Double clicking indicator background will maximize RVOL to the split screen window.
# Июн 13, 2021
# Информация о релизе:
# Added signals and alerts
# -Signal for entry point
# -Alert for when volume crosses defined amount.
# -Alert for entry point

# snapshot
# Entry point signals pick up great on the 1 second to 1 min charts.
# Июн 14, 2021
# Информация о релизе:
# Fixed entry signal and added price line
# Июн 14, 2021
# Информация о релизе:
# Added current bar volume. Can be turned off in settings.
# Июн 18, 2021
# Информация о релизе:
# Fixed problem with current bar volume number
# Июн 21, 2021
# Информация о релизе:
# Fixed rounding issue.
# Июн 22, 2021
# Информация о релизе:
# Ticker ID can now be turned on in settings for split screen setups.
# snapshot
# Авг 15, 2021
# Информация о релизе:
# Added option to display average volume. Previously this indicator just filtered out the noise. Now it also highlights anomalies. This extra plot gives traders many different options to present the data. Here are some examples:
# snapshot
# snapshot
# snapshot
# By changing the style options for the volume columns traders can switch between column, histogram or step line. Removing the blue moving averages can clean the indicator or even remove everything but the anomalies. Adjusting transparency can also help hide the volume columns to give a more traditional look as seen in the 3rd example on top indicator. These anomaly columns are big movements in volume and tend to dictate the short term trend of price action.









# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © veryfid

# //@version=4
# study("Relative Volume", shorttitle="RVOL", format = format.volume)
# lsmalength = input(50,"LSMA Length",group = "General Settings")
# avglength = input(30,"Lookback bars for Average",group = "General Settings")
# volalert = input(200000000, title = "Alert when volume reaches",group = "General Settings")
# showalert = input(false, "Show Alert Signal?",group = "General Settings")
# showentry = input(true, "Show Entry Signals?",group = "Entry Signals")
# showvol = input(true, "Show Current Volume?",group = "General Settings")
# showavg = input(false, title = "Show Average",group = "General Settings")
# showrvol = input(false, "Show RVOL Calculation?",group = "General Settings")
# showlsma21 = input(true,"Show LSMA 21 Entry Points", group = "Entry Signals")
# showlsma6 = input(true,"Show LSMA 6 Entry Points",group = "Entry Signals")
# showticker = input(false, "Show Ticker ID?",group = "General Settings")
# tickercol = input(color.blue, "Ticker ID Color",group = "Color Options")
# showanom = input(true, "Show Anomalies",group = "General Settings")
# showtrend = input(false, title = "Show Trend Columns",group = "General Settings")


# x = "k"
# vol = volume

# if volume < 1000
#     x := ""
# if volume >= 1000
#     vol := volume / 1000
# if volume >= 1000000
#     x := "M"
#     vol := volume / 1000000
# if volume >= 1000000000
#     x := "B"
#     vol := volume / 1000000000


    
# len = 20
# ma1 = sma(volume,len)
# ma2 = linreg(volume,lsmalength,0)
# ma3 = linreg(volume,21,0)
# ma4 = linreg(volume,6,0)

# length = 21
# std = 21
# src = volume
# hullma = wma(2*wma(src, length/2)-wma(src, length), floor(sqrt(length)))
# source = volume
# windowsize = 9
# offset = 0.85
# sigma = 6

# lsma2 = linreg(ma2, len, 0)
# a = ma2-lsma2
# zlsma = ma2+a

# cond1 = crossover(ma2,0)
# if showlsma21 and not showlsma6
#     cond1 := crossover(ma2,0) or crossover(ma3,0)
# if showlsma6 and not showlsma21
#     cond1 := crossover(ma2,0) or crossover(ma4,0)
# if showlsma6 and showlsma21
#     cond1 := crossover(ma2,0) or crossover(ma3,0) or crossover(ma4,0)   
# cond2 = crossover(volume, volalert)
# cond3 = volume > ma2

# plot(volume, style = plot.style_columns, color = close > open ? #00ffaa : color.red, title = "Volume", trackprice=true)
# plotshape(showentry? cond1 : na, title="Entry Signal", location=location.top, style=shape.circle, size=size.tiny, color=color.yellow, transp=0)

# plot(hullma, title = "Hull MA", style = plot.style_area,transp = 70)
# plot(alma(source, windowsize, offset, sigma), style = plot.style_area,transp = 50, title = "ALMA")
# plot(stdev(volume,std), style = plot.style_area,transp = 70, title = "Std Deviation")
# plot(ma1, style = plot.style_area,transp = 60, title = "SMA")
# //plot(zlsma, color = #b2ebf2, linewidth = 1, title = "ZLSMA")
# plot(ma2, color = #b2ebf2, linewidth = 1, title = "LSMA")
# dif = zlsma - ma2
# plot(showtrend and dif > 0 ? dif : na , style = plot.style_columns,transp = 40, color = #fff9c4, title = "Trend Columns")
# plotshape(showalert ? cond2 : na, title="Volume Alert", location=location.bottom, style=shape.diamond, size=size.tiny, color=color.red, transp=0)
# clean = volume - ma2
# plot(showanom and clean > stdev(volume,std) ? volume : na, style = plot.style_columns , color = close > open ? #00ffaa : color.red, title = "Anomalies")
# alertcondition(cond2, title='Volume Alert', message='Volume Alert')
# alertcondition(cond1, title='Volume Entry Alert', message='Volume Entry Alert')
# alertcondition(cond3, title='Increased Volume', message='Increased Volume Alert')

# avg = array.new_float(0)
# for i = 1 to avglength
# 	array.push(avg, volume[i])
# avg3 = array.new_float(0)
# for i = 1 to avglength
# 	array.push(avg3, vol[i])

# rvol = volume / array.avg(avg)

# y = "k"
# avg1 = array.avg(avg)
# avg2 = avg1
# if avg1 < 1000
#     y := ""
# if avg1 >= 1000
#     avg2 := avg1 / 1000
# if avg1 >= 1000000
#     y := "M"
#     avg2 := avg1 / 1000000
# if avg1 >= 1000000000
#     y := "B"
#     avg2 := avg1 / 1000000000
# var table perfTable = table.new(position.top_right, 3, 2, border_width = 0)

# i_posColor = input(color.rgb(38, 166, 154), title="Positive Color",group = "Color Options")
# i_negColor = input(color.rgb(240, 83, 80), title="Negative Color",group = "Color Options")

# f_fillCell(_table, _column, _row, _value) =>
#     _c_color = close > open ? i_posColor : i_negColor
#     _cellText = tostring(_value, "#.##") + x
#     table.cell(_table, _column, _row, _cellText, text_color = _c_color)

# f_fillCell4(_table, _column, _row, _value) =>
#     _c_color = close > open ? i_posColor : i_negColor
#     _cellText = tostring(_value, "#.##") + y
#     table.cell(_table, _column, _row, _cellText, text_color = color.blue)

# f_fillCell3(_table, _column, _row, _value) =>
#     _c_color = close > open ? i_posColor : i_negColor
#     _cellText = tostring(_value, "#.##")
#     table.cell(_table, _column, _row, _cellText, text_color = color.yellow)
    
# if barstate.islast and showvol
#     f_fillCell(perfTable, 2, 0, vol)
# if barstate.islast and showavg
#     f_fillCell4(perfTable, 1, 0, avg2)
# if barstate.islast and showrvol
#     f_fillCell3(perfTable, 0, 0, rvol)
    
# var table perfTable2 = table.new(position.top_center, 1, 2, border_width = 0)

# f_fillCell2(_table, _column, _row, _value) =>
#     table.cell(_table, _column, _row, text_color = tickercol, text= syminfo.tickerid + " " + timeframe.period)
# if barstate.islast and showticker
#     f_fillCell2(perfTable2, 0, 0, syminfo.description)

