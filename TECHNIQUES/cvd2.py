import ccxt
import pandas as pd
import numpy as np
import plotly.express as px

def fetch_trades_and_orderbook(symbol, limit):
    exchange = ccxt.binance()
    # exchange = ccxt.binance({
    #     'apiKey': "vPlx4lmDIcgMT6QcUhvW0yoNHgXawtKQrqmwOgCEneoNtRbe9JmT1qVdo1WUZjAr",
    #     'secret': "lll0IA6Gyqf2vn2qijISrzjf5ru99Z6hbnFE20SJxP1kIKr5czyHxPJeYnlHSzwE",
    # })
    # exchange_id = 'binance'
    # exchange_class = getattr(ccxt, exchange_id)
    # exchange = exchange_class({
    #     'apiKey': "vPlx4lmDIcgMT6QcUhvW0yoNHgXawtKQrqmwOgCEneoNtRbe9JmT1qVdo1WUZjAr",
    #     'secret': "lll0IA6Gyqf2vn2qijISrzjf5ru99Z6hbnFE20SJxP1kIKr5czyHxPJeYnlHSzwE",
    # })

# Получите свечи и данные о сделках

    trades = exchange.fetch_trades(symbol, params = {"paginate": True, "paginationCalls": 1})
    orderbook = exchange.fetch_order_book(symbol)
    
    trades_df = pd.DataFrame(trades)
    orderbook_df = pd.DataFrame(orderbook['bids'] + orderbook['asks'], columns=['price', 'volume'])

    return trades_df, orderbook_df


def calculate_cumulative_volume_delta_with_price(trades_df, orderbook_df):
    trades_df['price'] = trades_df['price'].astype(float)
    
    # Determine the side (buy or sell) based on price changes
    trades_df['side'] = np.where(trades_df['price'].diff() > 0, 1, -1)
    
    # Calculate the weighted volume delta
    trades_df['weighted_volume_delta'] = trades_df['amount'] * trades_df['price'] * trades_df['side']

    # Calculate the cumulative weighted volume for order book
    orderbook_df['cumulative_weighted_volume'] = orderbook_df['volume'].cumsum()
    
    # Calculate the cumulative weighted volume for trades
    trades_df['cumulative_weighted_volume'] = trades_df['weighted_volume_delta'].cumsum()

    # Calculate the Cumulative Volume Delta (CVD)
    trades_df['cvd'] = trades_df['cumulative_weighted_volume'] / orderbook_df['cumulative_weighted_volume']

    return trades_df


symbol = 'BTC/USDT'
limit = 99

# Получение данных
trades_df, orderbook_df = fetch_trades_and_orderbook(symbol, limit)
# print(trades_df)

# Расчет cvd
result_df = calculate_cumulative_volume_delta_with_price(trades_df, orderbook_df)
print(result_df)

# Использование начального значения cvd из ваших данных
# initial_cvd_value = result_df['cvd'].iloc[0]
# result_df['cvd'] = result_df['cvd'] + initial_cvd_value

# # Построение графика
# fig = px.line(result_df, x=result_df.index, y='cvd', labels={'cvd': 'CVD'},
#               title='Cumulative Volume Delta (CVD) Over Time')
# fig.update_xaxes(title_text='Time')
# fig.update_yaxes(title_text='CVD')
# fig.show()
