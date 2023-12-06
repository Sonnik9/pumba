import requests



import requests

url = 'https://open-api.coinglass.com/public/v2/open_interest_history'
headers = {
    'accept': 'application/json',
    'coinglassSecret': '1557b4ccbc624592b6b5c2d6a4d660ef'
}

params = {
    'symbol': 'BTC',
    'time_type': 'h1',  # m1 m5 m15 h1 h4 h12 all
    'currency': 'USDT'
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    # Задаем ключ явно, чтобы получить открытый интерес для биржи Binance
    exchange_key = 'Binance'
    
    binance_open_interest = data['data']['dataMap'][exchange_key]
    
    for timestamp, price, open_interest in zip(data['data']['dateList'], data['data']['priceList'], binance_open_interest):
        print(f'Timestamp: {timestamp}, Price: {price}, {exchange_key} Open Interest: {open_interest}')
else:
    print(f"Ошибка при запросе данных: {response.status_code}, {response.text}")


# // This source code is subject to the terms of the Mozilla Public License 2.0 at https://mozilla.org/MPL/2.0/
# // © MyFire_Yiannis 2023 
# //
# //@version=5
# indicator(title = "Open Interest with Heikin Ashi", shorttitle = "OIHA v1.0", format = format.volume, overlay=false)

# bool overwriteSymbolInput = input.bool(false, "Override symbol", inline = "Override symbol")
# string tickerInput = input.symbol("", "", inline = "Override symbol")
# string symbolOnly = syminfo.ticker(tickerInput)
# string userSymbol = overwriteSymbolInput ? symbolOnly : syminfo.prefix + ":" + syminfo.ticker
# string openInterestTicker = str.format("{0}_OI", userSymbol)
# string timeframe = syminfo.type == "futures" and timeframe.isintraday ? "1D" : timeframe.period
# [oiOpen, oiHigh, oiLow, oiClose, oiColorCond] = request.security(openInterestTicker, timeframe, [open, high, low, close, close > close[1]], ignore_invalid_symbol = true)
# oiOpen := oiOpen ? oiOpen : na
# oiHigh := oiHigh ? oiHigh : na
# oiLow := oiLow ? oiLow : na

# if barstate.islastconfirmedhistory and na(oiClose)
#     runtime.error(str.format("No Open Interest data found for the `{0}` symbol.", userSymbol))

# hasOHLC = ta.cum(oiOpen)
# color openInterestColor = oiColorCond ? color.teal : color.red
# // plot(hasOHLC ? na : oiClose, "Futures Open Interest", openInterestColor, style = plot.style_stepline, linewidth = 4)
# // plotcandle(oiOpen, oiHigh, oiLow, hasOHLC ? oiClose : na, "Crypto Open Interest", color = openInterestColor, wickcolor = openInterestColor, bordercolor = openInterestColor)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //
# // HA start
# //
# bgHA = input.bool(true, "Background color", inline = "Background color")
# heikenashi = ticker.heikinashi(openInterestTicker)

# o = request.security(heikenashi, timeframe.period, open)
# h = request.security(heikenashi, timeframe.period, high)
# l = request.security(heikenashi, timeframe.period, low)
# c = request.security(heikenashi, timeframe.period, close)
# clr = c > o ? color.lime : color.red

# plotcandle(o, h, l, c, 'Heiken Ashi', clr, color.black)
# bgcolor(bgHA ? color.new(clr, 90) : na)
# // HA stop
# //
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# python open_interest.py


