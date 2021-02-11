from collections import namedtuple
import csv 

def make_tuple(i):
    return (i[0], i[1], i[2], i[3])


record = namedtuple("record", ['name', 'id', 'pay', 'gender'])


def named_tuple(i):
    return record(i[0], i[1], i[2], i[3])


class Employee:
    def __init__(self, name, id, pay, gender):
        self.name = name
        self.id = id
        self.pay = pay
        self.gender = gender


def _class(i):
    return Employee(i[0], i[1], i[2], i[3])


def _csvread():
    records = []
    with open ('csv_file/employee.csv') as e:
        lines = csv.reader(e)
        header = next(lines)
        for i in lines:
            records.append(_class(i))
    return records
d = (_csvread())
for j in d:
    print(j)

 
