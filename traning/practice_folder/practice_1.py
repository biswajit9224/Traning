import copy
import re
import csv
from collections import defaultdict
# a = [1,2,3,[1,2]]
# b = copy.copy(a)


# a.append([3])



# print(a, id(a[0]))
# print(b, id(b[0]))

# import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)

# old_list[1][0] = 'BB'
# # old_list.append([1,2])
# old_list.pop([0][0])
# print("Old list:", old_list)
# print("New list:", new_list)


# old_list1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list1 = copy.copy(old_list1)

# old_list1[1][1] = 'AA'
# old_list1.append([1,2])
# print("Old list:", old_list1)
# print("New list:", new_list1)



















# import csv
# l1 = []
# def data_collect(l1):
#     # global l1
#     with open('csv_file/errors.log') as file_object:
#         print(file_object)
#         for i in file_object:
#             if 'INFO' in i:
#                 # print(i)
#                 i = i.split('-')
#                 # print(i)
#                 l1.append(i[-1])
#                 # print(l1[-1])
#         # print(l1)

# data_collect(l1)
# for j in l1:
#     print(j)

# l1 = []

# def data1(l1):
#     for i in range(5):
#         l1.append(i)
#         yield i
# print(data1(l1))
# d = data1(l1)
# print(next(d))
# for i in d:
#     print(i)



# _links = ['https://www.python.org',
#           'https://www.google.com',
#           'https://www.facebook.com',
#           'https://www.youtube.com',
#           'http://www.amazon.com.us'
#           ]
# match_links = r'\.[a-z]+'

# for link in _links:
#     matches = re.findall(match_links, link)
#     if matches:
#         print(matches)
#     # for match in matches:
#     #     print(match[1:-1])


# d = defaultdict(int)
# with open('csv_file/covid_dat2.csv')as e:
#     print(e)
#     next(e)
#     l = []
#     for i in e:
#         i = i.split(',')
#         l.append({'country':i[2], 'date':i[3], 'total_case':i[4], 'new_case':i[5]})
# print(len(l))
# for j in l:
#     if j['country'] == 'India' and j['date'][5:7] == '03':
#         d[j['date']]=j['total_case']
#         d[j['date']+'_new']=j['new_case']

# print(d)

 

#   l = [3,9,21,4,77,42,8,55,10,33,7]
# class Even:
#     def __init__(self,l):
#         self.l = l
#     def tuple_1(self):
#         _tupl_1 = sorted([i for i in self.l if i<25 and i%2!=0])
#         return tuple(_tupl_1)
#     def tuple_2(self):
#         _tupl_2 = sorted([i for i in self.l if i>25 and i%2!=0])
#         return tuple(_tupl_2)
# tupl = Even([3,9,21,4,77,42,8,55,10,33,7])
# print(tupl.tuple_1())
# print(tupl.tuple_2())
# t = (1,2,3,2,78,34)
# d = (sorted(t))
# print(d)
# print(type(d))
import re
_string = '''   Dictionary in Python is an unordered collection of data values that 
are used to store data values like a map. Unlike other Data Types that hold
only single value as an element, the Dictionary holds key:value pair.
In Dictionary, the key must be unique and immutable. This means that 
a Python Tuple can be a key whereas a Python List can not. 
A Dictionary can be created by placing a sequence of elements 
within curly {} braces, separated by ‘comma’.'''
serching = 'Dictionary'

# data = re.sub(serching,'dict',_string, 0)
# print(data)


# print(len(_string))

# serching = 'Dictionary'
# c = 0
# d = 0
# _string = _string.split()
# print(_string)
# for index in range(len(_string)):
#     d+=len(_string[index])
#     if _string[index] == 'Dictionary':
#         c += 1
#         if c == 1:
#             print(index)
#             print(d-len(serching))
#             break

# data = re.finditer(serching, _string)
# print(data)
# count = 0
# for i in data:
#     count+=1
#     if count == 3:
#         start = i.start()
#         end = i.end()
#         data_1 = _string[start:end+1]
#         print(data_1)
#         _string = _string.replace(data_1, 'dict')
# print(_string)

