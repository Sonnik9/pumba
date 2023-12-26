# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return 'slkdfjvn'

# async def foo():
#     start_flag = False
#     return_foo2 = None
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             loop = asyncio.get_event_loop()
#             return_foo2 = loop.create_task(foo2())
#             # Можно также использовать asyncio.create_task(foo2())
#             start_flag = True
#         print(return_foo2)
        
#         if return_foo2 and return_foo2.done():
#             result = return_foo2.result()
#             if result == 'slkdfjvn':
#                 print('It is success!!')
#                 return

# asyncio.run(foo())


# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return 'slkdfjvn'

# async def foo():
#     start_flag = False
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             tasks = [foo2()]
#             return_foo2 = asyncio.gather(*tasks)
#             start_flag = True
#         print(return_foo2)

#         if return_foo2.done():
#             results = return_foo2.result()
#             if 'slkdfjvn' in results:
#                 print('It is success!!')
#                 return

# asyncio.run(foo())


# import asyncio

# async def foo2():
#     print('foo2')
#     counter = 0
#     while True:
#         await asyncio.sleep(1)
#         print('tik!')
#         counter += 1
#         if counter == 5:
#             return 'slkdfjvn'

# async def foo():
#     start_flag = False
#     while True:
#         await asyncio.sleep(1)
#         if not start_flag:
#             tasks = [foo2()]
#             return_foo2 = asyncio.gather(*tasks)
#             start_flag = True

#         # Проверка, завершилась ли задача
#         if return_foo2.done():
#             results = return_foo2.result()
#             if 'slkdfjvn' in results:
#                 print('It is success!!')
#                 print(results[0])
#                 return results[0]  # Извлекаем результат из списка

# asyncio.run(foo())


import asyncio

async def foo2():
    print('foo2')
    counter = 0
    while True:
        await asyncio.sleep(1)
        print('tik!')
        counter += 1
        if counter == 5:
            return ['slkdfjvn']

async def foo():
    start_flag = False
    while True:
        await asyncio.sleep(1)
        if not start_flag:
            tasks = [foo2()]
            return_foo2 = asyncio.gather(*tasks)
            start_flag = True

        # Проверка, завершилась ли задача
        if return_foo2.done():
            results = return_foo2.result()

            # Проверка, является ли результат списком
            if isinstance(results, list):
                print('It is a list!!')

                # Проверка, что все элементы в списке также являются списками
                if all(isinstance(item, list) for item in results):
                    print('All items in the list are lists.')
                print(results[0])
                return   # Извлекаем результат из списка

asyncio.run(foo())

