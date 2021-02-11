# from selenium import webdriver
#
# driver_ = webdriver.Chrome(r"C:\Users\91824\Downloads\Compressed\chromedriver_win32\chromedriver")
# driver_.get('http://www.google.com')


# def _convert(string_):
#     l=[]
#     for _each in string_:
#         temp = ord(_each)
#         if temp>=65 and temp<=95:
#             l.append(chr(temp+32))
#         elif temp>=95 and temp<=122:
#             l.append(chr(temp-32))
#         else:
#             l.append(_each)
#     return ''.join(l)
# print(_convert('PyTh./@#On'))


# l = ["hi", "there", "how", "is", "it", "going",]
# print([i for i in l if len(i)%2==0])
#
#
# def contains_twice(string_,c):
#     if string_.count(c)>=2:
#         return True
#     else:
#         return False
# print(contains_twice('hello','o'))
#
# def repeat_string(_string,c):
#     return _string*c if c>0 else ''
# print(repeat_string('kanha', 0))
#
# def get_last_digit(number):
#     return str(number)[-1]
# print(get_last_digit(123))

# list_nums = [1, 2, 3, 1, 3, 5, 4, 3, 3, 1, 1, 1, 1]
# def count_(list_nums):
#     d = sorted({item_:list_nums.count(item_) for item_ in list_nums}.items(),key=lambda each_:each_[1])
#     d1 = {}
#     for i in reversed(d):
#         d1.setdefault(i[0],i[1])
#     return d1
# print(count_('hello'))
#
# from collections import Counter
# c = Counter(list_nums)
# print(c)
#
# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
# print(reverse('hello'))

#
# print([(x, y) for x in range(5) for y in range(5)])
# data = [1, 1.2, 'hello', len, True, (1, 2, 3), {9, 8, 6}, ['apple', 'ibm', 'yahoo']]
# print({type(item): data for item in data})

# def count_(num):
#     # print('start')
#     # while num>0:
#     for i in range(num,0,-1):
#         yield i
#
#     # print('Done')
# # for i in count_(5):
# #     print(i)
# d = count_(5)
# print(d)
# for j in d:
#     print(j)









