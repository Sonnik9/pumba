# # # import random 
# # # import time

# # # while True:
# # #     random_sleep = random.randrange(0,3) + (random.randrange(1,9)/10)
# # #     time.sleep(random_sleep)
# # #     print(random_sleep)

# # # d = 0.008849558
# # # c = round(d,2)
# # # print(c)

# # symbol_data = {'symbol': 'ETHUSDT', 'pair': 'ETHUSDT', 'contractType': 'PERPETUAL', 'deliveryDate': 4133404800000, 'onboardDate': 1569398400000, 'status': 'TRADING', 'maintMarginPercent': '2.5000', 'requiredMarginPercent': '5.0000', 'baseAsset': 'ETH', 'quoteAsset': 'USDT', 'marginAsset': 'USDT', 'pricePrecision': 2, 'quantityPrecision': 3, 'baseAssetPrecision': 8, 'quotePrecision': 8, 'underlyingType': 'COIN', 'underlyingSubType': [], 'settlePlan': 0, 'triggerProtect': '0.0500', 'liquidationFee': '0.020000', 'marketTakeBound': '0.10', 'maxMoveOrderLimit': 10000, 'filters': [{'maxPrice': '95264.25', 'filterType': 'PRICE_FILTER', 'tickSize': '0.01', 'minPrice': '18.67'}, {'minQty': '0.001', 'stepSize': '0.001', 'maxQty': '10000', 'filterType': 'LOT_SIZE'}, {'filterType': 'MARKET_LOT_SIZE', 'stepSize': '0.001', 'minQty': '0.001', 'maxQty': '10000'}, {'filterType': 'MAX_NUM_ORDERS', 'limit': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'limit': 10}, {'filterType': 'MIN_NOTIONAL', 'notional': '20'}, {'multiplierDown': '0.9000', 'filterType': 'PERCENT_PRICE', 'multiplierDecimal': '4', 'multiplierUp': '1.1000'}], 'orderTypes': ['LIMIT', 'MARKET', 'STOP', 'STOP_MARKET', 'TAKE_PROFIT', 'TAKE_PROFIT_MARKET', 'TRAILING_STOP_MARKET'], 'timeInForce': ['GTC', 'IOC', 'FOK', 'GTX', 'GTD']}
# # lot_size_filter = next((item for item in symbol_data['filters'] if item['filterType'] == 'MIN_NOTIONAL'), None)  
# # notional = float(lot_size_filter.get('notional', None))
# # print(notional)

# # import requests

# # url = "https://open-api.coinglass.com/public/v2/indicator/liquidation_pair?ex=Binance&pair=BTCUSDT&interval=h1&start_time=1668481704000&end_time=1668568104000"

# # headers = {
# #     "accept": "application/json",
# #     "coinglassSecret": '1557b4ccbc624592b6b5c2d6a4d660ef'
# # }

# # response = requests.get(url, headers=headers)

# # print(response.text)



# # import requests

# # url = "https://fapi.binance.com/fapi/v1/allForceOrders"
# # params = {
# #     "symbol": "BTCUSDT",
# # }

# # response = requests.get(url, params=params)

# # # Check if the request was successful (status code 200)
# # if response.status_code == 200:
# #     print(response.json())
# # else:
# #     if response.status_code == 400 and "The endpoint has been out of maintenance" in response.text:
# #         print("The endpoint is currently undergoing maintenance. Please try again later.")
# #     else:
# #         print(f"Error: {response.status_code}, {response.text}")


# from selenium import webdriver
# from selenium.webdriver.common.by import By

# url = "https://www.coinglass.com/tv/Binance_TIAUSDT"

# # Initialize the webdriver (make sure you have the appropriate webdriver installed)
# driver = webdriver.Chrome()

# # Open the webpage
# driver.get(url)

# # Find the first header on the page (assuming it's an h1 tag)
# first_header = driver.find_element(By.TAG_NAME, 'h1')

# if first_header:
#     print("First Header:", first_header.text.strip())
# else:
#     print("No header found on the page.")

# # Close the webdriver
# driver.quit()


