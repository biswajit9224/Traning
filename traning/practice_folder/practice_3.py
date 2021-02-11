# class Employee:
#     employee_list = []
#     def __init__(self, name):
#         self.name = name


# class Weekly_employee(Employee):
#     count_ = 0
#     def __init__(self, per_week_pay, total_week_work,name):
#         self.per_week_pay = per_week_pay
#         self.total_week_work = total_week_work
#         super().__init__(name)
        
#     def axcess_employ_list(self):
#         Weekly_employee.count_+=1
#         Employee.employee_list.append({'weekly_employee_data':{'name':self.name, 'per_week_pay':self.per_week_pay, 'total_week_work':self.total_week_work}})
#         return Employee.employee_list

# obj_Weekly_employee = Weekly_employee(1000,5,'Biswajit_Dash')
# obj_Weekly_employee_2 = Weekly_employee(1100,5,'Stitipragyna_Dash')
# # print(obj_Weekly_employee.per_week_pay)
# obj_Weekly_employee.axcess_employ_list()
# obj_Weekly_employee_2.axcess_employ_list()
# # print(Weekly_employee.__dict__)
# # print(obj_Weekly_employee.__dict__)
# print(Employee.employee_list)


class Employee:
    
    def __init__(self,name,gender,pay,id_):
        self.name = name
        self.gender = gender
        self.pay = pay
        self.id_ = id_

    def count_employee(self):
        return 




