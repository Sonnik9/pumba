import pandas as pd
# import time
# import random
import ccxt
import pandas as pd
from TG.tg_apii import TG_APIII
import asyncio
import time

method = 'GET'

class GETT_API_CCXT(TG_APIII):
    def __init__(self):
        super().__init__()
        # print(self.api_key)
        # print(self.api_secret)
        self.exchange = ccxt.binance({
            'apiKey': self.api_key,
            'secret': self.api_secret,
            'enableRateLimit': True, 
        })


    async def get_ccxtBinance_klines(self, symbol, timeframe, limit):
        self.test_flag = False
        self.init_api_key()
        self.init_urls()

        retry_number = 3
        decimal = 1.1        
        for i in range(retry_number):
            try:
                klines = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
                data = pd.DataFrame(klines, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
                data['Time'] = pd.to_datetime(data['Time'], unit='ms')
                data.set_index('Time', inplace=True)
                data = data.astype(float)
                return data
            except Exception as e:
                print(f"Error fetching klines: {e}")
                # time.sleep(1)
                await asyncio.sleep(1.1 + i*decimal)     

        return pd.DataFrame()
    
    def get_ccxtBinance_klines_usual(self, symbol, timeframe, limit):
        self.test_flag = False
        self.init_api_key()
        self.init_urls()
        
        retry_number = 3
        decimal = 1.1        
        for i in range(retry_number):
            try:
                klines = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
                data = pd.DataFrame(klines, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
                data['Time'] = pd.to_datetime(data['Time'], unit='ms')
                data.set_index('Time', inplace=True)
                data = data.astype(float)
                return data
            except Exception as e:
                print(f"Error fetching klines: {e}")
                time.sleep(1.1 + i*decimal)                

        return pd.DataFrame()

class GETT_API(GETT_API_CCXT):

    def __init__(self) -> None:
        super().__init__()   
        
    def get_all_tickers(self):
        all_tickers = None
        url = self.URL_PATTERN_DICT['all_tikers_url']        
        all_tickers = self.HTTP_request(url, method=method, headers=self.header)

        return all_tickers
    
    def get_excangeInfo(self, symbol):
       

        exchangeInfo = None
        if symbol:            
            url = f"{self.URL_PATTERN_DICT['exchangeInfo_url']}?symbol={symbol}"
        else:
            url = self.URL_PATTERN_DICT['exchangeInfo_url']        
        exchangeInfo = self.HTTP_request(url, method=method, headers=self.header)

        return exchangeInfo
    
    def get_balance(self):
       
        current_balance = None 
        url = self.URL_PATTERN_DICT['balance_url']
        # print(url)
        params = {}
        
        if not self.test_flag:
            params['recvWindow'] = 5000
            params = self.get_signature(params)
            current_balance = self.HTTP_request(url, method=method, headers=self.header, params=params)
            
            if self.market == 'spot':                
                current_balance = dict(current_balance)                
                current_balanceE = current_balance['balances']
                current_balance = [(x['free'], x['locked']) for x in current_balanceE if x['asset'] == 'USDT'][0]          
            if self.market == 'futures':                
                current_balanceE = list(current_balance)
                current_balance = [(x['balance'], x['crossUnPnl']) for x in current_balanceE if x['asset'] == 'USDT'][0]
        else:
            params = self.get_signature(params)
            current_balance = self.HTTP_request(url, method=method, headers=self.header, params=params)
            current_balance = float([x['balance'] for x in current_balance if x['asset'] == 'USDT'][0])  
            # print(current_balance)
            
        return current_balance
    

    
    def get_DeFacto_price(self, symbol):
        

        positions = None        
        url = self.URL_PATTERN_DICT['positions_url']
        params = {}
        params = self.get_signature(params)
        positions = self.HTTP_request(url, method=method, headers=self.header, params=params)
        
        positions = float([x for x in positions if x['symbol'] == symbol][0]["entryPrice"])

        return positions
    

# # ////////////////////////////////////////////////////////////////////////////////////

#     def get_all_orders(self):
#         all_orders = None        
#         params = {}               
#         url = self.URL_PATTERN_DICT['get_all_orders_url']
#         params = self.get_signature(params)
#         all_orders = self.HTTP_request(url, method=method, headers=self.header, params=params)

#         return all_orders
    
    def get_open_positions(self):
       
        all_positions = None        
        params = {}          
        symbol = None     
        url = self.URL_PATTERN_DICT['positions_url']
        if symbol:
            params["symbol"] = symbol
        params = self.get_signature(params)
        all_positions = self.HTTP_request(url, method=method, headers=self.header, params=params)
        all_positions = [x for x in all_positions if float(x["positionAmt"]) != 0]

        return all_positions 
# # //////////////////////////////////////////////////////////////////////////////////

# # get_apii = GETT_API()
# # symbol = 'BNBUSDT'
# # klines = get_apii.get_klines(symbol, 100)
# # print(klines)
# # price = get_apii.get_current_price(symbol)
# # print(price)#

# # # python -m API_BINANCE.get_api
    

# symbol = 'BNBUSDT'  # Replace with the symbol you're interested in
# timeframe = '1m'  # You can change the timeframe (e.g., '5m', '1h', '1d')

# binance_fetcher = BinanceDataFetcher()
# klines_data = binance_fetcher.get_ccxtBinance_klines(symbol, timeframe, limit=11)

# # # Display the fetched data
# print(klines_data)

