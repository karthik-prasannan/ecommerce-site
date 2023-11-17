#LIST
# * List is a sequential data type
# * collection of elements
# * list is mutable(changable)
# * it is represented using square bracket []
# * any data type collection
# * list constuctor=it is a constructor that is used to convert a set of datas into list

#li=['karthik','kpk',123,456]
# print(li)
# print(type(li))

#(tuple)
# li=('kpk','karthik',123,852)
# print(li)
# print(type(li))

# APPEND=it is used to add element at the end of a list
# li=['kpk',123,548]
# li.append('abc')
# print(li)

#INSERT=it is used to add element to a specific position
#li=['kpk',123,'karthik',258]
# li.insert(0,'hello')
# print(li)

# li=['kpk',123,'karthik',258]
# a=input('enter the name')
# p=int(input('enter the position'))
# li.insert(p,a)
# print(li)

#EXTEND=add elements of a list to the end of the current list
# li=['kpk',123,'karthik',258]
# li.extend(['a',1])
# print(li)

#POP()=it is a method used to remove elements at a specified position
# li=['kpk',123,'karthik',258]
# li.pop(1)     #if we use pop() like this it will remove last digit
# print(li)

#REMOVE METHOD=remove an element by using it's name
# li=['kpk',123,'karthik',258]
# li.remove('karthik')
# print(li)

#REVERSE=
# li=['kpk',123,'karthik',258]
# li.reverse()
# print(li)

#COUNT=it returns the number of elements with specified value
# li=['kpk',123,'karthik',258]
# a=li.count('kpk')
# print(a)

#SORT= arrange to correct order
# name=['karthik','ramu','jayan']
# name.sort()
# print(name)

# number=[12,56,11,25,78]
# number.sort()
# print(number)

# name=['Karthik','tony','silpa'] #capital letter comes first
# name.sort()
# print(name)

# num=[56,85,69,89]
# num.sort(reverse=True)
# print(num)

#LEN
# li=['karthik','ramu','jayan']
# print(len(li))

#LIST ITERATION
# li=['karthik','ramu','jayan']
# for i in li:
#     print(i)

#ELEMENT ACCESSING
# li=['karthik','ramu','jayan']
# el=li[0]
# print(el)

#SLICING
# li=['karthik','ramu','jayan','silpa']
# a=li[1:3]
# print(a)
# b=li[1:]
# print(b)
# c=li[:3]
# print(c)
# d=li[:]
# print(d)
# e=li[::-1]
# print(e)

# li=[]
# n=int(input('enter the no: of elements'))
# for i in range(n):
#     element=input('enter the element')
#     li.append(element)
# print(li)

#create 3 empty list
#name
#salary
#phone number

# name=[]
# salary=[]
# phone=[]
# a=int(input('enter the length of name list'))
# b=int(input('enter the length of salary list'))
# c=int(input('enter the length of phone number'))
# for i in range(a):
#     x=input('enter the name')
#     name.append(x)
# print(name)
# for j in range(b):
#     y=int(input('enter the salary'))
#     salary.append(y)
# print(salary)
# for k in range(c):
#     z=int(input('enter the phone number'))
#     phone.append(z)
# print(phone)

#create an empty list
# a=[]
# num=int(input('enter the number'))
# for i in range(num):
#     b=input('enter the data')
#     if b.isdigit():
#         a.append(int(b))
#     elif '.' in b:
#         a.append(float(b))
#     else:
#         a.append(b)
#     print(a)



