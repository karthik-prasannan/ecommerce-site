# *) abstraction in python is difined as a process of handling complexity by hiding unnecessory information from user
# *) this is one of the core concepts of object-priented programming (OOP)language

# what is ABC in abstract?
# this module provides the infrastructure for defining abstract base classes

# abc:python has a module called abc(abstract base class)that offers the necessory tools for crafting an abstract base class

# @abstractmethod : a decorator indicating abstract methods
# what is decorator?
# decorators can be extreamely usefull as the allow the extension of an existing function,without any modification to the-
# original function source code

# pass : it is a keyword that is used to define an empty class or empty function

# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def door(self):
#         pass
# class car(vehicle):
#     def wheel(self):
#         print('4 wheels....')
#     def airbag(self):
#         print('have airbag')
#     def door(self):
#             print('4 doors')
# obj=car()
# obj.wheel()
# obj.airbag()
# obj.door()

# from abc import ABC,abstractmethod
# class animal(ABC):
#     @abstractmethod
#     def eye(self):
#         pass
#     @abstractmethod
#     def skin(self):
#         pass
# class cat(animal):
#     def eye(self):
#         print(' 2 eyes ')
#     def skin(self):
#         print('have skin')
#     def nail(self):
#         print('have nail')
# class monkey(animal):
#     def eye(self):
#         print('have eyes')
#     def skin(self):
#         print('have skin')
#     def hair(self):
#         print('have hair')
#     def tail(self):
#         print('have tail')
# obj=cat()
# obj.eye()
# obj.skin()
# obj.nail()
# print()
# obj1=monkey()
# obj1.eye()
# obj1.skin()
# obj1.hair()
# obj1.tail()

# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def __init__(self,name,address):
#         pass
#     def hello(self):
#         pass
# class B(A):
#     def __init__(self,name,address):
#         super().__init__(name,address)
#         self.name=name
#         self.address=address
#         print('name : ',self.name,'\taddress : ',self.address)
#     def hello(self):
#         print('hello')
# obj=B('karthik','zxcvbn')
# obj.hello()






