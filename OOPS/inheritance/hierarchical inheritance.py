# syntax

# class A:
#     def fun1(self):
#         print('class A')
# class B(A):
#     def fun2(self):
#         print('class B')
# class C(A):
#     def fun3(self):
#         print('class C')
# class D(A):
#     def fun4(self):
#         print('class D')
# obj=B()
# obj.fun1()
# obj.fun2()
#
# obj1=C()
# obj1.fun1()
# obj1.fun3()
#
# obj2=D()
# obj2.fun1()
# obj2.fun4()

# without using constructor?

# details : id,name,gender,
# developer : designation,company name
# doctor : hospital,specialization

# class details():
#     def fun1(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#         print('id : ',self.id)
#         print('name : ',self.name)
#         print('gender : ',self.gender)
# class developer(details):
#     def fun2(self,designation,company_name):
#         self.designation=designation
#         self.company_name=company_name
#         print('designation : ',self.designation)
#         print('company name : ',self.company_name)
# class doctor(details):
#     def fun3(self,hospital,specialization):
#         self.hospital=hospital
#         self.specializaton=specialization
#         print('hospital : ',self.hospital)
#         print('specialization : ',self.specializaton)
# obj=developer()
# obj.fun1(777,'arun','male')
# obj.fun2('programmer','stark industry')
# print()
# obj=doctor()
# obj.fun1(444,'arunima','female')
# obj.fun3('mims hospital','eye specialist')

# HW
# using constructor

# class details():
#     def __init__(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#         print('id : ',self.id)
#         print('name : ',self.name)
#         print('gender : ',self.gender)
# class developer(details):
#     def __init__(self,id,name,gender,designation,company_name):
#         super().__init__(id,name,gender)
#         self.designation=designation
#         self.company_name=company_name
#         print('designation : ',self.designation)
#         print('company name : ',self.company_name)
# class doctor(details):
#     def __init__(self,id,name,designation,hospital,specialization):
#         super().__init__(id,name,designation)
#         self.hospital=hospital
#         self.specialization=specialization
#         print('hospital : ',self.hospital)
#         print('specialized : ',self.specialization)
# obj = developer(444,'arun','male','programmer','stark industry')
# obj1=doctor(777,'arunima','female','mims','ortho')








