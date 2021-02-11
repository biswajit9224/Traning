# class Employee:
#     def __init__(self, fname, lname, pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay

#         def eamil(self):
#             return f'{self.fname}.{self.lname}@gmail.com'

#         def hike(self, percent):
#             self.pay += (self.pay*percent)

# e1 = Employee('biswajit', 'dash', '20000')
# print(e1.__dict__)
# print(Employee.__dict__)
# print(e1.__class__.__dict__)
# e1.language = 'python'
# print(e1.__dict__)

# class Company:
#     def __init__(self):
#         self._employees = []

#     def add_employee(self, name, gender, team, pay):
#         self._employees.append((name,gender,team,pay))

#     def total_salary(self):
#         return sum([float(reciord[3]) for record in self._employees])

#     def count_by_gender(self):
#         d = defaultdict(int)
#         for record in self._employees:
#             d[record[1]]+=1
#         return d

# def read_csv(filename):
#     with open(filename)as f:
#         c = Company()
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             c.add_employee(row[0], row[1], row[2], row[3])
#         return c

# msft = read_csv('vjbnb/w,iowh/')
# apple = read_csv('fmf/rgm')

# class Covid:
#     def __init__(self):
#         self._employees = []

#     def add_employee(self, name, gender, team, pay):
#         self._employees.append((name,gender,team,pay))

#     def total_salary(self):
#         return sum([float(reciord[3]) for record in self._employees])

#     def count_by_gender(self):
#         d = defaultdict(int)
#         for record in self._employees:
#             d[record[1]]+=1
#         return d

# def read_csv(filename):
#     with open(filename)as f:
#         c = Company()
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             c.add_employee(row[0], row[1], row[2], row[3])
#         return c

# msft = read_csv('vjbnb/w,iowh/')
# apple = read_csv('fmf/rgm')

def insufficient_balance():
    return "insufficient_balance"


# class Bank:
#     def __init__(self, name, amount):
#         self.name = name
#         self.amount = amount
#
#     def deposite(self, deposite_amount):
#         self.amount += deposite_amount
#         return f"deposite sucessfully with {deposite_amount} now balance {self.amount}"
#
#     def widraw(self, widraw_amount):
#         if widraw_amount>self.amount:
#             return insufficient_balance()
#         else:
#             self.amount-=widraw_amount
#             return self.amount
#
#     def check_balance(self):
#         return self.amount
#
# obj_1 = Bank('Biswajit',1000)
# print(obj_1.__dict__)
# print(Bank.__dict__)
# print(obj_1.check_balance())
# print(obj_1.deposite(1000))
# print(obj_1.check_balance())
# print(obj_1.widraw(100))
# print(obj_1.check_balance())
# print(obj_1.widraw(1901))
# print(obj_1.check_balance())


# inheritance of class
class Parent:
    def __init__(self,name):
        self.name = name

    def message(self):
        print('Parent.message')

class Child_1(Parent):

    def message(self):
        print('Child_1.message')

class Child_2(Parent):

    def message(self):
        return 'Child_2.message'

    def same(self):
        return 1+1

class Child_3(Parent,Child_2):

    def message(self):
        # print('Child_3.message')
        return super().message()

obj = Child_3('name')
print(obj.message())
class Parent:
    print("excuting parent")
    def spam(self):
        print('Parent Spam')
        yield
        print("after spam of parent")
class Child2(Parent):
    print("excuting child2")
    def spam(self):
        print('Child2.Spam')
        yield
        print("after spam of Child2")
        # super().spam()

class Child1(Parent):
    print("excuting child1")
    def spam(self):
        print('Child1.Spam')
        yield
        print("after spam of child1")
        # super().spam()

class Child3(Parent):
    print("excuting child3")
    def spam(self):
        print('Child3.Spam')
        yield
        print("after spam of child3")

class Child4(Child2, Child3, Child1):
    print("excuting child4")
    def spam(self):
        print('Child4.Spam')
        # super(Child4, self).spam()
        super(Child2, self).spam()
        yield
        print("after spam of child4")
obj = Child4()
data = obj.spam()
# for i in data:
#     print(i)


# import csv
# record = []
# types = [str, int, int, str]
# with open('D:/python_practice/traning/csv_file/employee.csv')as e:
#     file_object = csv.reader(e)
#     next(file_object)
#     print(type(file_object))
#     for row in file_object:
#         each = [func(item) for func,item in zip(types, row)]
#         print(each)
# class TableFormatter:  # Acts as a design specification
#     def headings(self, headers):
#         raise NotImplementedError
#
#     def rows(self, row):
#         raise NotImplementedError
#
#
# class TextTableFormatter(TableFormatter):
#     def __init__(self, width=10):
#         self.width = width
#
#     def headings(self, headers):
#         for header in headers:
#             print(f'{header:>{self.width}}', end='')
#         print()
#
#     def rows(self, row):
#         for item in row:
#             print(f'{item:>{self.width}}', end='')
#         print()
#
#
# class CSVTableFormatter(TableFormatter):
#     def headings(self, headers):
#         print(','.join(headers))
#
#     def rows(self, row):
#         print(','.join(row))
#
#
# class HTMLFormatter(TableFormatter):
#     def headings(self, headers):
#         print('<tr>', end='')
#         for header in headers:
#             print(f'<th>{header}</th>', end='')
#         print('</tr>')
#
#     def rows(self, row):
#         print('<tr>', end='')
#         for item in row:
#             print(f'<td>{item}</td>', end='')
#         print('<tr>')
#
#
# class Quoted:
#     def rows(self, row):
#         r = [f'"{item}"' for item in row]
#         super().rows(r)
#
#
# class QuotedFormatter(Quoted, TextTableFormatter):
#     pass
#
#
# text = TextTableFormatter()
# _csv = CSVTableFormatter(1)
# a = QuotedFormatter()
# html = HTMLFormatter()
# print_table(data, ['Country', 'Cases', 'Per_million'], text)

# class Propoties:
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
#
#     @property
#     def setter_(self):
#         return self._name
#
#     @setter_.setter
#     def setter_(self, reset_name):
#         if not isinstance(reset_name,str):
#             raise TabError("name should be string")
#         elif len(reset_name)>5:
#             raise TypeError("length of name must be 8 characters")
#         self.name = reset_name
#
#
# obj = Propoties('kanha', 1000)
# print(obj.setter_())
# print(obj.__dict__)
# print(Propoties.__dict__)

# Setters and Getters
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#         # By setting self.first_name , the set operation uses the setter method to set the
#         # first_name attribute as opposed to bypassing it by accessing self._first_name
#
#     @property
#     def first_name(self):
#         print("Setting first_name to property")
#         return self._first_name
#
#     # @first_name.getter
#     # def first_name(self):
#     #     print("Getting value")
#     #     return self._first_name
#
#     @first_name.setter
#     def first_name(self, value):
#         print(f"Setting value for first_name to {value}")
#         if not isinstance(value, str):
#             raise TypeError('First Name must be String')
#         elif len(value) < 12:
#             raise ValueError('First Name must be less than 13 characters')
#         self._first_name = value
#
#     # Deleter function (optional)
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")
#
#
# p1 = Person('Steve', 'Jobs', 30)
#
# print(p1.first_name)
# p1.first_name = 'Bill'
# print(p1.first_name)
# # del p1.first_name


# class point:
#     pass
# obj = point
# print(obj.__dict__)
# print(point.__dict__)
#
# class Point:
#
#     def __init__(self, a, b,same):
#         self.a = a
#         self.b = b
#         self._points = (a, b)
#         self.same = same
#
#     # String representation of Point Object
#     def __str__(self):
#         print('Running __str__')
#         return f"({self.a},{self.b})"
#
#     # Implementing length of the Point Object
#     def __len__(self):
#         print('Running __len__')
#         return len(self._points)
#
#     # Making an object iterable
#     def __iter__(self):
#         print('Running __iter__')
#         return iter(self._points)
#
#     # Implementing membership operator
#     def __contains__(self, item):
#         print('Running __contains__')
#         return item in self._points
#
#     # Making an object indexable!
#     def __getitem__(self, item):
#         print('Running __getitem__')
#         return self._points[item]
#
#     # Restricting adding new attribute to the class (Making Class Immutable)
#     # Override __setattr__ method of object class.
#     def __setattr__(self, name, value):
#         print('Running __setattr__')
#         if name not in {"a", "b", "_points","same"}:
#             raise AttributeError(f"Cannot Add new Attribute {name}")
#         super().__setattr__(name, value)
#
#     # Restricting someone from deleting the attribute.
#     # Override __delattr__ method of object class.
#     def __delattr__(self, name):
#         print('Running __delattr__')
#         raise AttributeError('Cannot Delete Attribute {}'.format(name))
#
#     # Checks if two Point objects are equal
#     def __eq__(self, other):
#         print('Running __eq__')
#         return self._points == other._points
#
#     # Checks if the first Point object is greater than second Point Object
#     def __gt__(self, other):
#         print('Running __gt__')
#         return sum(self._points) > sum(other.points)
#
#     # Checks if the first Point object is less than second Point Object
#     def __lt__(self, other):
#         print('Running __lt__')
#         return sum(self._points) < sum(other._points)
#
#     # Adds two Point Objects
#     def __add__(self, other):
#         print('Running __add__')
#         return sum(self._points) + sum(other._points)
#
#     # Subtracts two Point Objects
#     def __sub__(self, other):
#         print('Running __sub__')
#         return sum(self._points) - sum(other._points)
# obj = Point(1,2,4)

# class Point_:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __len__(self):
#         return len(self.a)+len(self.b)
#     def __iter__(self):
#         return iter(self.a)
#
# point_object_ = Point_('Biswajit','kanha')
# print(len(point_object_))
# # print('j' in point_object_)
