from TEMPLATES.open_market_order_temp import TEMPP
import asyncio
       
class TG_HANDLERR(TEMPP):
    def __init__(self):
        super().__init__()

    # def update_main_paramss(self, new_market, new_test_flag):
    #     self.market = new_market
    #     self.test_flag = new_test_flag
    #     self.init_itits()

    def open_order_redirect_funcc(self, message):
        item = {}  
        symbol = item["symbol"] = message.text.split(' ')[0].strip().upper() + 'USDT'       
        item["defender"] = int(message.text.split(' ')[1].strip())
        item['in_position'] = False
        item['qnt'] = None 
        item["recalc_depo"] = None 
        item["price_precision"] = None 
        item["tick_size"] = None
        item["current_price"] = self.get_current_price(symbol)
        print(f'item["current_price"]: {item["current_price"]}')

        timeframe = '1m'
        limit = 15
        m1_15_data = self.get_ccxtBinance_klines_usual(symbol, timeframe, limit)            
        m1_15_data['TR'] = abs(m1_15_data['High'] - m1_15_data['Low'])
        m1_15_data['ATR'] = m1_15_data['TR'].rolling(window=14).mean()
        item['atr'] = m1_15_data['ATR'].iloc[-1]

        item = self.make_market_order_temp_func(item)

        if item['in_position']:
            response_message = 'The order was created successfuly!'
            message.text = self.connector_func(message, response_message)
            item = self.tp_make_orders(item)
            if item["done_level"] == 2:
                response_message = 'The takeProfit order was created successfuly!'
                message.text = self.connector_func(message, response_message)    
            else:
                print('Some problems with placing takeProfit order(') 
        else:
            print('Some problems with open order(')
        return None

    def run(self):          

        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.pump_candidate_busy_list = [] 
            self.signal_number_acumm_list = [] 
            self.init_itits()
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            self.pump_candidate_busy_list = [] 
            self.signal_number_acumm_list = [] 
            self.init_itits()
            self.bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            
            response_message = "Please select a settings options..." 
            message.text = self.connector_func(message, response_message) 
            self.settings_tg_flag = True

        @self.bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(message, response_message)   

        @self.bot.message_handler(func=lambda message: message.text == "STOP")
        def stop(message):
            self.stop_bot_flag = True
        # //////////////////////////////////////////////////////////////////////  

        @self.bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):
      
            response_message = "Please wait. It's gonna take some time...."
            message.text = self.connector_func(message, response_message)
            self.launch_finish_text = asyncio.run(self.launch(message))
            message.text = self.connector_func(message, self.launch_finish_text)

        @self.bot.message_handler(func=lambda message: message.text == "OPEN_ORDER")
        def open_order(message):
            # self.init_itits()            
            response_message = "Please enter a coin and side with a space (e.g.: btc 1)\n1 -- Long;\n-1 -- Short"
            message.text = self.connector_func(message, response_message)
            self.order_triger = True
            self.open_order_redirect_flag = True           
            
        @self.bot.message_handler(func=lambda message: self.open_order_redirect_flag)
        def open_order_redirect(message):
            self.open_order_redirect_funcc(message)
            self.init_api_ccxt()
            self.order_triger = False

        @self.bot.message_handler(func=lambda message: message.text == "CLOSE_POSITION")
        def open_order(message):
            # self.init_itits()            
            response_message = "Please enter a coin(e.g.: btc)"
            message.text = self.connector_func(message, response_message)
            self.order_triger = True
            self.close_position_redirect_flag = True   

        @self.bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(message, response_message)                 

        self.bot.polling()

def main_tg_func():   
    my_bot = TG_HANDLERR()
    my_bot.run()