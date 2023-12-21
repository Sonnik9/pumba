# # ///////////////////////////////////////////////////////////////////////////////////////        
#     async def assets_filters_2(self):
#         top_pairs = []
#         all_tickers = []
        
#         exclusion_contains_list = ['UP', 'DOWN', 'RUB', 'EUR']
#         all_tickers = self.get_all_tickers()
#         # print(all_tickers)

#         if all_tickers:
#             usdt_filtered = [ticker for ticker in all_tickers if
#                             ticker['symbol'].upper().endswith('USDT') and
#                             not any(exclusion in ticker['symbol'].upper() for exclusion in exclusion_contains_list) and
#                             (float(ticker['lastPrice']) >= self.MIN_FILTER_PRICE) and (float(ticker['lastPrice']) <= self.MAX_FILTER_PRICE)]
            
#             # print(usdt_filtered[0])
                       
#             filtered_volume_data = [x for x in usdt_filtered if float(x['quoteVolume']) >= self.MIN_VOLUM_USDT]
#             sorted_by_volume_data = sorted(filtered_volume_data, key=lambda x: float(x['quoteVolume']), reverse=True)
#             top_pairs = [x["symbol"] for x in sorted_by_volume_data if x not in self.problem_pairs]

#         return top_pairs
    
# # ///////////////////////////////////////////////////////////////////////////////////