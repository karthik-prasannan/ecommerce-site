# overloading is a method or operator that can do different functionalities with the same name and different parameter/argument

# class A:
#     def product(self,a,b):
#         print(a*b)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=A()
# obj.product(1,2)
# obj.product(1,2,3)

# in the above code,we have defined 2 product method,
# but we can only use the second method,as python does not support method overloading

# Method to achieve method overloading:
# multipledispatch method : it is the method that is used for achieve method overloading

### pip : python installer package ###

# how to install package in python?
# pip install package name


from multipledispatch import dispatch

# class A:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=A()
# obj.product(1,2)
# obj.product(1,2,3)

# class A:
#     @dispatch(str,str)
#     def add_str(self,a,b):
#         print(a+b)
#     @dispatch(str,str,str)
#     def add_str(self,a,b,n):
#         print(a+b+n)
# obj=A()
# obj.add_str('kpk','\tjaba')
# obj.add_str('kpk','\tjaba','\tjabali')





