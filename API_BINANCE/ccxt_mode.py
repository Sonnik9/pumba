import ccxt
import pandas as pd
from config import CONFIG

method = 'GET'

class GETT_API_CCXT(CONFIG):
    def __init__(self):
        super().__init__()
        # print(self.api_key)
        # print(self.api_secret)
        self.exchange = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
            'enableRateLimit': True, 
        })

    def get_all_tickers(self):
        all_tickers = None
        url = self.URL_PATTERN_DICT['all_tikers_url']        
        all_tickers = self.HTTP_request(url, method=method, headers=self.header)

        return all_tickers

    def get_ccxtBinance_klines(self, symbol, timeframe, limit):
        try:
            klines = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            data = pd.DataFrame(klines, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
            data['Time'] = pd.to_datetime(data['Time'], unit='ms')
            data.set_index('Time', inplace=True)
            return data
        except Exception as e:
            print(f"Error fetching klines: {e}")
            return pd.DataFrame()


# symbol = 'BNBUSDT'  # Replace with the symbol you're interested in
# timeframe = '1m'  # You can change the timeframe (e.g., '5m', '1h', '1d')

# binance_fetcher = BinanceDataFetcher()
# klines_data = binance_fetcher.get_ccxtBinance_klines(symbol, timeframe, limit=11)

# # # Display the fetched data
# print(klines_data)
