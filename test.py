# import requests
# import hashlib
# import time

# api_key = "96f214ce691b0dd8fc65b23002ee4e5ce0b55684598645c2eb2d0a819a6d387a"
# api_secret = "46e1372c84151cd7d486a4734cc21023ba1724d067b5967ce48ce769025cf0d2"
# symbol = 'BTCUSDT'
# margin_type = 'ISOLATED'  # 'CROSSED' для кросс-маржи

# # Вспомогательная функция для подписи запроса
# def generate_signature(params):
#     query_string = '&'.join([f'{key}={params[key]}' for key in sorted(params.keys())])
#     return hashlib.sha256(query_string.encode('utf-8')).hexdigest()

# # Создаем запрос для изменения типа маржи
# timestamp = int(time.time() * 1000)
# params = {
#     'timestamp': timestamp,
#     'symbol': symbol,
#     'type': margin_type,  # Заменил 'marginType' на 'type'
#     'newClientOrderId': 'CHANGE_MARGIN_TYPE',
#     'recvWindow': 5000,
#     'signature': '',
# }

# params['signature'] = generate_signature(params)

# url = 'https://testnet.binancefuture.com/fapi/v1/marginType'
# response = requests.post(url, params=params, headers={'X-MBX-APIKEY': api_key})

# if response.status_code == 200:
#     print('Тип маржи успешно изменен.')
#     print(response.json())
# else:
#     print(f'Ошибка при изменении типа маржи: {response.text}')

# import logging, os, inspect

# logging.basicConfig(filename='config_log.log', level=logging.INFO)
# current_file = os.path.basename(__file__)

# try:
#     a = 'kbgv'
#     b = int(a)
# except Exception as ex:
#     logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")