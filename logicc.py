from monitoringg import LIVE_MONITORING
import time
# from datetime import datetime
import asyncio

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


class MAIN_LOGIC(LIVE_MONITORING):
    def __init__(self) -> None:
        super().__init__()

    async def websocket_precession(self, symbol):
        precession_upgraded_data = {}
        try:
            self.KLINE_TIME, self.TIME_FRAME = 1, 'm'
            self.INTERVAL = str(self.KLINE_TIME) + self.TIME_FRAME
            timeframe = '1m'
            limit = 12
            m1_data = await self.get_ccxtBinance_klines(symbol, timeframe, limit)  
            close_1m_5_dataFramelist = m1_data['Close']
            close_1m_5_list = close_1m_5_dataFramelist.dropna().to_list()
            mean_close_1m_5 = close_1m_5_dataFramelist.mean()         
            
            close_pct_changes_5_list = [abs((new - old) / old) * 100 if old != 0 else 0 for old, new in zip(close_1m_5_list[:-1], close_1m_5_list[1:])]

            mean_close_pct_change_5 = sum(close_pct_changes_5_list) / len(close_pct_changes_5_list)
            cur_price_agregated_compearer_5 = mean_close_pct_change_5 * self.PRICE_KLINE_1M_MULTIPLITER

            if mean_close_1m_5 != 0:
                precession_upgraded_data = {
                    "symbol": symbol, 
                    "prev_close_1m": "",                            
                    "cur_price_agregated_compearer_5": abs(cur_price_agregated_compearer_5)
                    
                }   
        except:
            print('Some problem with m1 data')         

        return precession_upgraded_data
    # //////////////////////////////////////////////////////////

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

    async def launch(self, message):                
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
                        message.text = self.connector_func(message, response_textt)                    

                    self.websocket_pump_returned_flag = False
                    self.pump_candidate_list = []  
                    await asyncio.sleep(1)                  

            await asyncio.sleep(4)  
            print('await asyncio.sleep(4)')
            # break