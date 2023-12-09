# Dump Detecter uses Stochastic RSI to detect dumps/downtrends. Can be used as an exit trigger for long bots or an entry trigger for short bots. Change settings to lower timeframe for scalping. Pump signals can be turned on with tickbox.

# Default Settings are not the usual Stochastic RSI setup and have been tuned to bitcoin 3hr chart:
# Timeframe = 3hrs
# smoothK = 3
# smoothD = 3
# lengthRSI = 6
# lengthStoch = 27
# src = close
# Май 29, 2021
# Информация о релизе:
# Added a range filter for pump and dump detection, It was set to only pickup crossovers/crossunders over the 50 line on the Stochastic RSI indicator. Now default settings is to pick up all crosses. To use those old settings adjust "crossover/under must be greater than" to 50. Traders can choose to only pickup dump signals when Stochastic is overbought by making min value 80 and max value 100. Likewise for the opposite detecting pumps only in oversold range by setting min value to 0 and max value to 20.
    


# // © veryfid

# //@version=4
# study(title="Dump Detector - Stochastic RSI", shorttitle="Dump Detector - SRSI", overlay=true)
# res = input(title="Indicator Timeframe", type=input.resolution, defval="180")
# smoothK = input(3, "K", minval=1)
# smoothD = input(3, "D", minval=1)
# lengthRSI = input(6, "RSI Length", minval=1)
# lengthStoch = input(27, "Stochastic Length", minval=1)
# src = input(close, title="RSI Source")
# rsi = rsi(src, lengthRSI)
# mindump = input(0, "Dump Crossunder must be greater than:", minval=0, maxval=100)
# maxdump = input(100, "Dump Crossunder must be less than:", minval=0, maxval=100)
# minpump = input(0, "Pump Crossover must be greater than:", minval=0, maxval=100)
# maxpump = input(100, "Pump Crossover must be less than:", minval=0, maxval=100)
# showpump = input(defval = false, title = "Show Pump Signals?")

# k = security(syminfo.tickerid, res, sma(stoch(rsi, rsi, rsi, lengthStoch), smoothK))
# d = security(syminfo.tickerid, res, sma(k, smoothD))

# dump = k > mindump and k < maxdump and crossunder(k,d)
# plotshape(dump, title="Dump Warning", location=location.abovebar, style=shape.triangledown, size=size.tiny, color=color.red, transp=20)

# pump = k > minpump and k < maxpump and crossover(k,d) 
# plotshape(showpump ? pump : na, title="Dump Warning", location=location.belowbar, style=shape.triangleup, size=size.tiny, color=color.lime, transp=20)
# alertcondition(dump, title='Dump Detected', message='Dump Detected')
# alertcondition(pump, title='Pump Detected', message='Pump Detected')


