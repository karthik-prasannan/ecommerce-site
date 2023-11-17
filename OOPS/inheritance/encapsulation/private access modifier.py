# class employee:
#     def __init__(self,name,salary):
#         #public data members
#         self.name=name
#         self.__salary=salary
#     def fun(self): #public function
#         print('name = ',self.name,'salary = ',self.__salary)
# obj=employee('jaba',100000)
# obj.fun()
# print('name : ',obj.name)
# print('salary : ',obj.__salary) #will not work

# Name mangling = to access private data and method outside the class
# using public method to access private datas

# syntax
# _classname__datamember

# class employee:
#     def __init__(self,name,salary):
#         #public data members
#         self.name=name
#         self.__salary=salary
#     def __fun(self): #public function
#         print('name = ',self.name,'salary = ',self.__salary)
# obj=employee('karthik',1000000)
# print('name',obj.name)
# obj._employee__fun()
# print('salary',obj._employee__salary)

