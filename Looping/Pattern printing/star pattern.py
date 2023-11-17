# for i in range(n):
#     for j in range(n):
         #body of j loop

# for i in range(1,11):    #i=1,2,3,....,10
#     for j in range(1,11):  #j=1,2,3,....10
#         print(i,j)

# generate multiplication table from one to ten using nested for loop

# for i in range(1,11):
#     for j in range(1,11):
#         print('%d*%d=%d'%(i,j,i*j))
#     print() #new line

#Right angle triangle:
# i=used to create row
# j=used to create column
# *
# * *
# * * *
#user 3:
# for i in range(3):#i=0,1,2
#     for j in range(0,i+1): #(0,1) (0,2) (0,3)
#         print('*',end=' ')
#     print()
#
# num=int(input('enter the number'))
# for i in range(num):
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()

#generate a square pattern using nested for loop?
#enter the no of row:3

# num=int(input('enter the number'))
# for i in range(num):
#     for j in range(0,num):
#         print('*',end=' ')
#     print()

#generate a reverse right angle triangle ?
#user input
# a=int(input('enter the number'))
# for i in range(a):
#     for j in range(0,a-i):
#         print('*',end=' ')
#     print()
# or
# n=int(input('enter the number'))
# for i in range(n,0,-1):
#     for j in range(0,i):
#         print('*',end=' ')
#     print()

#PYRAMID PATTERN:
 #row : (0,3):i=0,1,2
 #space : (0,2)(0,1)(0,0):k(0,n-i-1)
 #star : (0,1)(0,2)(0,3):j(0,i+1)
  #  *
 # *   *
# *   *   *
# a=int(input('enter the number'))
# for i in range(0,a):
#     for k in range(0,a-i-1):
#         print('',end=' ')
#     for j in range(0,i+1):
#         print('*',end=' ')
#     print()

#GENERATE A REVERSE PYRAMID?

# a=int(input('enter the number'))
# for i in range(a):
#     for j in range(0,i):
#         print(' ' ,end='')
#     for k in range(0,a-i):
#         print('*',end=' ')
#     print()



