##from traning_1 import *
##data(10, 3)


from collections import defaultdict, Counter
import csv

with open('D:/csv_file/employee.csv') as e:
    data = []
    row = csv.reader(e)
    next(row)
    for i in row:
        data.append({'name': i[0], 'id': i[1], 'pay': i[2], 'gender': i[3]})

d = defaultdict(list)


##for i in data:
##d['total_sal']+=int(i.get('pay'))

##d = sum([int(i.get('pay')) for i in data])
##print(d)

##for i in data:
##    d[i['gender']]+=1
##    if i['gender'] in d:
##        d[i['gender']]+=1
##    else:
##        d[i['gender']] = 1

##print(d)
##c = Counter()
##for d1 in data:
##    c[d1['gender']]+=1
##print(c)

def each(i):
    return i.get('name')


# sorting employee record by name
##sort_name = sorted(data, key = each)
##print(sort_name)

##unic_data = {i.get('gender') for i in data}
##print(unic_data)

##for i in data:
##    d[i['gender']].append(i.get('name'))

d1 = {i['name']: i['pay'] for i in data if int(i['pay']) > 20000}

# decorator example starting here
import time


def delay(func, _time, *args, **kwargs):
    print(args)
    print(kwargs)
    time.sleep(_time)
    return func(*args, **kwargs)


def outer(func):
    def inner(*args, **kwargs):
        print('you are calling:', func.__name__)
        data = func(*args, **kwargs)
        print('after calling decorated')
        return data

    return inner


def greet():
    print('hello world')


def greeting(name):
    print('hello', name)


def add(a, b):
    print(a + b)


def mul(a, b, c):
    return a * b * c
