from tg_assistent_py import TG_ASSISTENT
import asyncio 
import time
import logging, os, inspect

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

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

class TG_BUTTON_HANDLER(TG_ASSISTENT):
    def __init__(self):
        super().__init__()

    async def open_order_tgButton_handler(self):
        item = {}  
        open_order_returned_list = []
        try:
            item["symbol"] = self.symbol 
            item["defender"] = self.defender

            item['in_position'] = False
            item['qnt'] = None 
            item["recalc_depo"] = None 
            item["price_precision"] = None 
            item["tick_size"] = None
            item["current_price"] = await self.get_current_price(self.symbol)
            print(f'item["current_price"]: {item["current_price"]}')

            timeframe = '15m'
            limit = 100
            m1_15_data = await self.get_ccxtBinance_klines(self.symbol, timeframe, limit)            
            m1_15_data['TR'] = abs(m1_15_data['High'] - m1_15_data['Low'])
            m1_15_data['ATR'] = m1_15_data['TR'].rolling(window=14).mean()
            item['atr'] = m1_15_data['ATR'].iloc[-1]

            item = await self.make_market_order_temp_func(item)

            if item['in_position']:
                open_order_returned_list.append(1)
                item = await self.tp_make_orders(item)
                if item["done_level"] == 2:
                    open_order_returned_list.append(2)   
                else:
                    open_order_returned_list.append(-2) 
            else:
                open_order_returned_list.append(-1)
        except Exception as ex:
            open_order_returned_list.append(0)
            print(f"main121: {ex}")

        return open_order_returned_list

    async def stop_tgButton_handler(self, tasks):
        try:
            await asyncio.gather(*tasks, return_exceptions=True)
        except asyncio.CancelledError:            
            pass
        finally:
            await asyncio.sleep(3)
            return True
        
    async def go_tgButton_handler(self, message):
        print('ksdvksfhbvb')
        cur_time = time.time()
        tg_response_allow = False
        last_duration_time = None
        duration = None
        date_of_the_month_start = await self.date_of_the_month()
        return_web_socket_task = None
        return_squeeze_unMomentum_assignator = None
        return_open_order_tgButton_handler = None
        answer_open_order_tgButton_handler = None
        return_info_tgButton_handler = None 
        answer_tg_reply = None
        return_closeAll_pos_tgButton_handler = None
        answer_closeAll_pos_tgButton_handler = None
        coins_in_squeezeOn = []
        coins_in_squeezeOff_var = []
        success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list = [], [], [], []
        return_closeCustom_pos_tgButton_handler = None
        answer_closeCustom_pos_tgButton_handler = None

        tasks = []        

        while True:
            # print("Before sleep1")
            await asyncio.sleep(1)
            # print("After sleep1")
            try:
                # /////////////////////////////////////////////////////////////////////////////////////        
                if self.stop_triger_flag and self.stop_triger_tumbler_flag:
                    self.stop_triger_tumbler_flag = False
                    print(' sfhdvbfkvb')
                    
                    if tasks:
                        stop_response = None
                        stop_response = await self.stop_tgButton_handler(tasks)
                        if stop_response:
                            self.stop_triger_flag = False
                            return "The robot was stopped!"
                    else:
                        self.stop_triger_flag = False
                        return "The robot was stopped!"
                    
                if self.get_balance_flag:
                    self.get_balance_flag = False
                    balance = await self.get_balance()
                    response_message = f"Your {self.market} balance is: {balance}"
                    message.text = self.connector_func(message, response_message) 
                # /////////////////////////////////////////////////////////////////////////////////////
                        
                # # /////////////////////////////////////////////////////////////////////////////////////
                if not self.data_updating_flag:
                    self.go_progression += 1
                    coins_in_squeezeOn = []
                    return_squeeze_unMomentum_assignator = None
                    self.data_updating_flag = True
                    task1 = [self.squeeze_unMomentum_assignator()]
                    tasks.append(task1)
                    return_squeeze_unMomentum_assignator = asyncio.gather(*task1)
                    return_web_socket_task = None  # Задача для веб-сокетов создается при необходимости

                # print(f"self.go_progression: {self.go_progression}")

                if return_squeeze_unMomentum_assignator and return_squeeze_unMomentum_assignator.done():
                    result_squeeze_unMomentum_assignator = return_squeeze_unMomentum_assignator.result()
                    # print(result_squeeze_unMomentum_assignator)
                    coins_in_squeezeOn = result_squeeze_unMomentum_assignator[0][0]
                    coins_in_squeezeOff_var = result_squeeze_unMomentum_assignator[0][1]
                    print(f"Монеты по выходу из сжатия: {coins_in_squeezeOff_var}\n {len(coins_in_squeezeOff_var)} шт")
                    response_textt = ""
                    for sy in coins_in_squeezeOff_var:
                        volum_confirma = False
                        volum_confirma = await self.volume_confirmation(sy)
                        # if volum_confirma:                          
                        link = f"https://www.coinglass.com/tv/Binance_{sy}"
                        response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {sy}\n{confirm_emoji} ___ {volum_confirma}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"                   

                    if response_textt:
                        message.text = self.connector_func(message, response_textt)
                    # //////////////////////////////////////////////////////////////////////
                    just_squeeze_symbol_list = [x["symbol"] for x in coins_in_squeezeOn]
                    print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(coins_in_squeezeOn)} шт")
                    return_squeeze_unMomentum_assignator = None 
                    self.websocket_launch_flag = True
                # /////////////////////////////////////////////////////////////////////////////////////
                    
                # /////////////////////////////////////////////////////////////////////////////////////
                if self.websocket_launch_flag and len(coins_in_squeezeOn) !=0:
                    self.go_progression += 1
                    self.websocket_launch_flag = False
                    tasks = []
                    task2 = [self.websocket_handler(coins_in_squeezeOn)]
                    tasks.append(task2)                    
                    return_web_socket_task = asyncio.gather(*task2)

                elif self.websocket_launch_flag and len(coins_in_squeezeOn) == 0:
                    await asyncio.sleep(21)
                    self.data_updating_flag = False

                # print(f"self.go_progression: {self.go_progression}")

                if return_web_socket_task and return_web_socket_task.done():
                    results_of_task_for_websocket = return_web_socket_task.result()
                    if True in results_of_task_for_websocket:                        
                        self.data_updating_flag = False
                        self.websocket_launch_flag = False
                        return_web_socket_task = None
                # /////////////////////////////////////////////////////////////////////////////////////
                        
                # /////////////////////////////////////////////////////////////////////////////////////
                async with self.lock_candidate_coins:
                    if self.websocket_pump_returned_flag:
                        self.websocket_pump_returned_flag = False
                        self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
                        last_duration_time = time.time() - cur_time
                        duration = round(last_duration_time / 60, 2)
                        cur_time = time.time()
                        tg_response_allow = True

                if tg_response_allow:
                    tg_response_allow = False
                    response_textt = ""

                    for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
                        volum_confirma = False
                        volum_confirma = await self.volume_confirmation(symbol)
                        if volum_confirma:                        
                            signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
                            link = f"https://www.coinglass.com/tv/Binance_{symbol}"
                            if defender == "PUMP":
                                defini_emoji_var = upper_trigon_emoji
                            else:
                                defini_emoji_var = lower_trigon_emoji
                            response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{confirm_emoji} ___ {volum_confirma}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"
                            
                            async with self.lock_candidate_coins:
                                self.pump_candidate_busy_confirm_list.append(symbol)

                    if response_textt:
                        message.text = self.connector_func(message, response_textt)
                            
                    async with self.lock_candidate_coins:                        
                        self.pump_candidate_list = []

                    
                # /////////////////////////////////////////////////////////////////////////////////////
                        
                # /////////////////////////////////////////////////////////////////////////////////////
                if self.info_triger:     
                    self.info_triger = False                
                    task4 = [self.positions_info()]
                    tasks.append(task4)
                    return_info_tgButton_handler = asyncio.gather(*task4)

                if return_info_tgButton_handler and return_info_tgButton_handler.done():                    
                    answer_tg_reply = return_info_tgButton_handler.result()
                    return_info_tgButton_handler = None   
                    print(answer_tg_reply)
                    if answer_tg_reply[0]:                        
                        info_tg_reply = answer_tg_reply[0]     
                        message.text = self.connector_func(message, info_tg_reply)
                    elif answer_tg_reply[0] == []:
                        info_tg_reply = "There is no one open order"
                        message.text = self.connector_func(message, info_tg_reply)
                    elif answer_tg_reply[0] == None:
                        info_tg_reply = "Some problems with getting positions data..."
                        message.text = self.connector_func(message, info_tg_reply)

                # /////////////////////////////////////////////////////////////////////////////////////
                
                # /////////////////////////////////////////////////////////////////////////////////////
                if self.close_order_triger and self.symbol and self.depo:
                    self.close_order_triger = False
                    task5 = [self.close_custom_poss(self.symbol)]
                    tasks.append(task5)
                    return_closeCustom_pos_tgButton_handler = asyncio.gather(*task5)

                if return_closeCustom_pos_tgButton_handler and return_closeCustom_pos_tgButton_handler.done():
                    answer_closeCustom_pos_tgButton_handler = return_closeCustom_pos_tgButton_handler.result()
                    return_closeCustom_pos_tgButton_handler = None
                    close_tg_reply = ""
                    success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list = answer_closeCustom_pos_tgButton_handler[0]
                    close_tg_reply = await self.closePos_template(success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list, close_tg_reply)

                    success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list = [], [], [], []
                    message.text = self.connector_func(message, close_tg_reply)
                # ///////////////////////////////////////////////////////////////////////////////////////

                if self.close_all_orderS_triger:                    
                    self.close_all_orderS_triger = False
                    task4 = [self.close_all_poss()]
                    tasks.append(task4)
                    return_closeAll_pos_tgButton_handler = asyncio.gather(*task4)

                if return_closeAll_pos_tgButton_handler and return_closeAll_pos_tgButton_handler.done():
                    answer_closeAll_pos_tgButton_handler = return_closeAll_pos_tgButton_handler.result()
                    return_closeAll_pos_tgButton_handler = None
                    close_tg_reply = ""
                    success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list = answer_closeAll_pos_tgButton_handler[0]
                    close_tg_reply = await self.closePos_template(success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list, close_tg_reply)

                    success_closePosition_list, problem_closePosition_list, cancel_orders_list, unSuccess_cancel_orders_list = [], [], [], []
                    message.text = self.connector_func(message, close_tg_reply)
                # /////////////////////////////////////////////////////////////////////////////////////

                # /////////////////////////////////////////////////////////////////////////////////////
                        
                if self.order_triger and self.symbol:
                    self.order_triger = False
                    task3 = [self.open_order_tgButton_handler()]
                    tasks.append(task3)
                    return_open_order_tgButton_handler = asyncio.gather(*task3)
                    
                if return_open_order_tgButton_handler and return_open_order_tgButton_handler.done():
                    answer_open_order_tgButton_handler = return_open_order_tgButton_handler.result()
                    if 0 in answer_open_order_tgButton_handler[0]:
                        order_tg_reply = "Some exceptions with placeing order..." + '\n'
                        message.text = self.connector_func(message, order_tg_reply)
                    if -1 in answer_open_order_tgButton_handler[0]:
                        order_tg_reply = "Some problem with placeing order..." + '\n'
                        message.text = self.connector_func(message, order_tg_reply)
                    if -2 in answer_open_order_tgButton_handler[0]:
                        order_tg_reply = "Some problem with setting takeProfit..." + '\n'
                        message.text = self.connector_func(message, order_tg_reply)
                    if 1 in answer_open_order_tgButton_handler[0]:
                        order_tg_reply = "The order was created successuly!" + '\n'
                        message.text = self.connector_func(message, order_tg_reply)
                    if 2 in answer_open_order_tgButton_handler[0]:
                        order_tg_reply = "The takeProfit was setting successuly!" + '\n'
                        message.text = self.connector_func(message, order_tg_reply)
                    return_open_order_tgButton_handler = None


                # /////////////////////////////////////////////////////////////////////////////////////

                # print("Before sleep2")
                await asyncio.sleep(1)
                # print("After sleep2")

            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
