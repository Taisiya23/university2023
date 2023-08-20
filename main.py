# import vk_api
# token = 'vk1.a.HGdVOKT3tUbOs3APy5ps1gC42hFMvzUdTnSz1uXRuj2PLT4M3vPlDvIeyugYogZMvJAWR4DS-PTs7RIxdIrHo6s6zvMu-I4hyXyTKiya-95tGvlxYfpAfyRsc5DKvyfl_U56yczoSfvSBaPcJn0fHI6w9ft1ZQShlD8qaG8pZGCNbaHcsAgEx_WO5Uhkr_NnmXeu8HlW5cNtrsKWtSqF4g'


# my_iter = (x for x in range(1, 100_000_000))
# for elem in my_iter:
#      print(elem)


# print(my_iter)

# def my_lazy_gen():
#     for x in range(10):
#         print('до', x)
#         yield x
#         print('после', x)
# for i in my_lazy_gen():
#     print(i)

# with open('file.txt', 'w') as f:
#     f.write('1111')
#     print(f.closed)
# print(f.closed)


# my_list = []
# for x in range(0, 100_000_000):
#     x = x**2
#     my_list.append(x)
#     print(x)
#

# goods = [
#     {
#         'name': 'Iphone 14',
#         'brand': 'Apple',
#         'price': 1400
#     },
#     {
#         'name': 'Samsung Galaxy A23',
#         'brand': 'Samsung',
#         'price': 700
#     },
#     {
#         'name': 'Xiaomi mi8 lite',
#         'brand': 'Xiaomi',
#         'price': 300
#     }
# ]

# def item_price(item):
#     return item['name']

# print(sorted(goods, key=lambda item: item['price']))

# apple_list = filter(lambda item: item['brand']=='Apple' , goods)
# print(list(apple_list))



# numbers = ['1', '2', '3']
# number_map = map(lambda item: item + 's', numbers)
# print(list(number_map))


# for item in goods:
#     print(item)

# for index, item in enumerate(goods):
#     print(index, item)



# names_list = ['данил', 'артём', 'никита', 'влад']
# name_list_map = map(lambda item: item.capitalize(), names_list)
# print(list(name_list_map))


import sqlite3





















