# from API_BINANCE.get_api import GETT_API
from API_BINANCE.ccxt_mode import GETT_API_CCXT

class UTILS_APII(GETT_API_CCXT):

    def __init__(self) -> None:
        super().__init__()

# ///////////////////////////////////////////////////////////////////////////////////////        
    async def assets_filters_2(self):
        top_pairs = []
        all_tickers = []
        
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        all_tickers = self.get_all_tickers()
        # print(all_tickers)

        if all_tickers:
            usdt_filtered = [ticker for ticker in all_tickers if
                            ticker['symbol'].upper().endswith('USDT') and
                            not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                            (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]
            
            # print(usdt_filtered[0])
                       
            filtered_volume_data = [x for x in usdt_filtered if float(x['quoteVolume']) >= self.MIN_VOLUM_USDT]
            sorted_by_volume_data = sorted(filtered_volume_data, key=lambda x: float(x['quoteVolume']), reverse=True)
            top_pairs = [x["symbol"] for x in sorted_by_volume_data if x not in self.problem_pairs]

        return top_pairs
    
# ///////////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////////////        
    async def assets_filters_1(self):
        top_pairs = []
        all_tickers = []
        
        exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
        all_tickers = self.get_all_tickers()
        # print(all_tickers)

        if all_tickers:
            usdt_filtered = [ticker for ticker in all_tickers if
                            ticker['symbol'].upper().endswith('USDT') and
                            not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
                            (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]
            
            # print(usdt_filtered[0])
            sorted_by_volume_data = sorted(usdt_filtered, key=lambda x: float(x['quoteVolume']), reverse=True)
            # print(sorted_by_volume_data[0]['quoteVolume'])
            # print(sorted_by_volume_data[1]['quoteVolume'])
            # print(sorted_by_volume_data[2]['quoteVolume'])
            # print(sorted_by_volume_data[3]['quoteVolume'])
            # print(sorted_by_volume_data[4]['quoteVolume'])
            # print(sorted_by_volume_data[5]['quoteVolume'])
            # print(sorted_by_volume_data[6]['quoteVolume'])
            # print(sorted_by_volume_data[7]['quoteVolume'])
            # print(sorted_by_volume_data[8]['quoteVolume'])
            # print(sorted_by_volume_data[9]['quoteVolume'])
            sorted_by_volume_data = sorted_by_volume_data[:self.SLICE_VOLUME_PAIRS]
            

            top_pairs = [x['symbol'] for x in sorted_by_volume_data if x['symbol'] not in self.problem_pairs]

        return top_pairs
    
# ///////////////////////////////////////////////////////////////////////////////////


# self.MIN_VOLUM_DOLLARS

# utils_apii = UTILS_API() 

# # python -m API.orders_utils