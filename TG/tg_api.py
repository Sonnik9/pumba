from monitoringg import LIVE_MONITORING
import telebot
from telebot import types
from config import CONFIG
import time
from datetime import datetime
import asyncio

# rocket_emoji = "\U0001F680"
# lightning_emoji = "\u26A1"
# clock_emoji = "\u231A"
# film_emoji = "\U0001F39E"
# percent_emoji = "%"
# repeat_emoji = "\U0001F501"

# 💰 (U+1F4B0)
# 💵 (U+1F4B5)
# 💲 (U+1F4B2)

# ✅ (U+2705)
# ☑️ (U+2611)
# ✔️ (U+2714)

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
signal_number_emoji = "🔢"
signal_number_emoji = "№"
link_emoji = "🔗"

class TG_CONNECTOR(LIVE_MONITORING):
    def __init__(self):
        super().__init__()
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["SETTINGS", "GO", "BALANCE", "RESTART", "1", "2"]        
        self.settings_flag = False

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO") 
        button2 = types.KeyboardButton("SETTINGS")        
        button3 = types.KeyboardButton("BALANCE")
        button4 = types.KeyboardButton("RESTART")
        menu_markup.add(button1, button2, button3, button4)        
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
            bot.send_message(message.chat.id, "Choose an option:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == 'RESTART')
        def handle_start(message):
            bot.send_message(message.chat.id, "Bot restart. Please, choose an option!:", reply_markup=self.menu_markup)

        @bot.message_handler(func=lambda message: message.text == "SETTINGS")
        def settingss(message):
            response_message = "Please select a settings options..." 
            message.text = self.connector_func(bot, message, response_message) 
            self.settings_flag = True

        @bot.message_handler(func=lambda message: message.text == "BALANCE")
        def balance(message):
            balance = self.get_balance()
            response_message = f"Your {self.market} balance is: {balance}"
            message.text = self.connector_func(bot, message, response_message)   

        # //////////////////////////////////////////////////////////////////////  

        @bot.message_handler(func=lambda message: message.text == "GO")
        def go(message):
            response_message = "Please wait. It may take a several time..."
            message.text = self.connector_func(bot, message, response_message)  

            async def launch():
                start_time = time.time()
                date_of_the_month_start = await self.date_of_the_month()
                signal_number_acumm_list = []
                while True:  
                    response_textt = ''''''         
                    top_coins = await self.assets_filters_1()
                    print(f"len(top_coins): {len(top_coins)}")
                    # print(top_coins[0:10])            
                    coins_in_squeezeOn = []                    
                    candidate_coins = []                  
                                       
                    for symbol in top_coins:
                        m15_data = None                
                        timeframe = '15m'
                        limit = 100
                        try:
                            m15_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)        
                            m15_data = await self.squeeze_unMomentum(m15_data)
                            if m15_data['squeeze_on'].iloc[-1]:
                                coins_in_squeezeOn.append({"symbol": symbol, "prev_close_1m": ""})
                        except:
                            continue               
                    just_squeeze_symbol_list = [x["symbol"] for x in coins_in_squeezeOn]                   
                    print(f"len(coins_in_squeezeOn): {len(coins_in_squeezeOn)}")
                    print("Монеты в сжатии:", just_squeeze_symbol_list)                 

                    candidate_coins = await self.price_volume_monitoring(coins_in_squeezeOn)

                    just_candidate_symbol_list = [x[0] for x in candidate_coins]
                    signal_number_acumm_list += just_candidate_symbol_list
                    print("Кандидаты в ПАМП/ДАМП:", just_candidate_symbol_list)
                    date_of_the_month_current = await self.date_of_the_month()
                    if date_of_the_month_current != date_of_the_month_start:
                        signal_number_acumm_list = []
                        date_of_the_month_start = date_of_the_month_current

                    finish_time = time.time() - start_time  
                    duration = round(finish_time/3600, 2)
                    start_time = time.time()
                       
                    for pairs, defender, cur_per_change, curTimee in candidate_coins:
                        volum_confirma = await self.volume_confirmation(pairs)
                        signal_number = sum(1 for x in signal_number_acumm_list if x == pairs)
                        link = f"https://www.coinglass.com/tv/Binance_{pairs}"
                        if defender == "PUMP":
                            defini = upper_trigon_emoji
                        else:
                            defini = lower_trigon_emoji
                        response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} --- {pairs}\n{clock_emoji} --- {curTimee}\n{defini} --- {defender}\n{percent_emoji} --- {cur_per_change}\n{confirm_emoji} (volum) --- {str(volum_confirma)}\n{film_emoji} --- {duration} h\n{signal_number_emoji} --- {signal_number}\n{link_emoji} --- {link}\n\n{money_emoji} {money_emoji} {money_emoji}"
                    message.text = self.connector_func(bot, message, response_textt)
                    # break

            asyncio.run(launch())  


        @bot.message_handler(func=lambda message: message.text not in self.reserved_frathes_list)
        def exceptions_input(message):
            response_message = f"Try again and enter a valid option."
            message.text = self.connector_func(bot, message, response_message)                 

        bot.polling()

def main_tg_func():   
    my_bot = TG_ASSISTENT()
    my_bot.run()