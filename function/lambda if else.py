#find square of a number if number greater than 0?
# x=lambda a:a**2 if a>0 else None  #none = null value
# print(x(5))

#find a number is negative or positive using lambda?
#x=lambda a:'positive' if a>0 else 'negative'
#print(x(-5))

#find the largest of 2 numbers using lambda?
# x=lambda a,b:'a is largest' if a>b else 'b is largest'
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# print(x(a,b))

#convert a positive number to negative number and negative number to positive number?
# x=lambda a:-1*a if a>0 else -1*a   #-1*1=-1 , -1*-1=1
# a=int(input('enter the number'))
# print(x(a))

#find a number is odd or even?
# x=lambda a:'a is odd'if a%2 else 'a is even'
# a=int(input('enter the number'))
# print(x(a))

#write a program to find the largest of 3 numbers?

# x=lambda a,b,c:'a is greater' if a>b and a>c else('b is greater'if b>c else 'c is greater')
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# print(x(a,b,c))

#find the smallest of 3 numbers input by the user?
# x=lambda a,b,c:'a is smaller' if a<b and a<c else('b is smaller' if b<c else 'c is smaller')
# a= int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# print(x(a,b,c))

#find a number is positive or negative or zero
# x=lambda a:'positive'if a>0 else('negative'if a<0 else 'zero')
# a=int(input('enter the number'))
# print(x(a))

#find the largest of 4 numbers
# x=lambda a,b,c,d:'a is greater' if a>b and a>c and a>d else('b is greater'if b>c and b>d else('c is greater'if c>d else 'd is greater'))
# a=int(input('enter the number'))
# b=int(input('enter the number'))
# c=int(input('enter the number'))
# d=int(input('enter the number'))
# print(x(a,b,c,d))

#HW

#accept the age of 4 people and display the youngoust one
# x=lambda a,b,c,d:'%d is youngest'%a if a<b and a<c and a<d else('%d is youngest'%b if b<c and b<d else ('%d is youngest'%c if c<d else '%d is youngest'%d))
# a=int(input('enter the age'))
# b=int(input('enter the age'))
# c=int(input('enter the age'))
# d=int(input('enter the age'))
#print(x(a,b,c,d))


# lamda built in function

# 1)filter
# 2)map
# 3)reduce
#
# filter

# filter that takes a sequence as an argument that will filter out all the element of the sequence

# syntax
# variable_name = list(list(filter(lambda argument:expression,list variable))

# write a lambda function to filter out even number from the given list?
# li=[1,2,3,4,5,6]
# x=list(filter(lambda i:i%2==0,li))
# print(x)

# odd
# x=list(filter(lambda i:i%2!=0,li))
# print(x)

# from the list filter out numbers which is divisible by 13 but not by 3 using lambda
# li=[1,213,100,220,101,33,13]
#
# x=list(filter(lambda i:i%13==0 and i%3!=0,li))
# print(x)

# from the given list filter out the ages between 18 and 50?
# age=[12,34,28,2,50,22,1]
#
# x=list(filter(lambda i:i<50 and i>18,age))
# print(x)

#MAP()
# map function in python takes a sequence as argument and a new sequence is returned
# it is a build in function that allows ypu to process and transfprm all the items in an iterable list without a for loop

# syntax
# variable_name=list(map(lambda argument:expression,list_name))

# to find the square of all list
# l=[2,3,4,5,6]
# x=list(map(lambda i:i**2,l))
# print(x)

#find square root of each element in the given list
# l=[1,4,9,16,25,36]
# x=list(map(lambda i:i**0.5,l))
# print(x)

# create a list of numbers from 1 to 10
#enter the number=
# l=[1,2,4,5,6,7,8,9,10]
# a=int(input('enter the number'))
# x=list(map(lambda  i:i*a,l))
# print(x)

# Map function using two list

# zip()
# in python zip function which is used o combine 2 or more into a single iterable where elements from corresponding
# positions are paired together

# name=['kpk','karthik']
# age=[12,14]
# a=zip(name,age)
# print(list(a))

# a=[1,2,3,4]
# b=[4,5,6,7]
# w=list(map(lambda x,y:x+y,a,b))
# print(w)

# l=['alen alen','joseph joseph','chutki chutki']
# a=list(map(lambda i:i.capitalize(),l))
# print(a)

#Reduce()
# reduce function in python takes a sequence as an argument and a new reduced result is returned
# * the reduce function which belongs to function tool module.
# * module=it is a collrction of functions,it is python file with .py extension

# how to import reduce method?

# from functools import reduce
# # find the largest element from the list using reduce()
# l=[100,200,300,500,400]
# x=reduce(lambda a,b:a if a>b else b,l)
# print(x)

# find the smallest element from the list
# from functools import reduce
# l=[2,1,3,5,7]
# x=reduce(lambda a,b:a if a<b else b,l)
# print(x)

# HW
# find the sum of elements in list using reduce?
# li=[1,2,3,4,5,6]
#
# find the product of numbers from given list ?
# li[5,7,9,11,13]

# li=[1,2,3,4,5,6]
# from functools import reduce
# x=reduce(lambda a,b:a+b,li)
# print('sum of elements :',x)

# li=[5,7,9,11,13]
# from functools import reduce
# z=reduce(lambda a,b:a*b,li)
# print('product of numbers :',z)







