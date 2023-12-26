# Ставка начальной маржи = (1 / 50) = 2%

# Ставка поддерживающей маржи = 0,5% 

# Цена ликвидации = 20 000 USDT × (1 - 0,02 + 0,005) = 19 700 USDT
# Цена ликвидации = 20 000 USDT × (1 + 0,02 - 0,005) = 20 300 USDT
# direction_multiplier = -1 
# a = f"1/((1 - (((19700/20000)) - 0.005)))"
# b = f"1/(((20300/20000) + 0.005) - 1)"
# c = eval(a)
# d = eval(b)
# print(c)
# print(d)


# from API_BINANCE.utils_api import UTILS_APII

# # def calculate_liquidation_price(entry_price, leverage=50, long=True, risk_limit=0.004):
# #     margin_rate = 1 / leverage
# #     direction_multiplier = 1 if long else -1
# #     liquidation_price = entry_price * (1 - (direction_multiplier * margin_rate) + (direction_multiplier * risk_limit))
# #     return liquidation_price

# def calculate_leverage(entry_price, defender, atr, risk_limit=0.004):
#     liquidation_price = entry_price - (defender * atr * self.atr_multipliter)
#     print(f"liquidation_price: {liquidation_price}")
#     if defender == 1:
#         leverage = 1 / (1 - ((liquidation_price/entry_price) - risk_limit))
#     else:
#         leverage = 1 / ((liquidation_price/entry_price) + risk_limit - 1)

#     return abs(int(leverage))

# # Пример использования:
# get_apii = UTILS_APII()
# symbol = 'SOLUSDT'
# timeframe, limit = '15m', 100
# klines = get_apii.get_ccxtBinance_klines_usual(symbol, timeframe, limit)
# # # print(klines)
# entry_price = klines["Close"].iloc[-1]
# print(f"entry_price: {entry_price}") 
# # print(type(entry_price)) 
# klines['TR'] = abs(klines['High'] - klines['Low'])
# klines['ATR'] = klines['TR'].rolling(window=14).mean()   
# atr = klines["ATR"].iloc[-1]   
# print(f"atr: {atr}")
# defender = 1
# leverage = calculate_leverage(entry_price, defender, atr)


# print(f"Leverage: {leverage}")


                        # asyncio.create_task(self.websocket_handler(self.coins_in_squeezeOn))  
                        # loop = asyncio.get_event_loop()
                        # loop.create_task(self.websocket_handler(self.coins_in_squeezeOn))
