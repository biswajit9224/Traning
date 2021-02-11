# def fun1(a, b):
#    print(f'addition of a and b is {a+b}')
#
# def fun2(a, b):
#    print(f'addition of a and b is {a-b}')

# print('hallo')


# s = "hi how are you"
# s = s.split()
# for i in range(5):
#    print(str(i).zfill(2))

# a = [1,2,3]
# b = [4,5,6]
# d = [2,34,5]
# c = [*a,*b,*d]
# print(c)

d = {"a": 1, "b": 2}
# for key,value in d.items():
#    print(key,value)
# d1 = sorted(d)
# print(d1)
# d1 = {'rg':23, 'de':89}
# d2 = {**d, **d1}
# print(d2.get('a'))

# l1 = [i**i for i in range(1,11)]
# print(l1)
#
# s = "hi how are you"
# l2 = [i.upper() for i in s.split()]
# print(l2)
#
# l3 = [(word,len(word))for word in s.split()]
# print(l3)
#
# l4 = [{word:len(word)} if len(word)%2==0 else word.upper()for word in s.split()]
# print(l4)
#
#
# search = input('enter a string: ')
# with open('D:/python_read.txt') as e:
#     data = e.readlines()
#     print(len(data))
#     print(data)
#     for each_line in data:
#         if search in each_line:
#            print(' '.join([i.replace(i[0], i[0].upper()) for i in each_line.split()]))

from collections import defaultdict

with open('D:/csv_file/employee.csv') as e:
    all_data = []
    next(e)
    for i in e:
        data = i.split(',')
        all_data.append({"name": data[0], "id": data[1], "pay": data[2], "gender": data[3]})
gender = defaultdict(list)

{gender[each['gender']].append(each.get('name')) for each in all_data}
print(gender)
