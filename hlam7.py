
        
                # if squeeze_task and squeeze_task.done():
                #     self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = squeeze_task.result()
                #     just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]
                #     print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")

            #     if not self.websocket_launch_flag and self.coins_in_squeezeOn:
            #         self.go_progression += 1
            #         self.websocket_launch_flag = True
            #         tasks = []
            #         tasks.append(self.websocket_handler(self.coins_in_squeezeOn))
            #         return_web_socket_task = asyncio.gather(*tasks)
                            
                # # print(self.go_progression)
                # if return_web_socket_task and return_web_socket_task.done():
                #     results_of_task_for_websocket = return_web_socket_task.result()
                #     if True in results_of_task_for_websocket:
                #         self.data_updating_flag = False
                #         self.websocket_launch_flag = False

                # async with self.lock_candidate_coins:
                #     if self.websocket_pump_returned_flag:
                #         self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(
                #             self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
                #         last_duration_time = time.time() - cur_time
                #         duration = round(last_duration_time / 60, 2)
                #         cur_time = time.time()
                #         self.tg_response_allow = True

                # if self.tg_response_allow:
                #     response_textt = ""

                #     for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
                #         signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
                #         link = f"https://www.coinglass.com/tv/Binance_{symbol}"
                #         if defender == "PUMP":
                #             defini_emoji_var = upper_trigon_emoji
                #         else:
                #             defini_emoji_var = lower_trigon_emoji
                #         response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"

                #     if response_textt:
                #         message.text = self.connector_func(message, response_textt)
                            
                #     async with self.lock_candidate_coins:
                #         self.websocket_pump_returned_flag = False
                #         self.pump_candidate_list = []

                #     self.tg_response_allow = False



#     import asyncio

# class TG_BUTTON_HANDLER(TG_ASSISTENT):
#     def __init__(self):
#         super().__init__()

#     async def go_tgButton_handler(self, message):
#         cur_time = time.time()
#         date_of_the_month_start = await self.date_of_the_month()
#         squeeze_task = None
#         return_web_socket_task = None

#         while True:
#             try:             

#                 if self.stop_triger_flag:
#                     if return_web_socket_task and return_web_socket_task.done():
#                         results_of_task_for_websocket = return_web_socket_task.result()
#                         if True in results_of_task_for_websocket:
#                             self.data_updating_flag = False
#                             self.websocket_launch_flag = False

#                     if squeeze_task and squeeze_task.done():
#                         self.coins_in_squeezeOn, self.stop_squeezeAddition_func_flag = squeeze_task.result()
#                         just_squeeze_symbol_list = [x["symbol"] for x in self.coins_in_squeezeOn]
#                         print(f"Монеты в сжатии: {just_squeeze_symbol_list}\n {len(self.coins_in_squeezeOn)} шт")

#                         if not self.websocket_launch_flag and self.coins_in_squeezeOn:
#                             self.go_progression += 1
#                             self.websocket_launch_flag = True
#                             return_web_socket_task = asyncio.create_task(self.websocket_handler(self.coins_in_squeezeOn))

#                     await asyncio.sleep(1)
#                     print('await asyncio.sleep(2)')

#                 if not self.data_updating_flag:
#                     self.go_progression += 1
#                     self.coins_in_squeezeOn = []
#                     self.data_updating_flag = True
#                     squeeze_task = asyncio.create_task(self.squeeze_unMomentum_assignator())

#                 async with self.lock_candidate_coins:
#                     if self.websocket_pump_returned_flag:
#                         self.signal_number_acumm_list, date_of_the_month_start = await self.signal_counter_assistent(
#                             self.pump_candidate_list, self.signal_number_acumm_list, date_of_the_month_start)
#                         last_duration_time = time.time() - cur_time
#                         duration = round(last_duration_time / 60, 2)
#                         cur_time = time.time()
#                         self.tg_response_allow = True

#                 if self.tg_response_allow:
#                     response_textt = ""

#                     for symbol, defender, cur_per_change, curTimee in self.pump_candidate_list:
#                         signal_number = sum(1 for x in self.signal_number_acumm_list if x == symbol)
#                         link = f"https://www.coinglass.com/tv/Binance_{symbol}"
#                         if defender == "PUMP":
#                             defini_emoji_var = upper_trigon_emoji
#                         else:
#                             defini_emoji_var = lower_trigon_emoji

#                         response_textt += f"{money_emoji} {money_emoji} {money_emoji}\n\n{rocket_emoji} ___ {symbol}\n{clock_emoji} ___ {curTimee}\n{defini_emoji_var} ___ {defender}\n{percent_emoji} ___ {cur_per_change}\n{film_emoji} ___ {duration} min\n{repeat_emoji} ___ {signal_number}\n{link_emoji} ___ {link}\n\n{money_emoji} {money_emoji} {money_emoji}"

#                     if response_textt:
#                         message.text = self.connector_func(message, response_textt)

#                     async with self.lock_candidate_coins:
#                         self.websocket_pump_returned_flag = False
#                         self.pump_candidate_list = []

#                     self.tg_response_allow = False

#                 await asyncio.sleep(1)
#                 print('await asyncio.sleep(2)')

#             except Exception as ex:
#                 logging.exception(f"An error occurred: {ex}")
