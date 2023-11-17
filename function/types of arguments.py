#types of arguments
# Arguments are classifies into 5 types

# 1)positional arguments

# 2)default arguments     #values which are used to assign a default value to the argument

#example
# def add(a,b=1):
#     print(a+b)
# add(5)
# add(5,2)

# def multiply(a,b=1,c=1,d=1):
#     print(a*b*c*d)
# multiply(1,2,3,4)

# def largest(a,b,c,d):
#     if a>b and a>c and a>d:
#         print('a is largest')
#     elif b>a and b>c and b>d:
#         print('b is greater')
#     elif c>a and c>b and c>d:
#         print('c is largest')
#     else:
#         print('d is largest')
# largest(1,2,5,1)

# 3)Keyword arguments

#    during a function call values passed through argumens need not be in the order of parameters in the function definition
# this can be achieved by keyword arguments

# def name(first_name, middle_name,last_name):
#     print(first_name,middle_name,last_name)
# name(middle_name='prasannan',first_name='karthik',last_name='k')

# 4)arbitory argument

# for arbitory argument a star is placed before a parameter in function definition which can hold any number of values

# def add(*a):
#     print(a)
# add(1,2,3,4,5,6)   #will store as a tuple
#
# def add(*a):
#     sum = 0
#     for i in a:
#            sum += i
#     print(sum)
# add(1,2,3,4)


#5)arbitory keyword argument

# def name(**kwargs):
#     print(kwargs)
#     for i,j in kwargs.items():
#         print(i,j)
# name(firstname='kpk', lastname='prasanan', phone=2126456)

#function with argument and return type
#return is a special statement that u can only use inside a function to send the function's resulst back to the coulumn










