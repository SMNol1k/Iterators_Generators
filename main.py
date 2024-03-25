# my_list = [1, 2, 3, 4, 5, 6]
from time import sleep

# for num in my_list:
#     print(num)

# my_iterator = iter(my_list)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


# class MyIterator:
#     def __init__(self, limit):
#         self.limit = limit
#
#     def __iter__(self):
#         print('Начинаем цикл')
#         self.counter = 0
#         return self
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return f'очередная итерация {self.counter}'
#         else:
#             raise StopIteration
#
#
# for item in MyIterator(5):
#     print(item)
#     sleep(1)
# print('Цикл завершен!')


# class MyRange:
#     def __init__(self, a, b=None, c=None):
#         if c is not None:
#             self.start = a
#             self.end = b
#             self.step = c
#         elif b is not None:
#             self.start = a
#             self.end = b
#             self.step = 1
#         else:
#             self.start = 0
#             self.end = a
#             self.step = 1
#
#     def __iter__(self):
#         self.current = self.start
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         else:
#             self.current += self.step
#             return self.current - self.step
#
#
# for i in MyRange(1000000000):
#     print(i)


import requests

# class SWHeroes:
#     def __iter__(self):
#         self.next_page = 'https://swapi.dev/api/people/'
#         self.results = iter([])
#         return self
#
#     def __next__(self):
#         try:
#             next_item = next(self.results)
#         except StopIteration:
#             if self.next_page is None:
#                 raise StopIteration
#             response = requests.get(self.next_page)
#             data = response.json()
#             self.results = iter(data['results'])
#             self.next_page = data['next']
#             next_item = next(self.results)
#         return next_item


# for hero in SWHeroes():
#     print(hero['name'])


# def generator_1():
#     yield 1
#     print('перед возвратом 2')
#     yield 2
#     yield 3
#     yield 4
#     yield 5


# print(type(generator_1()))
# print(dir(generator_1()))

# for item in generator_1():
#     print(item)
#     sleep(3)


# def generator_2(limit):
#     for item in range(limit):
#         yield item
#         sleep(1)


# def generator_3():
#     my_list = ['a', 'b', 'c']
#     # for item in my_list:
#     #     yield item
#     yield from my_list
#
#
# for i in generator_3():
#     print(i)


# def sw_heroes():
#     next_page = 'https://swapi.dev/api/people/'
#     while next_page:
#         response = requests.get(next_page)
#         data = response.json()
#         # yield from data['results']
#         for result in data['results']:
#             yield result
#         next_page = data['next']
#
#
# for hero in sw_heroes():
#     print(hero['name'])


numbers = [1, 2, 4, 5, 6, 8, 21] # -> [4, 16, 36, 64]

squares_1 = []
for item in numbers:
    if item % 2 == 0:
        squares_1.append(item ** 2)
print(squares_1)


squares_2 = [num ** 2 for num in numbers if num % 2 == 0]
print(squares_2)

# squares_3 = (num ** 2 for num in numbers if num % 2 == 0)
# for item in squares_3:
#     print(item, end=", ")

squares_4 = (num ** 2 for num in numbers if num % 2 == 0)
print(squares_4)