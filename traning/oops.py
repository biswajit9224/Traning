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
# from collections import defaultdict
# class Employee:
#     def __init__(self):
#         self.data_list = []
#     def add_data(self,data):
#         self.data_list.append(data)

#     def total_salary(self):
#         totalsal_ = defaultdict(int)
#         for each in self.data_list:
#             totalsal_['pay']+=each['pay']
#         return totalsal_


# with open("csv_file/employee.csv")as file_object:
#     header = next(file_object).split(',')
#     obj = Employee()
#     for each in file_object:
#         each = each.split(',')
#         obj.add_data({header[0]:each[0], header[1]:each[1], header[2]:int(each[2]), header[3]:each[3]})

# print(obj.total_salary())
        

# class BankAccount:
#     _interest = 4.0

#     def deposit(self, amount):
#         print('Depositing Amount:', amount)

#     def withdraw(self, amount):
#         print('Withdrawing Amount:', amount)

#     def roi(self):
#         print("ROI is:", self.__interest)


# class SavingsAccount:
#     __interest = 4.5
#     _interest=__interest+2.5     # Does Not Override __interest of Parent Class
# obj = SavingsAccount()
# print(SavingsAccount._interest)
# print(SavingsAccount._SavingsAccount__interest)
# print(SavingsAccount.__dict__)


# class Register():
#     def register_(self):
#         chrome_driver.find_element_by_xpath("//a[.='Register']").click()
#
#     sleep(3)
#
#     def radio_gender(self):
#         chrome_driver.find_element_by_xpath("//div[@class='gender']//input[@id='gender-male']").click()
#
#     sleep(2)
#
#     def first_name(self):
#         chrome_driver.find_element_by_id("FirstName").send_keys("biswajit_")
#
#     sleep(2)
#
#     def last_name(self):
#         chrome_driver.find_element_by_id("LastName").send_keys("Dash")
#
#     sleep(2)
#
#     def email(self):
#         chrome_driver.find_element_by_id("Email").send_keys("haiihow@gmail.com")
#
#     sleep(2)
#
#     def password(self):
#         chrome_driver.find_element_by_xpath("(//input[@class = 'text-box single-line password'])[1]").send_keys(
#             "kanha@1997")
#
#     sleep(2)
#
#     def repassword(self):
#         chrome_driver.find_element_by_xpath("(//input[@class = 'text-box single-line password'])[2]").send_keys(
#             "kanha@1997")
#
#     sleep(2)
#
#     def register(self):
#         chrome_driver.find_element_by_xpath("//input[@id='register-button']").click()
#
#     sleep(2)

# class parent:
#     def spam(self):
#         print('parent.spam')
#
# class child1(parent):
#     pass
#     # def spam(self):
#     #     print('child1.spam')
#
# class child2(parent):
#     def spam(self):
#         print('child2.spam')
#
# class child3(child1,child2):
#     def spam(self):
#         print('child3.spam')
#         super().spam()
#
# obj = child3()
# obj.spam()
