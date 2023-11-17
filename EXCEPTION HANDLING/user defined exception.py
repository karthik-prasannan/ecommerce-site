# user define exception

# in python,user can define custom exceptions by creating a new class
# this exception class has to be derived,either directly or indirectly,
# from the build-in Exception class,most of the build-in exception are also derived this  class

# class ZeroError(Exception):
#     pass
# class NegativeError(Exception):
#     pass
#
# try:
#     num=int(input('enter a number'))
#     if num==0:
#         raise ZeroError
#     elif num<0:
#         raise NegativeError
#     else:
#         print('success')
# except ZeroError:
#     print('zero error occured')
# except NegativeError:
#     print('negative error occured')




# age>50 :too old
# age<21 :too young
# else : you are registered

# class tooold(Exception):
#     pass
# class tooyoung(Exception):
#     pass
#
# try:
#     a=int(input('enter age'))
#     if a>50:
#         raise tooold
#     elif a<21:
#         raise tooyoung
#     else:
#         print('you are registered')
# except tooold:
#     print('enter age below 50')
# except tooyoung:
#     print('enter age above 21')





