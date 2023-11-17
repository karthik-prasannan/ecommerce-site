















# s={'a','b','c'}
# print(s)
# #
# # #length
# print(len(s))
# #
# # #type
# print(type(s))
#
# #find the length of set without using len function
# co=0
# for i in s:
#     co+=1
# print(co)
#
# #add method
# s.add('d')
# print(s)

# create an empty set add elements into the set

# s=set({})
# a=int(input('enter the value'))
# for i in range(0,a):
#     element=input('enter thr element')
#     s.add(element)
# print(s)

#remove duplicate
# li=['a','a','b','b','c','c']
# x=set(li)
# print(type(x))
# print(x)
# y=list(x)
# print(type(y))
# y.sort()     #to sort the variables
# print(y)

#update()method
# s={'a','b','c'}
# s1={'h','i','j','k'}
# s.update(s1)
# print(s)
# s2=[1,2,3,4]
# s.update(s2)
# print(s)

#tuple
# s4=(6,7,8)
# s.update(s4)
# print(s)

#remove method
# s.remove('b')
# print(s)

#discard method
# s.discard('b')
# print(s)

#pop() method
# s.pop()
# print(s)#(to remove the last digit)

#question
# do you want to remove element from the set:yes
#enter the element to remove:a
#{'b','c'}
#do you want to remove element from the set:no
#exit

# s={'a','b','c'}
# while True:
#     b = input('do you want to remove element from the set')
#     if b=='yes':
#         element=input('enter the element remove:')
#         s.remove(element)
#         print(s)
#     elif b=='no':
#         print('exit')
#         break   #it is a keyword(reserved word)that is used to stop the execution of your program

#intersection_update method
#it is the method that is used to keep only items that are present in both sets

# x={'a','b','c'}
# y={'c','d','e'}
# x.intersection_update(y)
# print(x)

#symmetric_difference update
#method will keep only the element that are not present in both

# x={'a','b','c'}
# y={'c','d','e'}
# x.symmetric_difference_update(y)
# print(x)

#frozenset
#it is an inbuild function in python which takes an iterable object as input and makes the immutable simply it freeze
#iterable pbject and makes them unchangable
#
# list=[1,2,3]
# x=frozenset(list)
# x.append('a')  #(not possible)
# print(x)


