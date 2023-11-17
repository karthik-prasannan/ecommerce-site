# syntax
# try :
#     //code to be excecuted
# except :
#     //catch the exception

# 1) zero division errors:

# try :
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except :
#     print('cant divisible by zero')

# solve quadratic equation using exceptional handling

# try :
#     a=int(input('enter a\t'))
#     b=int(input('enter b\t'))
#     c=int(input('enter c\t'))
#     x=-b+((b**2)-4*a*c)**0.5/(2*a)
#     x1=-b-((b**2)-4*a*c)**0.5/(2*a)
#     print(x)
#     print(x1)
# except :
#     print('invalid')


# 2) value error

# try :
#     a=int(input('enter a'))
#     print(a)
# except :
#     print('input an integer')


# try :
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('cant divide by zero')
# except ValueError:
#     print('input an integer')

# 3) intex error

# it occures when an invalid intex is given

# name=['amal','alex','arjun','alen']
# try :
#     position=int(input('enter the intex position'))
#     print(name[position])
# except IndexError:
#     print('list intex is out of range')
# except ValueError:
#     print('input am integer')

# 4) file not found error
#
# import os
# try :
#     filename=input('enter the file name')
#     os.remove(fr'C:\Users\karth\PycharmProjects\python class\{filename}')
#     print('file removed')
# except FileNotFoundError:
#     print('file not found')
# except ValueError:
#     print('enter string as input')

# a=int(input('enter the number'))
# print(b)



# exception handling with arguments
# an exception can have an argument which is a value that gives additional information about the problem.
# the content of the argument changes by the type of exception

# syntax

# try:
#     //code to be excecuted
# except Exceptiontype as Argument:
#     //exception body


# try:
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except ZeroDivisionError as e:
#     print(e)

# value error
# try:
#     a=int(
#     input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except ValueError as e:
#     print(e)
#
# filenotfound error
# import os
# try:
#     filename=input('enter the file name')
#     os.remove(fr'C:\Users\karth\PycharmProjects\python class\{filename}')
# except FileNotFoundError as e:
#     print(e)


# index error
# str=['a','b''c']
# try:
#     pos=int(input('enter position'))
#     print(str[pos])
# except IndexError as e:
#     print(e)