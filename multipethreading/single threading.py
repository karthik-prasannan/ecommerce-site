from threading import *

def cube(a):
    print('calculate cube')
    for i in a:
        print('cube=',i**3,current_thread().name)
def square(a):
    print('calculate square')
    for i in a:
        print('calculate square',i**2,current_thread().name)
li=[1,2,3,4]
cube(li)
square(li)


### current_thread().name?
# this function is used to get the name of current working thread of a process

# mainthread=mainthread in a process called a singlethread in which a process that excecutes in a singlethread during the running of a programe
