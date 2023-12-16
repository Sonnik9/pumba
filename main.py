# from TG.tg_api import main_tg_func

# def main():
#     main_tg_func() 

# if __name__=="__main__":
#     main()


from datetime import datetime
import time

# Получение текущего времени в формате timestamp
current_time = time.time()

# Преобразование timestamp в объект datetime
datetime_object = datetime.fromtimestamp(current_time)

# Преобразование объекта datetime в строку с заданным форматом
formatted_time = datetime_object.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_time)