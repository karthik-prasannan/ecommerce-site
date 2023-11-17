#1) encapsulation is one of the fundamental concept in oops
#2) it describes the idea of wrapping data and the methods
#3) this puts restrictions on accessing variables and method directly
#4) it can prevent the accidental modification of data

# in object oriented programming access modifiers are used to limit the access to the variable and functions of a class

# *)public access mmodifiers:accessible anywhere from outside the class
# *)
# *)
# *)

# syntax

# class employee:
#     def __init__(self,name,project,salary):
#         self.name=name        #(public member)
#         self._project=project #(protected member)
#         self.__salary=salary  #(private member)

# class employee:
#     def __init__(self,name,salary):
#         #public data members
#         self.name=name
#         self.salary=salary
#     def fun(self): #public function
#         print('name = ',self.name,'salary = ',self.salary)
# emp=employee('jessa',10000)
# print('Name = ',emp.name,'Salary = ',emp.salary)
# emp.fun()

# student , name , roll , school

# class student:
#     def __init__(self,name,roll,school):
#         self.name=name
#         self.roll=roll
#         self.school=school
#     def fun(self):
#         print('name = ',self.name)
#         print('roll = ',self.roll)
#         print('school = ',self.school)
# obj=student('karthik',10,'unity school')
# print('NAME= ',obj.name,'ROLL= ',obj.roll,'SCHOOL= ',obj.school)
# obj.fun()