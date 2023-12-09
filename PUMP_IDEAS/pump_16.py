# Fibodex Trap indicator

# this indicator designed by the Fibodex team
# you will receive dump and bump singles buy using this indicator
# also, you will receive buy and sell signals
# indeed by using our indicator you won't need many technical analyses
# The accuracy of the indicator with the correct settings is estimated to be more than 70%
# also, we are trying to improve it to make it more accurate
# notice that this indicator should be used as a secondary tool
# By using this indicator, you also accept the risk of using it.

# //@version=4
# ////////////////////////////////////////////////////////////////////////////////////////////
# //                            *** Fibodex indicator ***                                ***//
# // ***                                                                                 ***//
# // ***                                                                                 ***//
# //          *** Thanks to Alireza Yarian for invaluable scripting ideas :-)            ***//
# ////////////////////////////////////////////////////////////////////////////////////////////
# //
# study(title="Fibodex Signal", overlay=true)
# //
# //General inputs
# showSig = input(true, title="خرید و فروش نمایش داده شود؟")
# showpump = input(true, title= "اعلان پامپ نمایش داده شود؟ ")
# nit = input( title= "مبنای پامپ",type=input.float,defval=3, minval=1)
# Rsip = input( title= "حد بالای rsi",type=input.integer,defval=65, minval=1)
# Rsid = input( title= "حد پایین rsi",type=input.integer,defval=30, minval=1)
# Mv=input(title="دوره محاسبه در پامپ",type=input.integer,defval=7 ,minval=1) 
# len = input(14, title="دوره میانگین قیمت")
# vlength=input(10, title="دوره حجم معاملات")
# shc = input(false, title="خط میانگین قیمت نمایش داده شود؟")
# cc = input(false, title="خط میانگین قیمت به صورت نزولی و صعودی نمایش داده شود؟ ")
# nfilter = input(false, title="سیگنال دهی کمتر؟")
# nflen = input(14, title="فیلتر دوره ای")
# smoothK = input(5, title="فیلتر صافی K")
# smoothD = input(3, title="فیلتر صافی D")
# drive = input(1, minval=1, maxval=3, title="one /n/n :  1= MA AND VOL, 2 = MA, 3 =VOL")
# rsivalue = rsi(close, 14)
# // cal 
# rsiPump = rsivalue >= Rsip
# rsiDump = rsivalue <= Rsid

# volget=sma(volume,Mv) * nit
# lastVol=volume
# pump = lastVol > volget
# t_id = tickerid(syminfo.prefix, syminfo.ticker)
# realC = security(t_id, timeframe.period, close)
# real4 = security(t_id, timeframe.period, ohlc4)
# buyprice = 0.0
# buyprice := nz(buyprice[1])
# sellprice = 0.0
# sellprice := nz(sellprice[1])
# last_tran = false
# last_tran := nz(last_tran[1])
# ema1 = ema(realC, len)
# ema2 = ema(ema1, len)
# ema3 = ema(ema2, len)
# tema = 3 * (ema1 - ema2) + ema3
# avg = 3 * (ema1 - ema2) + ema3
# out = avg
# out1 = security(t_id, timeframe.period, out)
# ma_up = out1 >= out1[1]
# ma_down = out1 < out1[1]
# col = cc ? ma_up ? color.lime : ma_down ? color.red : color.lime : color.aqua
# x=(2*close-high-low)/(high-low)
# tva=sum(volume*x,vlength)
# tv=sum(volume,vlength)
# va=100*tva/tv
# VOLUP = va >= 0 ? true : false
# VOLDOWN = va < 0 ? true : false
# t_UP = drive == 1 ? ma_up and VOLUP : drive == 2 ? ma_up : drive == 3 ? VOLUP : na
# t_DOWN = drive == 1 ? ma_down and VOLDOWN : 
#    drive == 2 ? ma_down : drive == 3 ? VOLDOWN : na
# t_NON = t_UP == t_DOWN
# res = timeframe.period
# k = sma(stoch(close, high, low, nflen), smoothK)
# d = sma(k, smoothD)
# outK = security(syminfo.tickerid, res, k)
# outD = security(syminfo.tickerid, res, d)
# Fbuy = (outK > outD) or not nfilter
# Fsell = (outD > outK) or not nfilter
# plot(out1, title="Improbability curve", style=plot.style_line, linewidth=2, color=col, transp=iff(shc, 0, 100))
# long = t_UP and not last_tran and not t_NON and Fbuy
# short = t_DOWN and last_tran and not t_NON and Fsell
# if long
#     buyprice := realC  //Set buyprice
#     last_tran := true  //Set long condition
#     last_tran
# if short
#     sellprice := realC  //Set sellprice
#     last_tran := false  //Set short condition
#     last_tran
# goodlong = long and buyprice <= sellprice
# goodshort = short and sellprice > buyprice
# txtlight_b = color.lime
# txtlight_s = iff(goodshort, color.lime, color.red)


# alertcondition(long, title='سیگنال خرید', message='موقعیت مناسب خرید')
# alertcondition(short, title='سیگنال فروش', message='موقعیت فروش')
# alertcondition(pump and showpump and rsiPump, title='هشدار پامپ', message='پامپی در جریان است')
# alertcondition(pump and showpump and rsiDump, title='هشدار دامپ', message='دامپی در جریان است')

# plotshape(pump and showpump and rsiPump, title = "سیگنال پامپ", location=location.belowbar, color=color.green, transp=0, style=shape.labelup, size=size.small, textcolor=color.white, text = "پامپ")
# plotshape(pump and showpump and rsiDump, title = "سیگنال دامپ", location=location.belowbar, color=color.red, transp=0, style=shape.labelup, size=size.small, textcolor=color.white, text = "دامپ")
# plotshape(long and showSig, title="سیگنال خرید", color=color.green, transp=0, style=shape.arrowup, text="خرید", textcolor=color.green, location=location.belowbar)
# plotshape(short and showSig, title="سیگنال فروش", color=color.red, transp=0, style=shape.arrowdown, text="فروش", textcolor=color.red, location=location.abovebar)




