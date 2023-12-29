# import time
# import random
from datetime import datetime
import pandas as pd
import asyncio
import time
from connectorss import CONNECTOR_TG

import logging, os, inspect

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)


method = 'GET'

class GETT_API_CCXT(CONNECTOR_TG):
    def __init__(self):   
        super().__init__()     

    async def get_ccxtBinance_klines(self, symbol, timeframe, limit):

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
       
        retry_number = 3
        decimal = 1.1        
        for i in range(retry_number):
            try:
                klines = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
                # print(klines)
                data = pd.DataFrame(klines, columns=['Time', 'Open', 'High', 'Low', 'Close', 'Volume'])
                data['Time'] = pd.to_datetime(data['Time'], unit='ms')
                data.set_index('Time', inplace=True)
                data = data.astype(float)
                return data
            except Exception as e:
                print(f"Error fetching klines: {e}")
                time.sleep(1.1 + i*decimal)                

        return pd.DataFrame()

    def transformed_qnt(self, symbol, amount):
        
        self.exchange.load_markets()
        formatted_amount = self.exchange.amount_to_precision(symbol, amount)
        return formatted_amount

    def transformed_price(self, symbol, price):
        
        self.exchange.load_markets()
        formatted_price = self.exchange.price_to_precision(symbol, price)
        return formatted_price

class GETT_API(GETT_API_CCXT):

    def __init__(self) -> None:
        super().__init__()   
        
    async def get_all_tickers(self):

        all_tickers = None
        url = self.URL_PATTERN_DICT['all_tikers_url']        
        all_tickers = await self.HTTP_request(url, method=method, headers=self.header)

        return all_tickers
    
    async def get_excangeInfo(self, symbol):       

        exchangeInfo = None
        if symbol:            
            url = f"{self.URL_PATTERN_DICT['exchangeInfo_url']}?symbol={symbol}"
        else:
            url = self.URL_PATTERN_DICT['exchangeInfo_url']        
        exchangeInfo = await self.HTTP_request(url, method=method, headers=self.header)

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
    
# ///////////////////////////////////////////////////////////////////
    async def get_current_price(self, symbol):
        method = 'GET'
        current_price = None
        url = self.URL_PATTERN_DICT['current_ptice_url']
        params = {'symbol': symbol}
        print(f"symbol: {symbol}")
        try:
            current_price = await self.HTTP_request(url, method=method, params=params) 
            # print(current_price)  
            # current_price = float([x['price'] for x in current_price if x['symbol'] == symbol])
            current_price = float(current_price["price"])
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return current_price  

# ///////////////////////////////////////////////////////////////////////////////////////   
        
    async def get_DeFacto_price(self, symbol):       

        positions = None        
        url = self.URL_PATTERN_DICT['positions_url']
        params = {}
        params = self.get_signature(params)
        positions = await self.HTTP_request(url, method=method, headers=self.header, params=params)
        
        positions = float([x for x in positions if x['symbol'] == symbol][0]["entryPrice"])

        return positions
    

# # ////////////////////////////////////////////////////////////////////////////////////

    def get_all_orders(self):
        all_orders = None        
        params = {}               
        url = self.URL_PATTERN_DICT['get_all_orders_url']
        params = self.get_signature(params)
        all_orders = self.HTTP_request(url, method=method, headers=self.header, params=params)

        return all_orders
    
    async def get_open_positions(self):
       
        all_positions = None        
        params = {}          
        symbol = None     
        url = self.URL_PATTERN_DICT['positions_url']
        if symbol:
            params["symbol"] = symbol
        params = self.get_signature(params)
        all_positions = await self.HTTP_request(url, method=method, headers=self.header, params=params)
        all_positions = [x for x in all_positions if float(x["positionAmt"]) != 0]
        all_positions = await self.format_positions_data(all_positions)

        return all_positions 
    

# # //////////////////////////////////////////////////////////////////////////////////

# get_apii = GETT_API()
# symbol = 'BNBUSDT'
# symbol = 'SOLUSDT'
# # # klines = get_apii.get_klines(symbol, 100)
# # # print(klines)
# price = asyncio.run(get_apii.get_current_price(symbol))
# open_pos = asyncio.run(get_apii.get_open_positions())
# print(open_pos)
# print(price)


# # # python -m API_BINANCE.get_api
    

# symbol = 'BNBUSDT'  # Replace with the symbol you're interested in
# timeframe = '1m'  # You can change the timeframe (e.g., '5m', '1h', '1d')

# binance_fetcher = BinanceDataFetcher()
# klines_data = binance_fetcher.get_ccxtBinance_klines(symbol, timeframe, limit=11)

# # # Display the fetched data
# print(klines_data)


# GETT_API_CCXTxfjk = GETT_API_CCXT()
# symbol = 'BTC/USDT'
# klines = GETT_API_CCXTxfjk.get_ccxtBinance_klines_usual(symbol, '1m', 100)
# amount = 1.234567887  # amount in base currency BTC
# price = 42500.321  # price in quote currency USDT
# formatted_amount = GETT_API_CCXTxfjk.transformed_qnt(symbol, amount)
# formatted_price = GETT_API_CCXTxfjk.transformed_price(symbol, price)
# print(formatted_amount, formatted_price)

