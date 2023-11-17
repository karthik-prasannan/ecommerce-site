#.....DATA TYPES AND METHODS.....

# Text datatype = string
# Sequential datatype = list , tuple
# Mapping datatype = dictionary
# Set datatype = set , frozenset

#what is a srting

#METHOD

#Capitilize
# a='hello world'
# print(a)
# print(a.capitilize())

#Find
# a='hello world'
# f=a.find('l')
# print(f)
#the find method that return intex position pf a element

#Intex
# a='hello world'
# f=a.index('o')
# print(f)

#Title
# a='hello world'
# print(a.title())

#Upper method
# a='hello world'
# print(a.upper())

#Lower case
# a='HELLO WORLD'
# print(a.lower())

#Swapcase
# a='Hello World'
# print(a.swapcase())

#Split method
# b='hello welcome'
# li=b.split(' ')
# print(li)

# path='aa/bb/abc.png'
# li=path.split('/')
# print(li)

#Strip method
# a=' hello '
# print(a.strip())

#to remove the space

#1)rstrip = to remove space in right
#2)lstrip = "    "    "     "  left

#String checking methods
#1)Isalpha() =
#print only alphabets

# w=input('enter the number')
# print(w.isalpha())

#2)Isdigit() =
#print only numbers

# w=input('enter the number')
# print(w.isdigit())

#3)isalnum() =
#print both number and alphabet

# w=input('enter the word')
# print(w.isalnum())

#4)istitle() =
#will become capital for the first word's first letter

# w=input('enter the word')
# print(w.istitle())

#5)Isupper() =
#print to capital

# w=input('enter the word')
# print(w.isupper())

#6)islower() =
#print to small letters

# w=input('enter the word')
# print(w.islower())

#String iteration
# word='hello'
# for i in word:
#     print(i)

#String concantination(adding)
#method of adding 2 or more string
# print('welcome'+'hello')

#28/04/23

#string slicing:it is used to access a part of sequence
#str='hello world'
# x=str[1:4]
# print(x)
#
# y=str[2:]
# print(y)
#
# z=str[:5]
# print(z)
#
# z1=str[:]
# print(z1)

#INTEXING = element accessing using intex position:
#always use square bracket
# str='hello world'
# a=str[2]
# print(a)

#NEGATIVE INTEXING
# str='hello world'
# b=str[-1]
# print(b)

#d=-1, l=-2, r=-3, l=-4  etc.....


#LEN():
# it is a function that is used to find length of a string of sequence

# str='hello world'
# print(len(str))

# write a program to find length of a string input by the user without using an inbuild function?

# str=input('enter the string')
# length=0
# for i in str:
#     length+=1
# print('len of string=',length)

#write a program to remove white space from a string input by the user without using inbuild function?

#input expected= hello world
#output=helloworld

# str=input('enter the string')
# str1=''
# for i in str:
#     if i!=' ':
#         str1+=i
# print(str1)

#write a program to find total number of vowels in a string input by the user?

#hello
#total no.of vowels=2

# a=input('enter a srting')
# num=0
# for i in a:
#     if i in 'aeiouAEIOU':
#         num+=1
# print(num)

#write a program to find reverse of a string input by the user?

# a=input('enter the string')
# print(a[::-1])

#OR

# a=input('enter the string')
# p=len(a)-1 #to get the last intex position of the string
# for i in range(p,-1,-1): #i=4,3,2,1,0
#     print(a[i],end='')







