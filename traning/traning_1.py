# from library import *
#
# print('start')
#
# fun1(2,3)
# fun2(2,1)
#
# print('end')
#
# print('hi')
#
# def data(a, b):
#     print(f"a multiply with b is {a*b}")
#


# def run(func):
#     def in_fun(*args, **kwargs):
#         data = func(*args, **kwargs)
#         return data
#     return in_fun


# def run(func):
#     return func

# import time
#
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f'you are calling the {func.__name__} function')
#         start = time.time()
#         print(f'decorated function execution start {start}')
#         # op = func(*args, **kwargs)
#         end = time.time()
#         print(f'decorated function execution end {end}')
#         print(f'{func.__name__} function total time taking {end - start}')
#         op = func(*args, **kwargs)
#         return op
#     return wrapper
#
#
# @log
# def add(a, b):
#     print(a + b)
#
#
# @log
# def sub(a, b):
#     return a - b
#
#
# @log
# def string(name):
#     return f'hai {name}'
#
#
# @log
# def mul(a, b):
#     return a * b
#

# print(run(add(4,3)))


# add(a=1, b=2)

# sub(2, 4)
#
# string('hello')


# def test(l):
# ...     start = time.time()
# ...     for i in range(1000000):
# ...             l.append(i)
# ...     end = time.time()
# ...     print(len(l))
# ...     return f'append function take {end-start} time to do'



# def tu(t):
#     start = time.time()
#     for i in range(10000):
#         t += (i,)
#     end = time.time()
#     print(len(t))
#     return f'tuple_append function take {end - start} time to do'
#
#
# t = tuple()
# print(tu(t))

# __________________mock________________
# import re
# from itertools import islice
# s = 'Vishwas'
# s = s[::-1]
# print(s)
# s = 'Vishwas'
# s = str(reversed(s))
# print(s)
# s = 'Vishwas'
# ns = ''
# for i in s:
#     ns = i + ns
#     print(ns)
# s = 'Hello'
# print(ns)
# d = {}
# for c in s:
#     d[c] = d.get(c, 0) + 1
# print(d)
# l1 = ['a', 'b', 'c']
# l2 = [1, 2, 3]
# d = {i: j for i, j in zip(l1, l2)}
# print(d)
#
#
# class Emp:
#     cnt = 0
#
#     def __init__(self):
#         Emp.cnt += 1
#
#
# a = Emp()  # Emp.__init__(a)
# b = Emp()
# c = Emp()
# print(Emp.cnt)
#
# l = [i for i in range(1, 11)]
#
#
# def geven():
#     for i in l:
#         if i % 2 == 0:
#             yield i
#
#
# g = geven()
# print(next(g))
# print(next(g))
#
#
# with open(r'random.txt') as f:
#     cnt = 0
#     for i in f:
#         cnt += 1
#
#     f.seek(1)
#     lines = islice(f, cnt - 2, cnt)
#     for i in lines:
#         print(i)
#
#
# s = 'Vishwas123python78selenium12'
# print(sum(int(i) for i in re.findall(r'\d', s)))
# print(sum(int(i) for i in re.findall(r'\d+', s)))
#
#
# # class Animal:
# #     def __init__(self, color):
# #         self.color = color
#
# #     def walk(self):
# #         pass
#
#
# # class Horse(Animal):
# #     a = Animal()
# #     a.walk()
#
# #     def __init__(self, color, size):
# #         self.color = color
# #         self.size = size
#
# #     def eat(self):
# #         pass
#
#
# # class Mare(Horse, Animal):
# #     h = Horse()
# #     print(h.__dict__)
#
# #     h.eat()
#
#
# # m = Mare()
# # print(m__dict__)
#
#
# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
#
# @positive
# def diff(a, b):
#     return a - b
#
#
# print(diff(1, 2))
#
# # s = 'Vishwas'
# # s[1] = 'g'
# l = [1, 2, 3]
#
# print(l)
# l[1] = 1000
# print(l)
#
#
# # def isprime(n):
# #     for i in range(2, n):
# #         if n % i == 0:
# #             # continue
# #             print('Something')
# #             pass
# #             # break
# #             return False
# #         elif:
# #             pass
# #         elif:
# #             pass
# #         else:
# #         print('Something')
# #     return True
#
#
# def some():
#     for i in range(1, 11):
#         if i == 1:
#             pass
#             print('vis')
#         print('yes')
#         print(i)
#
#
# some()
#
#
# def fact(n):
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * fact(n - 1)
#
#
# print(fact(5))


