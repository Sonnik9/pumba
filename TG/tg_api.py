from monitoringg import LIVE_MONITORING
import telebot
from telebot import types
from config import CONFIG
import time
from datetime import datetime
import asyncio

# 💰 (U+1F4B0)
# 💵 (U+1F4B5)
# 💲 (U+1F4B2)

# ✅ (U+2705)
# ☑️ (U+2611)
# ✔️ (U+2714)
# signal_number_emoji = "🔢"
# signal_number_emoji = "№"

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
confirm_emoji = "(U+2714)"
link_emoji = "🔗"

class TG_CONNECTOR(LIVE_MONITORING):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SETTINGS", "GO", "STOP", "BALANCE", "RESTART", "1", "2"]
        self.signal_number_acumm_list = []
        

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO") 
        button2 = types.KeyboardButton("SETTINGS")        
        button3 = types.KeyboardButton("BALANCE")
        button4 = types.KeyboardButton("RESTART")
        button5 = types.KeyboardButton("STOP")
        menu_markup.add(button1, button2, button3, button4, button5)        
        return menu_markup

    def connector_func(self, bot, message, response_message):
        retry_number = 3
        decimal = 2        
        for i in range(retry_number):
            try:
                bot.send_message(message.chat.id, response_message)                
                return message.text
            except:
                time.sleep(2 + i*decimal)        
        return None
    
    async def data_updating_func(self):
        self.coins_in_squeezeOn = []
        top_coins = await self.assets_filters_1()
        print(f"len(top_coins): {len(top_coins)}")
        # print(top_coins[0:10])                       
        for symbol in top_coins:
            if self.stop_bot_flag:
                return self.coins_in_squeezeOn, "Stop data_updating_func"
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
    
class TG_ASSISTENT(TG_CONNECTOR):
    def __init__(self):
        super().__init__()

    def update_main_paramss(self, new_market, new_test_flag):
        self.market = new_market
        self.test_flag = new_test_flag
        self.init_itits()

    def run(self):
        bot = self.bot        

        @bot.message_handler(commands=['start'])
        def handle_start(message):

            self.init_itits()
            bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            self.pump_candidate_busy_list = [] 
            self.signal_number_acumm_list = [] 
            self.init_itits()
            bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            
            response_message = "Please select a settings options..." 
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_tg_flag = True

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(bot, message, response_message)   

        @bot.message_handler(func=lambda message: message.text == "STOP")
        def stop(message):
            self.stop_bot_flag = True
        # //////////////////////////////////////////////////////////////////////  

        @bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):
            self.init_itits()
            
            response_message = "Please wait. It's gonna take some time...."
            message.text = self.connector_func(bot, message, response_message)  

            async def launch():                
                cur_time = time.time()
                date_of_the_month_start = await self.date_of_the_month()           

                while True: 
                    last_update_time = time.time() - cur_time              
                    
                    if (cur_time - last_update_time)/3 >= 1:    
                        async with self.lock_candidate_coins: 
                            if (self.stop_bot_flag) and ((self.go_progression == 0) or 
                                (self.go_progression == 1 and self.stop_data_updating_func_flag == "Stop data_updating_func") or 
                                (self.go_progression == 2 and self.websocket_stop_returned_flag)):                                              
                                return "The robot was stopped!"       
                        

                    if not self.data_updating_flag: 
                        self.go_progression += 1
                        self.coins_in_squeezeOn = []  
                        self.data_updating_flag = True 
                        self.coins_in_squeezeOn, self.stop_data_updating_func_flag = await self.data_updating_func()                                   
                        just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]                      
                        print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")                         

                    if not self.websocket_launch_flag:
                        if self.stop_data_updating_func_flag != "Stop data_updating_func":
                            if self.coins_in_squeezeOn:
                                self.go_progression += 1
                                self.websocket_launch_flag = True
                                #  = asyncio.create_task(self.websocket_handler(self.coins_in_squeezeOn))  
                                loop = asyncio.get_event_loop()
                                loop.create_task(self.websocket_handler(self.coins_in_squeezeOn))
                            
                            else:
                                self.data_updating_flag = False
                                self.websocket_launch_flag = False
                                await asyncio.sleep(61)
                            
                    async with self.lock_candidate_coins:   
                        if self.websocket_pump_returned_flag: 
                            response_textt = ""  
                            # self.go_progression += 1               
                            
                            just_candidate_symbol_list = [x[0] for x in self.pump_candidate_list]
                            self.signal_number_acumm_list += just_candidate_symbol_list
                            print("Кандидаты в ПАМП/ДАМП:", just_candidate_symbol_list)
                            date_of_the_month_current = await self.date_of_the_month()
                            if date_of_the_month_current != date_of_the_month_start:
                                self.signal_number_acumm_list = []
                                date_of_the_month_start = date_of_the_month_current
                                self.pump_candidate_busy_list = []

                            last_update_time = time.time() - cur_time  
                            duration = round(last_update_time/60, 2)
                            cur_time = time.time()
                        
                            for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
                                volum_confirma = await self.volume_confirmation(symbol)
                                if volum_confirma:
                                    signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
                                    link = f"https://www.coinglass.com/tv/Binance_{symbol}"
                                    if defender == "PUMP":
                                        defini_emoji_var = upper_trigon_emoji
                                    else:
                                        defini_emoji_var = lower_trigon_emoji
                                    response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} --- {symbol}\n{clock_emoji} --- {curTimee}\n{defini_emoji_var} --- {defender}\n{percent_emoji} --- {cur_per_change}\n{confirm_emoji} (volum) --- {str(volum_confirma)}\n{film_emoji} --- {duration} min\n{repeat_emoji} --- {signal_number}\n{link_emoji} --- {link}\n\n{money_emoji} {money_emoji} {money_emoji}"
                            if response_textt:
                                message.text = self.connector_func(bot, message, response_textt)                    

                            self.websocket_pump_returned_flag = False
                            self.pump_candidate_list = []  
                            await asyncio.sleep(1)                  

                    await asyncio.sleep(4)  
                    print('await asyncio.sleep(4)')
                    # break

            self.launch_finish_text = asyncio.run(launch())
            message.text = self.connector_func(bot, message, self.launch_finish_text)

        @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(bot, message, response_message)                 

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()