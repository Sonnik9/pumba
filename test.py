# import time 
# import random

# last_update_time = time.time()
# while True:
#     print(random.randrange(11,11111))
#     # current_time = time.time()
#     # time_difference = current_time - last_update_time
#     # if (time_difference)/10 >= 1:
#     #     print(time_difference)
#     #     last_update_time = current_time
#     time.sleep(1)

# print(f"kadjfvn\n\nadkfjbdgjkbn")

# signal_number_acumm_list = ["ETH", "BNB", "XRP", "LUNA", "ETH", "BNB", "BTC", "ETH", "BNB", "XRP", "LUNA", "ETH", "BNB"]
# symbol_list = ["BTC", "ETH", "BNB", "XRP"]

# for pairs in symbol_list:
#     signal_number = sum(1 for x in signal_number_acumm_list if x == pairs)
#     print(f"{pairs}: {signal_number} times")
from datetime import datetime
import time
def cur_dateTime():        
    current_time = time.time()        
    datetime_object = datetime.fromtimestamp(current_time)       
    formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
    return str(formatted_time)

print(cur_dateTime())