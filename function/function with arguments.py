#arguments
#these are the values that are passed into a function during function calling
#function are also known as parameters

# def add(a,b):
#     print(a+b)
# add(4,5)

#variable classification
#1)global
#2)local

#global:a variable that can access inside a function and outside a function

#local variable:a variable that can only access inside a function

# def add(a,b):
#     print(a+b)
# num1=int(input('enter number'))
# num2=int(input('enter 2nd number'))
# add(num1,num2)

#factorial using function with argument?
# def factorial(a):
#     f=1
#     for i in range(1,a+1):
#         f+=1
#         print('factorial=',f)
# num=int(input('enter the num'))
# factorial(num)

#find the largest of 3 numbers using function with arg?

# def largest(a,b,c):
#     if a>b and a>c:
#         print('%d is greater'%a)
#     elif(b>c):
#         print('%d is greater'%b)
#     else:
#         print('%d is greater'%c)
# largest(1,2,3)

#reverse of a string using function with arg?

# def string_rev(a):
#     print(a[::-1])
# str=input('enter string')
# string_rev(str)

#find a number is armstring or not using function with arg?

#armstrong(153)
#output:
#153 is an armstrong number

# def armstrong(a):
#     sum=0
#     temp=a
#     while a!=0:
#         rem=a%10
#         sum+=rem**3
#         a=a//10
#     if temp==sum:
#         print('armstrong')
#     else:
#         print('not armstrong')
# a=int(input('enter the number'))
# armstrong(a)

#HW

#reverse of a number
#area of a circle
#solve quadratic equation

# def number_rev():
#     a=int(input('enter the number'))
#     rev=0
#     while(a!=0):
#         rem=a%10
#         rev=rev*10+rem
#         a//=10
#     print('reverse if number',rev)
# number_rev()

# def area_circle(r):
#     pi=3.14
#     a=pi*r**2
#     print(a)
# r=int(input('enter the radius'))
# print('area of circle')
# area_circle(r)

# import cmath
# def solve_quadratic(a,b,c):
#     q=(b**2)-(4*a*c)
#     q1=(-b-cmath.sqrt(q))/(2*a)
#     q2=(-b+cmath.sqrt(q))/(2*a)
#     print('value of x',q1,q2)
# a=float(input('enter the a:'))
# b=float(input('enter the b:'))
# c=float(input('enter the c:'))
# solve_quadratic(a,b,c)

# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enter c'))
# d=((b**2)-4*a*c)**0.5 #root of a number =(^1/2)=^0.5
# x1=(-b+d)/(2*a)
# x2=(-b-d)/(2*a)
# print(x1)
# print(x2)

# def quadratic_eqn(a,b,c):
#     d=((b**2)-4*a*c)**0.5
#     x1=(-b+d)/(2*a)
#     x2=(-b-d)/(2*a)
#     print('the solution %s is %s'%(x1,x2))
# n1=int(input('enter the first num'))
# n2=int(input('enter the second num'))
# n3=int(input('enter the third num'))
# quadratic_eqn(n1,n2,n3)

# def tax(a):
#     if a>100000:
#         tax=(a*15)/100
#     elif a>50000 and a<=100000:
#         tax=(a*10)/100
#     else:
#         tax=(a*5)/100
#     print('tax is =',tax)
# x=int(input('enter the cost'))
# tax(x)

# def divisible(a):
#     if a%2==0 and a%3==0:
#         print('divisible')
#     else:
#         print('not divisible')
# x=int(input('enter the num'))
# divisible(x)
























