# inheritance
# it is the method of accessing the properties,behavior and methods of parent class
# 1)single
# 2)multiple
# 3)multilevel
# 4)hierachical
# 5)hybrid

# single inheritance : it is a method with a single child class that access the method of a single parent child

# class A:             #parent class
#     def setval(self):
#         print('i am parent')
# class B(A):            #child
#     def setval1(self):
#         print('i am child')
# c=B()
# c.setval()
# c.setval1()
#
# class company:
#     def setval(self,name,location):
#         self.name=name
#         self.location=location
#         print('company name=',name)
#         print('location=',location)
# class employee(company):
#     def setval1(self,name,location):
#         self.name=name
#         self.location=location
#         print('name=',name)
#         print('location=',location)
# c=employee()
# c.setval('nexo','pandikkad')
# c.setval1('karthik','wandoor')

# single inheritance using constructor:
# class A:
#     def __init__(self):
#         print('parent class')
# class B(A):
#     def setval(self):
#         print('child class')
#         super().__init__()
# c=B()
# c.setval()

# super function : it is a function that is used to call the constructor of a parent class


# class vehicle:
#     def __init__(self,name,number):
#         self.name=name
#         self.number=number
#         print('vehicle name=',self.name)
#         print('vehicle number = ',self.number)
# class car(vehicle):
#     def __init__(self,name,number,color,price):
#         super().__init__(name, number)
#         self.color=color
#         self.price=price
#         print('color = ',self.color)
#         print('price = ',self.price)
# c=car('KIA','KL 10 AR 3333','silver',2000000)

# impliment a single inheritance using constructor & static variable?

# class stationary:
#     def __init__(self,company,type):
#         self.company=company
#         self.type=type
#         print('company name : ',self.company)
#         print('type : ',type)
# class pencil(stationary):
#     def __init__(self,company,type,color,hp):
#         super().__init__(company,type)
#         self.color=color
#         self.hp=hp
#         print('pencil color : ',color)
#         print('HP : ',hp)
# c=pencil('DOMS','pencil','BLACK AND WHITE','5HP')








