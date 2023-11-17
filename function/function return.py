# def hello():
#     return'hello'
# print(hello())

#write a program to multiply 2 numbers using functions with arg and return

# def multiply(a,b):
#     return a*b
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# print(multiply(a,b))

#find a number odd or even using function with arg and return
# def num(a):
#     if a%2==0:
#         return 'num is even'
#     elif a%2!=0:
#         return'num is odd'
# a=int(input('enter the num'))
# print(num(a))

# simple calculator with arg and return

# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mul(a,b):
#     return(a*b)
#
# def div(a,b):
#     return(a/b)
#
#
# print('simple calculator\noption:\n1.adiition\n2.substracton\n3.multiplication\n4.division')
# choice=int(input('enter your choice'))
# if choice==1:
#     a = int(input('enter the first number'))
#     b = int(input('enter the second number'))
#     print(add(a,b))
# elif choice==2:
#     a = int(input('enter the first number'))
#     b = int(input('enter the second number'))
#     print(sub(a,b))
# elif choice==3:
#     a = int(input('enter the first number'))
#     b = int(input('enter the second number'))
#     print(mul(a,b))
# elif choice==4:
#     a = int(input('enter the first number'))
#     b = int(input('enter the second number'))
#     print(div(a,b))
# else:
#     print('exit')



#lambda function
#1)a lambda function which is a single line anonymous function

#2)anonymous function which means a function without declaration or a function without a name

#3)we use lambda function when we requires a nameless function for a short period of time

#syntax
#variable_name=lamda arguments:expression

# x=lambda a,b:a+b
# print(x(1,2))

# x=lambda a:'my name is %s'%a
# print(x('kpk'))

#1)solve a/b*c using lambda function?
#2)find square root of a number ?
#3)find cube of an argument?
#4)find area of circle

# x=lambda a,b,c:a/b*c
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# print(x(a,b,c))

# x=lambda a:a**0.5
# a=int(input('enter the number'))
# print(x(a))

# x=lambda a:a**3
# a=int(input('enter the number'))
# print(x(a))

# x=lambda a:3.14*a**2
# a=int(input('enter the number'))
# print(x(a))


