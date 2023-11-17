# data structure:
# it act as a container to store and organise data

#1) stack : it is a data structure that follows 'LIFO'(last in first out) operation.stack follows 2 methods
#     *)push : which adds element into the collection
#     *)pop : remove element from the collection
#2)queue : it is a data structure that follows 'FIFO'(first in first out)operation.
#     *)enqueue : which adds elements into the collection
#     *)dequeue : removes elements from the collection


# global = it is a keyword that is used to change the global values

#stack

# stack=[]
# size=int(input('enter the size of stack:'))
# top=0
# def push():
#     global top
#     if top==size:
#         print('stack is full')
#     else:
#         el=int(input('enter the element'))
#         stack.append(el)
#         top+=1
#         print(stack)
# def pop():
#     global top
#     if top==0:
#         print('stack is empty')
#     else:
#         stack.pop()
#         top-=1
#         print(stack)
# while True:
#     print('operation to perform')
#     choice=int(input('1.push\t\t2.pop:'))
#     if choice==1:
#         push()
#     elif choice==2:
#         pop()
#     else:
#         print('enter the correct input')

#queue
#
# queue=[]
# size=int(input('enter the size'))
# top=0
# def enqueue():
#     global top
#     if top==size:
#         print('queue is full')
#     else:
#         el=int(input('enter the element'))
#         queue.append(el)
#         top+=1
#         print(queue)
# def dequeue():
#     global top
#     if top==0:
#         print('queue is empty')
#     else:
#         queue.pop(0)
#         top-=1
#         print(queue)
# while True:
#     choice=int(input('1.enqueue \t\t2.dequeue\n enter your choice:'))
#     if choice==1:
#         enqueue()
#     elif choice==2:
#         dequeue()
#     else:
#         print('enter a valid output')

# Modules : * collection of function
#           * they are .py extension files












