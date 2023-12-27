from API_BINANCE.utils_api import UTILS_APII
from TECHNIQUES.techniques_py import TECHNIQUESS
from API_WEBSOCKET.websocket_handler import LIVE_MONITORING 
from datetime import datetime
import asyncio
import time

money_emoji = "💰"
rocket_emoji = "🚀"
lightning_emoji =  "⚡"
clock_emoji = "⌚"
film_emoji = "📼"
percent_emoji = "📶"
repeat_emoji = "🔁"
upper_trigon_emoji = "🔼"
lower_trigon_emoji = "🔽"
confirm_emoji = "✅"
link_emoji = "🔗"

class TG_ASSISTENT(UTILS_APII, TECHNIQUESS, LIVE_MONITORING):

    def __init__(self):
        super().__init__()

    # def update_main_paramss(self, new_market, new_test_flag):
    #     self.market = new_market
    #     self.test_flag = new_test_flag
    #     self.init_itits()

    async def date_of_the_month(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%d')
        return int(formatted_time)
    
    async def signal_counter_assistent(self, pump_candidate_list, signal_number_acumm_list, date_of_the_month_start):        
        just_candidate_symbol_list = [x[0] for x in pump_candidate_list]
        signal_number_acumm_list += just_candidate_symbol_list
        print("Кандидаты в ПАМП/ДАМП:", just_candidate_symbol_list)
        date_of_the_month_current = await self.date_of_the_month()
        if date_of_the_month_current != date_of_the_month_start:
            signal_number_acumm_list = []
            date_of_the_month_start = date_of_the_month_current
            self.pump_candidate_busy_list = []

        return signal_number_acumm_list, date_of_the_month_start
    
    def connector_func(self, message, response_message):
        retry_number = 3
        decimal = 1.1       
        for i in range(retry_number):
            try:
                self.bot.send_message(message.chat.id, response_message)                
                return message.text
            except:
                time.sleep(1.1 + i*decimal)        
                   
        return None

    async def squeeze_unMomentum_addition(self):
        self.coins_in_squeezeOn = []
        top_coins = await self.assets_filters_1()
        print(f"len(top_coins): {len(top_coins)}")
        # print(top_coins[0:10])                       
        for symbol in top_coins:
            if self.stop_bot_flag:
                return self.coins_in_squeezeOn, True
            m15_data = None    
            precession_upgraded_data = {}            
            timeframe = '15m'
            limit = 100
            try:
                m15_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                m15_data = await self.squeeze_unMomentum(m15_data)
                if m15_data['squeeze_on'].iloc[-1]:   
                    precession_upgraded_data = await self.websocket_precession(symbol)                 
                    self.coins_in_squeezeOn.append(precession_upgraded_data)
            except:
                continue 
        self.coins_in_squeezeOn = [x for x in self.coins_in_squeezeOn if x != {}]
        return self.coins_in_squeezeOn, None

class TG_BUTTON_HANDLER(TG_ASSISTENT):
    def __init__(self):
        super().__init__()

    def open_order_tgButton_handler(self, message):
        item = {}  
        try:
            symbol = item["symbol"] = message.text.split(' ')[0].strip().upper() + 'USDT'       
            item["defender"] = int(message.text.split(' ')[1].strip())
            self.depo = int(message.text.split(' ')[2].strip())
            item['in_position'] = False
            item['qnt'] = None 
            item["recalc_depo"] = None 
            item["price_precision"] = None 
            item["tick_size"] = None
            item["current_price"] = self.get_current_price(symbol)
            print(f'item["current_price"]: {item["current_price"]}')

            timeframe = '15m'
            limit = 100
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
        except Exception as ex:
            print(f"main121: {ex}")
        return None
       
    async def go_tgButton_handler(self, message):                
        cur_time = time.time()
        date_of_the_month_start = await self.date_of_the_month()       

        while True:            
            last_update_time = time.time() - cur_time              
            
            if (cur_time - last_update_time)/5 >= 1:    
                async with self.lock_candidate_coins: 
                    if (self.stop_bot_flag) and ((self.go_progression == 0) or 
                        (self.go_progression == 1 and self.stop_squeezeAddition_func_flag) or 
                        (self.go_progression == 2 and self.websocket_stop_returned_flag)):    
                        self.go_progression = 0  
                        self.stop_bot_flag = False                                        
                        return "The robot was stopped!"               

            if not self.data_updating_flag:
                self.go_progression += 1
                self.coins_in_squeezeOn = []  
                self.data_updating_flag = True 
                self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = await self.squeeze_unMomentum_addition()                                   
                just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]                      
                print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")                         

            if not self.websocket_launch_flag:
                if self.stop_squeezeAddition_func_flag != "Stop data_updating_func":
                    if self.coins_in_squeezeOn:
                        self.go_progression += 1
                        self.websocket_launch_flag = True
                        tasks = [self.websocket_handler(self.coins_in_squeezeOn)]
                        return_webSocket = asyncio.gather(*tasks)
                    
                    else:
                        self.data_updating_flag = False
                        self.websocket_launch_flag = False
                        await asyncio.sleep(61)

                    
            async with self.lock_candidate_coins:  
                if self.websocket_pump_returned_flag:                            
                    self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
                    last_update_time = time.time() - cur_time  
                    duration = round(last_update_time/60, 2)
                    cur_time = time.time()
                    self.tg_response_allow = True    

            if self.tg_response_allow:
                response_textt = ""  

                for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
                    # volum_confirma = await self.volume_confirmation(symbol)
                    # if volum_confirma:                    
                    signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
                    link = f"https://www.coinglass.com/tv/Binance_{symbol}"
                    if defender == "PUMP":
                        defini_emoji_var = upper_trigon_emoji
                    else:
                        defini_emoji_var = lower_trigon_emoji
                    response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"
                if response_textt:
                    message.text = self.connector_func(message, response_textt)                    
                async with self.lock_candidate_coins: 
                    self.websocket_pump_returned_flag = False
                    self.pump_candidate_list = []  
                    
                self.tg_response_allow= False
                await asyncio.sleep(1)  

            if return_webSocket.done():
                results_ofTask_forWebsocket = return_webSocket.result()
                if True in results_ofTask_forWebsocket:
                    self.data_updating_flag = False
                    self.websocket_launch_flag = False
                    
            await asyncio.sleep(2)  
            print('await asyncio.sleep(2)')
    
             
class TG_MANAGER(TG_BUTTON_HANDLER):
    def __init__(self):
        super().__init__()

    def run(self):          

        @self.bot.message_handler(commands=['start'])
        def handle_start(message):

            self.init_itits()
            self.bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @self.bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):

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
            self.init_itits()
            response_message = "Please wait. It's gonna take some time...."
            message.text = self.connector_func(message, response_message)
            self.launch_finish_text = asyncio.run(self.go_tgButton_handler(message))
            message.text = self.connector_func(message, self.launch_finish_text)

        @self.bot.message_handler(func=lambda message: message.text == "OPEN_ORDER")
        def open_order(message):
            # self.init_itits()            
            response_message = "Please enter a coin and side with a space (e.g.: btc 1 9)"
            message.text = self.connector_func(message, response_message)
            self.order_triger = True
            self.open_order_redirect_flag = True           
            
        @self.bot.message_handler(func=lambda message: self.open_order_redirect_flag)
        def open_order_redirect(message):
            open_order_tgButton_handler_resp = self.open_order_tgButton_handler(message)
            self.order_triger = False

        @self.bot.message_handler(func=lambda message: message.text == "CLOSE_POSITION")
        def closee_pos(message):               
            response_message = "Please enter a coin(e.g.: btc)"
            message.text = self.connector_func(message, response_message)
            self.order_triger = True
            self.close_position_redirect_flag = True   

        @self.bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(message, response_message)                 

        self.bot.polling()

def main():
    my_bot = TG_MANAGER()
    my_bot.run()

if __name__=="__main__":
    main()