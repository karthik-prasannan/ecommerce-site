# fullmatch :

# write a regex pattern to validate a name

import re

# rule='^[A-Za-z]+'
# word=input('enter your name')
# match=re.fullmatch(rule,word)
# if match:
#     print('match')
# else:
#     print('not match')

# name should start with uppercase
# lowercase,space
# 7-10

# rule='^[A-Z][a-z\s]{6,9}'
# word=input('enter the name')
# match=re.fullmatch(rule,word)
# if match:
#     print('valid')
# else:
#     print('invalid')


### rules ###

# 1) the name should only starts with uppercase A,B or C
# 2)followed by lowercase
# 3)numbers should be included or not included


# rule='^[ABC][a-z]+[0-9]*'
# name=input('enter the name')
# match=re.fullmatch(rule,name)
# if match:
#     print('valid')
# else:
#     print('invalid')


# phone number validation
# 10 number required
# it should starts with 9,8,7,6

# import re

# rule='^[9876][0-9]{9}'
# a=input('enter the number')
# check=re.fullmatch(rule,a)
# if check:
#     print('true')
# else:
#     print('false')

# +91
# 9,8,7,6
# limit=10

# rule='^[+][9][1][6-9][0-9]{9}'
# a=input('enter the number')
# check=re.fullmatch(rule,a)
# if check:
#     print('true')
# else:
#     print('false')


# 1.the name should only starts with uppercase A,B OR C
# 2.followed by lowercase
# 3.numbers should be included(2 numbers) or not included

# rule='^[ABC][a-z]+([^0-9]|[0-9]{1,2})'
# a=input('enter name')
# check=re.fullmatch(rule,a)
# if check:
#     print('true')
# else:
#     print('false')


# email validation
# karthik@gmail.com
# karthik123@gamil.com
# karthik_123@gmail.com
# 123@gmail.com -->not valid

# rule='^[a-z]+[0-9]*[*_]?[a-z0-9]*[@][g][m][a][i][l][.][c][o][m]'
# a=input('enter the gmail')
# check=re.fullmatch(rule,a)
# if check:
#     print('valid')
# else:
#     print('not valid')


# DOB VALIDATION
# 14/10/2001
# 14-10-2001
# rule=r'^[0-9]{1,2}[-][0-9]{1,2}[-][0-9]{4}|[0-9]{1,2}[\\][0-9]{1,2}[\\][0-9]{4}'
# a=input('enter the DOB')
# check=re.fullmatch(rule,a)
# if check:
#     print('valid')
# else:
#     print('not valid')



# registration and login using regex

# enter name:
# enter email:
# enter phone number:
# enter password:
#registration success
# login page:
# email:
# password:
# login success,else:failed

#else:registration failed

# rule1='^[A-Za-z]+'
# rule2='^[a-z]+[0-9]*[*_]?[a-z0-9]*@gmail.com'
# rule3='^[+][9][1][9876][0-9]{9}'
# rule4='^[a-zA-Z]\w{3,14}$'
# name=input('enter the name')
# check=re.fullmatch(rule1,name)
# email=input('enter email')
# check1=re.fullmatch(rule2,email)
# phone=input('enter phone number')
# check2=re.fullmatch(rule3,phone)
# password=input('enter password')
# check3=re.fullmatch(rule4,password)
# if check and check1 and check2 and check3:
#     print('registration success')
#     a=input('enter email')
#     b=input('enter password')
#     if a==email and b==password:
#         print('login success')
#     else:
#         print('failed')
# else:
#     print('registratiion failed')




