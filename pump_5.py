# This indicator is based on Smart Money MCDX
# (Pine editor @v4)

# Indicator built for cryptocurrencies.
# Best for day trading.

# The coin seems overbought but still pump? Check this indicator
# This indicator help you see when institutional buyer enter/exit trade and is a good combination with RSI + Stochastic RSI .

# This indicator focus on buying activity by big players and is built for LONG or SPOT, shorter can still use it to determine when to exit short (if smart money appear on a significant TF you may not enter/stay in a short).

# Banker plot show strong buyer activities (appear generally when RSI already overbought but still increasing).


# It appear as a Histogram with a color code to better see the fading strength of the institutional activity :

# Light Blue Bar = Institutional presence ( bullish )
# Green Bar = Pump candle (very bullish ), (Banker > Banker MA)
# Orange Bar = Retest candle = natural decline after a growth (Banker < Banker MA)
# Black Bar = Down candle = progressive exit of institutional leads to this candle, you must have TP before.
# Red Bar = Dump candle = steep decline, the institutional take profit hard. You better be out before that one.


# Hot-Money plot show momentum and react fast to price action.
# It appear as a filled zone (red or green) depending on the plot position compared to its average.
# In a downtrend you may only see this one.

# Key-Signals:

# "Bullish signal 𓃓" = open a long

# "Sell signal 💲" = close the long

# I recommend you don't keep all the signals enabled at first.
# (feel free to ask me the use of the other signals)


# It seemed to me that SMART MONEY MCDX was counter-intuitive and archaic,
# So i made this one for personal use,
# I'm happy if this indicator helps you,

# Have a good trade


# // © LOKEN94
# //
# // Custom version based of [M2J] Indicator | MCDX
# // 
# // 
# // 
# // Changes:
# // No more useless Retaillers Money, no more counter intuitive color.  
# // Added uneditable black solid line at the bottom to hide negative Banker histogram.

# //@version=4
# study("LOKEN 𓃓 (v4) BULLISH MCDX v2.2", "𓃓",precision=2)


# RSIBaseBanker       = input(50,  "Banker Base",           minval = 10)
# RSIPeriodBanker     = input(50,  "Banker RSI Period",     minval = 10)
# RSIBaseHotMoney     = input(30,  "Hot Money RSI Base",    minval = 10)
# RSIPeriodHotMoney   = input(40,  "Hot Money RSI Period",  minval = 10)
# SensitivityBanker   = input(1.5, "Sensitivity Banker",    minval = 0.1, step = 0.1)
# SensitivityHotMoney = input(0.7, "Sensitivity Hot Money", minval = 0.1, step = 0.1)

# rsi_function(sensitivity, rsiPeriod, rsiBase) =>
#     rsi = sensitivity * (rsi(close, rsiPeriod) - rsiBase)
#     if rsi > 20
#         rsi := 20
#     else if rsi < 0
#         rsi := 0
#     rsi 

# rsi_Banker   = rsi_function(SensitivityBanker,   RSIPeriodBanker,   RSIBaseBanker)
# rsi_HotMoney = rsi_function(SensitivityHotMoney, RSIPeriodHotMoney, RSIBaseHotMoney)

# plot(rsi_HotMoney, "Hot Money", #00026d17, 3, plot.style_area)
# plot(rsi_Banker,   "Banker",    color=rsi_Banker>0?#84afc9:#84afc900, linewidth=4, style=plot.style_histogram)
# hot=plot(rsi_HotMoney,display=display.none,editable=false)
# bank=plot(rsi_Banker,display=display.none,editable=false)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# hotma2=rma(rsi_HotMoney,2)
# bankma2=sma(rsi_Banker,2)
# hotma7=rma(rsi_HotMoney,7)
# bankma7=ema(rsi_Banker,7)
# hotma31=rma(rsi_HotMoney,31)
# bankma31=ema(rsi_Banker,31)
# //plot(hotma2)
# //plot(bankma2)
# //plot(hotma7)
# //plot(bankma7)
# //plot(hotma31)
# //plot(bankma31)
# hotma=ema(((hotma2*34)+(hotma7*33)+(hotma31*33))/100,2)
# bankma=sma(((bankma2*70)+(bankma7*20)+(bankma31*10))/100,1)
# hotsignal=rma(hotma,2)
# banksignal=rma(bankma,4)
# hotline=plot(hotma,style=plot.style_line,color=hotma>hotsignal?#00ff0a:#ff0014,transp=75, title="Hot Money MA",display=display.all,editable=false)
# bankline=plot(bankma,style=plot.style_line,color=bankma>banksignal or bankma>bankma[1]?#00ff0a:#ff881e30,transp=25, title="Banker MA",display=display.all,editable=false)
# hotline2=plot(hotsignal,style=plot.style_line,color=hotma>hotsignal?#00ff0a:#ff881e,transp=75, title="Hot Money MA2",display=display.all,editable=false)
# bankline2=plot(banksignal,style=plot.style_line,color=banksignal<0.1?#000000:#ff881e80,transp=50, title="Banker MA2",display=display.all,editable=true)
# //
# fill(hotline,hotline2, color=hotma>hotsignal?#00ff0a:#ff0014,transp=85, title="Fill : Hot-Money MA")
# fill(bankline,bankline2, color=bankma>banksignal?#00ff0a00:#ff9800,transp=85, title="Fill : Banker MA")
# fill(hotline,hot, color=rsi_HotMoney>hotma?#00ff0a40:#9b0000,transp=50, title="Fill : HOT")

# //
# hbma=vwma(((rsi_HotMoney*10)+(hotma*35)+(hotsignal*15)+(bankma*35)+(banksignal*5))/100,1)
# major=wma(hbma,9)
# lowma2=sma(rsi_Banker/2,1)
# lowma3=sma(rsi_Banker/3,1)
# lowma4=sma(rsi_Banker/4,1)
# lowma5=sma(rsi_Banker/5,1)
# lowma6=sma(rsi_Banker/6,1)
# lowma7=sma(rsi_Banker/7,1)
# lowmaster=sma(((lowma2*1)+(lowma3*1)+(lowma4*1)+(lowma5*1)+(lowma6*1)+(lowma7*1))/6,1)
# lowamp=sma(((lowma2*1)+(lowma3*1)+(lowma4*1)+(lowma5*1)+(lowma6*1)+(lowma7*1))/1,1)
# //LOW2=plot(lowma2)
# //LOW3=plot(lowma3)
# //LOW4=plot(lowma4)
# //LOW5=plot(lowma5)
# //LOW6=plot(lowma6)
# //LOW7=plot(lowma7)
# lowampsignal=ema(lowamp,31)
# LOWAMP2=plot(lowampsignal,display=display.none,editable=false)
# lowmsignal=ema(((lowmaster*90)+(lowamp*10))/100,7)
# LOWM2=plot(lowmsignal,display=display.none,editable=false)


# GMA=plot(major,color=hbma>8.5?#00862c:#9b0000,transp=80,display=display.none,editable=false)
# HBMA=plot(hbma,style=plot.style_line,linewidth=3,color=hbma>major and hbma>8.5?#00862c60:#e5d75c60,transp=5, title="Up-Trend",display=display.none,editable=true,trackprice=false)
# HBMA2=plot(hbma,style=plot.style_line,linewidth=3,color=hbma>8.5?na:#9b000060,transp=5, title="Down-Trend",display=display.all,editable=true,trackprice=false)
# tracker=plot(hbma,style=plot.style_stepline,linewidth=1,color=hbma>8.5?#00862c:#bb0000,transp=50, title="Trend Tracker",display=display.all,editable=true,trackprice=true)
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# h1 = hline(8.5, "Bullish Confirmation Line", color=#002fb030, linestyle=hline.style_solid, editable = true)
# //h2 = hline(-0.4598, "Mask", color=#000000, linestyle=hline.style_solid, linewidth=4, editable = true)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //Crossing signals
# //
# topsignals = crossunder(bankma, banksignal) and rsi_Banker < 15 and rsi_HotMoney > 10 and banksignal>8 

# downtrendsignal = crossunder(hotma, hotsignal)
# uptrendsignal = crossover(hotma, hotsignal)
   
# bullishsignals = crossover(rsi_Banker, 8.5) and
#    rsi_HotMoney[0] > 17 and
#    bankma>banksignal and
#    hotma>hotsignal and
#    rsi_Banker[2]<6 and
#    rsi_Banker[5]<5 and
#    rsi_Banker[24]<12
   
# bearishsignals = crossunder(rsi_Banker, 8.5) and
#    rsi_HotMoney[0] < 18 and
#    bankma<banksignal and
#    hotma<hotsignal and
#    rsi_Banker<5
   
# entrysignals = crossover(rsi_HotMoney, 16) and
#    rsi_Banker>0 and
#    rsi_HotMoney[3]<15 and
#    rsi_HotMoney[10]<13 and
#    rsi_HotMoney[20]<13
   
# climax = crossover(hbma, 19)

# pump = crossover(rsi_Banker,hbma)

# bottom = crossunder(rsi_HotMoney,hbma)

# greed = crossover(lowampsignal,hbma) and lowampsignal>12 and rsi_Banker>8.5

# long = crossunder(lowampsignal,banksignal) and lowampsignal<10
# //
# ploff = 0
# plot(downtrendsignal  ? hbma[0] + ploff : na, title="Downtrend signal",style=plot.style_circles, color=#ff0000, linewidth=2,transp=0, display=display.all, editable=false)
# plot(uptrendsignal  ? hbma[0] + ploff : na, title="Uprend signal",style=plot.style_circles, color=#73ff00, linewidth=2,transp=0, display=display.all, editable=false)

# //
# plotshape(bullishsignals  ? 0[0] - ploff : na, title="Bullish signal 𓃓", text="𓃓", style=shape.labeldown, location=location.absolute, size=size.tiny, color=#81d9ff50, textcolor=#000000, offset=0, transp=0, display=display.all, editable=true)
# plotshape(topsignals  ? rsi_HotMoney[0] + ploff : na, title="Pull-back signal ⤼", text="⤼", style=shape.labelup, location=location.absolute, size=size.tiny, color=#9e004500, textcolor=#000000, offset=0, transp=0, display=display.all, editable=true)

# plotshape(bearishsignals  ? hbma[0] + ploff : na, title="Bearish signal 𓃾", text="𓃾", style=shape.labelup, location=location.absolute, size=size.tiny, color=#ff000050, textcolor=#ffffff, offset=0, transp=0, display=display.all, editable=true)
# plotshape(entrysignals  ? hbma[0] + ploff : na, title="Entry signal 𓄀", text="𓄀", style=shape.labeldown, location=location.absolute, size=size.tiny, color=#00862c50, textcolor=#000000, offset=0, transp=0, display=display.all, editable=true)

# plot(rsi_Banker,   "Retest Candles",    color=banksignal>bankma and rsi_Banker>0?#c1510060:na, linewidth=4, style=plot.style_histogram)
# plot(rsi_Banker, "Pump Candles", color=rsi_Banker>hbma?#00ff0a:na,transp=70, linewidth=4, style=plot.style_histogram)
# plot(rsi_Banker, "Down Candles", color=rsi_Banker<rsi_Banker[1] and rsi_Banker<rsi_Banker[2] and rsi_Banker[1]<rsi_Banker[2] and rsi_Banker<rsi_Banker[3] and rsi_Banker<rsi_Banker[4] and rsi_Banker[3]<rsi_Banker[4] and rsi_Banker[6]>8.5 and rsi_Banker<10?#000000:na,transp=40, linewidth=4, style=plot.style_histogram)
# plot(rsi_Banker, "Dump Candles", color=rsi_Banker<rsi_Banker[1]/1.75?#ff0000:na,transp=40, linewidth=4, style=plot.style_columns)

# plotshape(climax  ? hbma[0] + ploff : na, title="Oversold signal ᅐ", text="ᅐ", style=shape.labelup, location=location.absolute, size=size.tiny, color=#ff000050, textcolor=#000000, offset=0, transp=0, display=display.all, editable=true)
# plotshape(bottom  ? hbma[0] + ploff : na, title="Lower Low signal ⤷", text="⤷", style=shape.labeldown,location=location.absolute, size=size.tiny, color=#ffffff00, textcolor=#000000, offset=0, transp=0, display=display.all, editable=true)

# plotshape(greed  ? hbma[0] + ploff : na, title="Sell signal 💲", text="💲", style=shape.labelup,location=location.absolute, size=size.tiny, color=#ff000070, textcolor=#008055, offset=0, transp=0, display=display.all, editable=true)
# plotshape(long  ? lowampsignal[0] + ploff : na, title="Long signal ＄", text="＄", style=shape.labeldown,location=location.absolute, size=size.tiny, color=#00862c00, textcolor=#00862c, offset=0, transp=0, display=display.all, editable=true)




