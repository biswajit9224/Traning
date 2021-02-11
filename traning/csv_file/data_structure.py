from collections import namedtuple
from dataclasses import dataclass

def make_tuple(row):
    return (row[0], row[1], row[2], row[3])


def make_dict(row):
    return {

            "name":row[0]
            "gender":row[1]
            "team":row[2]
            "pay":row[3]

    }

record = namedtuple("record", ['name', 'gender', 'team', 'pay'])

def make_named_tuple(row):
    return record(row[0], row[1], row[2], row[3])




class Employee:
    def __init__(self,'name', 'gender', 'team', 'pay'):
        self.name = name
        self.gender = gender
        self.team = team
        self.pay = pay

def make_class(row):
    return Employee(row[0], row[1], row[2], row[3])




@dataclass
class D_Employee:
    name:str
    gender:str
    team:str
    pay: float

def make_data_class(row):
    return D_Employee(row[0], row[1], row[2], row[3])




def read_csv():
    recordes = []
    with open('file_name') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rows in rows:
            recordes.append(func(row))
    return recordes

data = read_csv(make_data_clas)















# l = [1, 2]

# t = (1, 2)

# d = {"a":1, "b":2}
# s = {1, 2}

# np = namedtuple("np", ['a', 'b'])
# p = np(5, 2)
# print(p.a)

# class Point:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# p1 = Point(1,2)
# p2 = Point(13,4)

# @dataclass
# class d_point:
#     a: int
#     b: int
# dp = d_point(10,2)
# ds = d_point(10, 4.4)
# print(dp.a)
# print(type(ds.b))
