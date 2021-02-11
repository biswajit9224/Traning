from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
# chrome_driver= webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
# ('xpath',"//select[@id='standard_cars']")
# chrome_driver.get(r'file:///D:/python_practice/traning/selenium/html_files/standard_listbox.html')
# chrome_driver.get("https://www.naukri.com/")
# chrome_driver.get(r"file:///D:/python_practice/traning/selenium/html_files/javascriptallert.html")
# chrome_driver.maximize_window()
# sleep(5)
# chrome_driver.implicitly_wait(10)
# windows_ = chrome_driver.window_handles
# chrome_driver.find_element('xpath',"//button[.='Try it']").click()
# chrome_driver.switch_to.alert.dismiss()
# for i in windows_:
#     chrome_driver.switch_to_window(i)
#     # sleep(2)
#     # amazon = chrome_driver.title.upper() == 'AMAZON'
#     # if amazon:
#     chrome_driver.close()

# chrome_driver.save_screenshot()
# elements = chrome_driver.find_element_by_xpath("(//div[@class='custom-select'])[1]")
# element = chrome_driver.find_element_by_id("standard_cars")
# for i in elements:
#     print(i.text)
# s = Select(element)
# options_ = s.options
#
# items = [item.text for item in options_]
#
# for item in items:
#     s.select_by_visible_text(item)
#     sleep(1)
# element = chrome_driver.find_element_by_id('dd')
# s = Select(element)
# # time.sleep(2)
# # s.select_by_visible_text('audi')
# # time.sleep(2)
# # s.select_by_visible_text('honda')
# # time.sleep(2)
#
#
# # o
#ptionss = s.options
# # for index in range(1,len(optionss)):
# #     s.select_by_index(index)
# #     time.sleep(1)
#
# # items = []
# # for i in optionss:          #or items = [i.text for i in optionss]
# #     items.append(i.text)
#
#
# # for item in items:
# #     s.select_by_visible_text(item)
# #     time.sleep(1)
#
#
# # for index,item in enumerate(items):
# #     if 'honda' ==item:
# #         s.select_by_visible_text(item)
# #         print(index,item)
#
# # __________________multiselect_________________
#
# # s.select_by_visible_text('honda')
# # time.sleep(1)
# # s.select_by_visible_text('ford')
# # time.sleep(1)
# # s.select_by_visible_text('audi')
# # time.sleep(1)
# # s.select_by_visible_text('hyundai')
# # time.sleep(1)

# # items = ['honda','ford','audi', 'maruti','hyundai']
# # for item in items:
# #     try:
# #         s.select_by_visible_text(item)
# #         time.sleep(1.5)
# #     except Exception as e:
# #         print(e)
#
#
#
# class spam:
#     def __init__(self):
#         pass
#     def __call__(self):
#         print('hai')
# c = spam()
# c()

# def change(file_path,previousdata,newdata):
#     with open(file_path)as e:
#         for i in e:
#             if previousdata in i:
#                 d=i.replace(previousdata,newdata)
#
#
#
#
#
# change("D:/1.txt",'kanha','kanhu')
# import fileinput
#
# def change(file_path, text_to_search,replacement_text):
#     with fileinput.FileInput(file_path,inplace=True,backup='.bak')as e:
#         for line in e:
#             print(line.replace(text_to_search,replacement_text))
#
# change("D:/1.txt",'kanhu','kanhu_')

# d = (i for i in range(10))
# l = [i for i in range(10)]
# s = {i for i in range(10)}
# print(d)
# for i in d:
#     print(i)
# print(f"l is a {type(l)}    {l}")
# print(f"l is a {type(s)}    {s}")

# t = (10,20)
# for i in range(10):
#     t = t+(i,)
# print(t)
import time
# def wait_(wait_time):
#     def _time(func):
#         def wrapper(*args, **kwargs):
#             start = time.time()
#             result = func(*args, **kwargs)
#             end = time.time()
#             print(f'Exe Time for {func.__name__} : {end-start}')
#             time.sleep(wait_time)
#             return result
#         return wrapper
#     return _time
#
# @wait_(5)
# def wait():
#     return 5
# print(wait())

# def type_check(exp_types, actual_values):
#     for _type, _value in zip(exp_types, actual_values):
#         if not isinstance(_value, _type):
#             raise TypeError
#
#
# # Decorator to Type Check.
# def validate(**typs):
#     def _validate(func):
#         def wrapper(*args, **kwargs):
#             _expected_types = list(typs.values())
#             _actual_values = list(args)
#             type_check(_expected_types, _actual_values)
#             return func(*args, **kwargs)
#         return wrapper
#     return _validate
#
# @validate(a=int,b=int)
# def typo(a,b):
#     return a+b
# print(typo(19,2))

# def check(actuall_data,requierd_data):
#     for value,type in zip(actuall_data,requierd_data):
#         if not isinstance(value,type):
#             raise TypeError
#
#
#
# def outer_(**type_):
#     def outer(func):
#         def inner(*args,**kwargs_):
#             actuall_data = list(kwargs_.values())
#             requierd_data = list(type_.values())
#             print(actuall_data,requierd_data)
#             check(actuall_data,requierd_data)
#             return func(*args,**kwargs_)
#
#         return inner
#     return outer
#
#
# @outer_(a=float,b=int)
# def add(a,b):
#     return a+b
#
# print(add(b=2.6,a=4))








