import collections as col
# # find the length of string without using len
# # one way
# def st():
#     count1 = 0
#     for i in 'string':
#         count1+=1
#     return count1
# print(st())

# #another way
# def st():
#     d = col.defaultdict(int)
#     for i in 'stringi':
#         d[i]+=1
#     length_ = 0
#     for j in d.values():
#         length_+=j
#     return length_
# print(st())

# # Write a program to reverse a string without using any inbuilt functions.

# def re_str(str_1):
#     l_1 = []
#     for i in range(len(str_1)-1,-1,-1):
#         l_1.append(str_1[i])
#     return ''.join(l_1)
# print(re_str('kanha'))

# # Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".

# str_2 = "Hello World"
# str_2 = str_2.replace('World','Universe')
# print(str_2)

# # How to convert a string to a list and vice-versa.
# def con_str_lis():
#     str_3 = 'data'
#     str3 = list(str_3)
#     return str3

# def con_lis_str():
#     str_3 = con_str_lis()
#     print(str_3)
#     str3 = ''.join(str_3)
#     print(str3)
    
# con_lis_str()

# Covert the string "Hello welcome to Python" to a comma separated string.
# str_0 = "Hello welcome to Python"

# one way

# data = str_0.replace(' ',',')
# print(type(data))

# anathor way

# data = str_0.split()
# data = ','.join(data)
# print(data)

# Write a program to print alternate characters in a string.

# str_0 = 'Write program'
# print(str_0[::2])

# Write a Program to print ascii values of the characters present in a string

# str_0 = 'Write program'
# for i in str_0:
#     print(ord(i))

# Write program to convert upper case to lower case and vice-versa without using inbuilt method.

# str_0 = 'Write program'
# l = []
# for i in str_0:
#     if i.isupper():
#         i_ = i.lower()
#         l.append(i.replace(i,i_))
#     elif i.islower():
#         i_ = i.upper()
#         l.append(i.replace(i,i_))
#     # else:
#     #     continue
# print(''.join(l))

# d = {1:1,2:2}
# d_ = {23:1,3:2, 234:232}
# l = [1,2,3]
# l_ = [2,3]
# print([*l,*l_])
# print({**d,**d_})

# def askii(string1):
#     l = []
#     for i in string1:
#         temp = ord(i)
#         print(temp)
#         if temp>=97 and temp<=122:
#             l.append(chr(temp-32))
#         elif temp<=90 and temp>=65:
#             l.append(chr(temp+32))
#         else:
#             continue
#     return ''.join(l)
# print(askii('AajdsHje'))

# s = 'python is a programming language and it is a object orieanted programm'
d = col.defaultdict(int)
# s = list(s)
# for word in s:
#     d[word].append(word)
# print(len(d[' ']))
# sentence = "python is a programming language"
# d = {'p':['python', 'programming'] , 'i': ['is'] , 'a': ['a'] , 'l' : ['language'] }
# s = sentence.split()
# for word in s:
#     d[word[0]]+=1
# print(d)

# s = 'helloworld'
# s1 = set(s)
# for i in s1:
#     if s.count(i)>1:
#        s = s.replace(i,'-')
# print(s)

# my_string = 'hellohai' # O/P should be '-e--o-ai'

# my_string = 'heallohai'

# # Get all the unique characters
# ss = set(my_string)

# for ch in ss:
#     if my_string.count(ch) > 1:
#         my_string = my_string.replace(ch, '-')

# print(my_string)

# def outer(func):
#     def wrapper(*args):
#         data = func(*args)
#         print(abs(data))
#     return wrapper

# @outer
# def sub(a,b):
#     print(a-b)
# print(sub(2,3))


# l = ['hello',1,2,223,2,3221]
# d = [i if isinstance(i,str) else str(i)[::-1] for i in l]
# print(d)

# class Simple:
#     def __init__(self, items):
#         self._items = items

#     def __iter__(self):
#         return iter(self._items)


# class Check:
#     def __init__(self, file):
#         self.file = file
    
#     # def __iter__(self,)

#     def data1(self, index):
#         ___file = self.file.readlines()
#         # for i in ___file:
#         return ___file[index]


# with open('csv_file/employee.csv') as e:
#     d = Check(e)
#     print(d.data1(-1))

# st = "python is a programming language"
# d={}
# for i in st.split():
#     if i[0] in d:
#         d[i[0]].append(i)
#     else:
#         d[i[0]]=[]
#         d[i[0]].append(i)
# print(d)

# st = "python is a programming language" #o/p will be '_yth____s_______________l___u__e'
# s = set(st)
# print(s)
# for i in s:
#     if st.count(i)>=2:
#         st = st.replace(i,'_')
# print(st)

# class Count:
#     counting = 0
#     def __init__(self):
#         Count.counting+=1
# d1 = Count()
# d2 = Count()
# print(Count.counting)

# def lis_str_(data):
#     data1 = [i if isinstance(i,str) else float(str(i)[::-1]) for i in data]
#     # return ''.join(data1)
#     return data1
# print(lis_str_(['string', 'integer', 'float',2,234,453]))

# class iter_:
#     def __init__(self,object_):
#         self.object_ = object_
    
#     def __iter__(self):
#         return iter(self.object_)


    # def __iter__(self):
    #     for i in self.object_:
    #         print(i)

# with open('csv_file/employee.csv') as e:
# c = iter_([1,2,3,4])
# for i in c:
#     print(i)

# print(iter_.__dict__)

# from difflib import get_close_matches
# if __name__=='__main__':
#     t = ["eat", "tea",'tan', 'ate','nat', 'bat']
#     t_l = [[],[],[],]
#     for i in t:
#         if 'e' and 'a' and 't' in i:
#             t_l[-1].insert(0,i)
#         elif 'a' and 'n' and 't' in i:
#             t_l[-2].insert(0,i)
#         elif 'a' and 'b' and 't' in i:
#             t_l[-3].insert(0,i)

#     print(t_l)


# # Python program to print all words that 
# # have the same unique character set 

# # Function to group all strings with same characters 
# from collections import Counter 

# def groupStrings(input): 
# 	# traverse all strings one by one 
# 	# dict is an empty dictionary 
# 	dict={} 
	
# 	for word in input: 
# 		# sort the current string and take it's 
# 		# sorted value as key 
# 		# sorted return list of sorted characters 
# 		# we need to join them to get key as string 
# 		# Counter() method returns dictionary with frequency of 
# 		# each character as value 
# 		wordDict=Counter(word) 

# 		# now get list of keys 
# 		key = wordDict.keys() 

# 		# now sort these keys 
# 		key = sorted(key) 

# 		# join these characters to produce key string 
# 		key = ''.join(key) 
		
# 		# now check if this key already exist in 
# 		# dictionary or not 
# 		# if exist then simply append current word 
# 		# in mapped list on key 
# 		# otherwise first assign empty list to key and 
# 		# then append current word in it 
# 		if key in dict.keys(): 
# 			dict[key].append(word) 
# 		else: 
# 			dict[key]=[] 
# 			dict[key].append(word) 

# 		# now traverse complete dictionary and print 
# 		# list of mapped strings in each key seprated by , 
# 	for (key,value) in dict.iteritems(): 
# 		print ','.join(dict[key]) 
		
# # Driver program 
# if __name__ == "__main__": 
# 	input=['may','student','students','dog','studentssess','god','cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle'] 
# 	groupStrings(input) 


# from collections import Counter
# l = [1,2,3,4,54,2,1,'']
# print(Counter(l))
# def check(d_1):
#     d = {}
#     for word in d_1:
#         d2 = Counter(word)
#         key = d2.keys()
#         key = d2
#         key = ''.join(key)
#         if key in d2.keys(): 
#             d2[key].append(word) 
#         else: 
#             d2[key]=[] 
#             d2[key].append(word)
#     print(d2)
#     # for (key,value) in d2.iteritems(): 
#     #     print ','.join(d2[key])




# check(["eat", "tea",'tan', 'ate','nat', 'bat'])




# s = "hai how are u and what are u doing"
# s = s.split()
# get = {word:len(word) for word in s}
# print(max(get.items(), key= lambda item: item[-1]))
from itertools import islice
# def create_read(s):
#     with open('csv_file/test.txt','w') as file_object:
#         data = sorted([i for i in s.split()])
#         for j in data:
#             file_object.write(j+'\n')
#     with open('csv_file/test.txt','r') as file_object:
#         count_ = 0
#         for i in file_object:
#             count_+=1
#         d = islice(file_object, count_-3,count_)
#         for i in d:
#             print(i)

# create_read(s = "hai how are u and what are u doing")

# with open('csv_file/test.txt') as file_object:
#     count_ = 0
#     for i in file_object:
#         count_+=1
#     print(count_)
#     file_object.seek(1)
#     lines = islice(file_object,count_-3,count_)
#     for line in lines:
#         print(line)
# l = ["eat", "tea",'tan', 'ate','nat', 'bat']
# set_l = set([''.join(sorted(i))for i in l])
# op = [[j for j in l if ''.join(sorted(j))==k]for k in set_l]
# print(op)
# print([[j for j in l if k == ''.join(sorted(j))]for k in set([''.join(sorted(i)) for i in l])

# def counting():
#     try:
#         with open('coustom_.log') as file_object:
#             # print(file_object)
#             d = col.defaultdict(int)
#             for i in file_object:
#                 if i.strip():
#                     i = i.split(':')
#                     if i[0] in i:
#                         d[i[0]]+=1
#                     else:
#                         continue
#         return d
#     except Exception as e:
#         print(e)

# print(counting())

# def rev(l,l1):
#     for i in range(len(l)-1,-1,-1):
#         l1.append(l[i])
#     print(l1)
# rev([1,2,3,4,2,4,5,6],[])

# def data_(string_,from_):
#     print(string_[from_::2])
# data_('TRACXN',1)

# s = "Sony12India567Pvt2ltd"
# def adding(s, l):
#     for i in s:
#         if i.isnumeric():
#             l.append(int(i))
#     return sum(l)
# print(adding("Sony12India567Pvt2ltd",[]))
# import re
# def adding(s):
#     data =   re.findall('[\d]+',s)
#     return sum([int(i) for i in data])
# print(adding("Sony12India567Pvt2ltd"))


# def atr(s):
#     se = set(s)
#     for i in se:
#         if s.count(i)>1:
#             print(i.upper(),'=',s.count(i))
# atr('helloworld')

# def data(file_name,n):
#     with open(file_name)as e:
#         data = col.deque(e,n) #it will return n number of lines from end... 
#     return data
# print(data('csv_file/test.txt',3))  

# print(list(map(lambda each:each**2,[k for k in range(1,21)])))

# l_1 = ['apple', 'yahoo', 'google', 'gmail', 'walmart', 'flipkart', 'facebook', 'amazon']
# print([i if len(i)%2 == 0 else i[::-1] for i in l_1])

# def data(file_name):
#     with open(file_name)as e:
#         return len(e.readlines())
# print(data('csv_file/test.txt'))  


# def data(file_name):
#     with open(file_name)as e:
#         for i,j in enumerate(e,start=1):
#             print(f'{i} = {j}')
# print(data('csv_file/test.txt'))  

# l = [[1,2,3],[4,5,6],[7,8,9]]
# sum_inter = [sum(i) for i in l]
# print(sum_inter)
# print(sum(sum_inter))

# t1 = (1, 2, 3, 4)
# t2 = (100, 200, 300)
# # o/p (1, 2, 3, 4, 100, 200, 300)
# t = (*t1,*t2)
# print(t)

# d = {'a': 100, 'b': {'m': 'man', 'n': 'nose', 'o': 'ox', 'c': 'cat'}}
# d['b']['o']='oxigen'
# print(d)
# d = {'a': 'hello', 'b': '100', 'c': '10.1', 'd': 'world'}
# print(sorted(d.items(),key=lambda data: data[1][-1]))

# def coustom_sort(filename):
#     with open(filename)as e:
#         l = []
#         next(e)
#         for i in e:
#             if i.strip():
#                 i=i.split(',')
#                 l.append({'name':i[0],'id':i[1],'pay':i[2],'gender':i[3]})
#     return l
# d = coustom_sort('csv_file/employee.csv')
# print(d)
# sorting_name = sorted(dict(d),key=lambda name:name.get('name'))
# print(sorting_name)

# class sorting
##
##class Employee:
##    def __init__(self,first_name, last_name, sal):
##        self.first_name = first_name
##        self.last_name = last_name
##        self.sal = sal
##
##emp1 = Employee('biswajit','dash',2300)
##emp2 = Employee('stitipragyna','dash',1100)
##emp3 = Employee('payal','swain',2000)
##l = [emp1,emp2,emp3]
##s = sorted(l,key=lambda data:data.first_name)
##for i in s:
##    print(i.first_name)


class Parent:
    def spam(self):
        print('Parent Spam')

class Child1(Parent):
    def spam(self):
        print('Child1.Spam')
##        super().spam()

class Child2(Parent):
    def spam(self):
        print('Child2.Spam')
        super().spam()

class Child3(Child1, Child2):
    pass
obj  = Child3()





