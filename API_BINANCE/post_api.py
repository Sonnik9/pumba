from API_BINANCE.get_api import GETT_API
method = 'POST'

class POSTT_API(GETT_API):

    def __init__(self) -> None:
        
        super().__init__()    
        # self.init_post_api()

    def init_post_api(self):
        self.test_flag = self.open_order_testnet_flag
        self.init_api_key()
        self.init_urls()
        print(self.api_key)
        print(self.api_secret) 

    def set_leverage(self, symbol):
        self.init_post_api()

        params = {}
        url = self.URL_PATTERN_DICT["set_leverage_url"]
        params['symbol'] = symbol
        params['leverage'] = self.LEVERAGE
        params = self.get_signature(params)
        response = self.HTTP_request(url, method=method, headers=self.header, params=params)
        
        return response 
    
    def make_order(self, item, is_closing, target_price, market_type):
        self.init_post_api()

        response = None
        success_flag = False
        url = self.URL_PATTERN_DICT['create_order_url']
        params = {}        
        params["symbol"] = item["symbol"]        
        params["type"] = market_type
        params["quantity"] = item['qnt']
      
        if market_type == 'LIMIT':            
            params["price"] = target_price
            params["timeinForce"] = 'GTC' 
            
        if market_type == 'STOP_MARKET' or market_type == 'TAKE_PROFIT_MARKET':
            params['stopPrice'] = target_price
            params['closePosition'] = True 
  
        if item["defender"] == 1*is_closing:
            side = 'BUY'
        elif item["defender"] == -1*is_closing:
            side = "SELL" 
        params["side"] = side 

        params = self.get_signature(params)
        response = self.HTTP_request(url, method=method, headers=self.header, params=params)
        if response and 'status' in response and response['status'] == 'NEW':
            success_flag = True

        return response, success_flag
    
# post_apii = POSTT_API()

