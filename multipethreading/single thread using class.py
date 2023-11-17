# from threading import *
# import time
#
# class hello(Thread):
#     def run(self):
#         for i in range(5):
#             time.sleep(1.5)
#             print('hello',current_thread().name)
# class hai(Thread):
#     def run(self):
#         for i in range(5):
#             time.sleep(2)
#             print('hii',current_thread().name)
# t1=hello()
# t2=hai()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('this is a thread',current_thread().name)



# from threading import *
# import time
#
# class hello(Thread):
#     def a(self,a,b):
#         print(a+b)
#         for i in range(5):
#             time.sleep(1.5)
#             print('hello',current_thread().name)
# class hai(Thread):
#     def a(self,a,b):
#         print(a+b)
#         for i in range(5):
#             time.sleep(2)
#             print('hii',current_thread().name)
# t1=hello()
# t2=hai()
# t1.a(1,2)
# t2.a(1,4)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# from threading import *
# class hello(Thread):
#     def __init__(self,a,b):
#         Thread.__init__(self)
#         self.a=a
#         self.b=b
#     def run(self):
#         for i in range(5):
#             print(self.a+self.b,current_thread().name)
#
#
# t1=hello(1,2)
# t1.start()
# t1.join()

## run(): it is the entry point for a thread


# # create a class multiply,pass 3 arguments using run function print the product 3 times

# from threading import *
# class multiply(Thread):
#     def __init__(self,a,b,c):
#         Thread.__init__(self)
#         self.a=a
#         self.b=b
#         self.c=c
#     def run(self):
#         for i in range(5):
#             print(self.a*self.b*self.c,current_thread().name)
# t1=multiply(1,2,3)
# t1.start()
# t1.join()



# set name
# it is a function that is used to customize thread name

# from threading import *
#
# def cube(a):
#     print('calculate cube')
#     for i in a:
#         print('cube=',i**3,current_thread().name,t2.is_alive())
# def square(a):
#     print('calculate square')
#     for i in a:
#         print('calculate square',i**2,current_thread().name,t1.is_alive())
# li=[1,2,3,4]
#
# t1=Thread(target=square,args=(li,))
# t1.setName('first_thread')
# t2=Thread(target=cube,args=(li,))
# t2.setName('second_thread')
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(t1.is_alive())
# print(t2.is_alive())
# print('this is a multithread process',current_thread().name)



# is alive(): it is a function that is used to check a thread is alive or,not,if alive it returns True otherwise False

