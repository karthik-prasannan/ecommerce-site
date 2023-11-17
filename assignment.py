# Q1:
# Write a Python program to calculate the discount percentage based on the
# purchase amount. If the purchase amount is greater than or equal to 1000, apply a 10%
# discount.If the amount is less than 1000, apply a 5% discount. Print the final discounted
# amount.

# A:
# price=int(input("enter price"))
# if(price>=1000):
#     total=price*0.10
#     print("discount amount is ",total)
# else:
#     total=price*0.05
#     print("discounted amount is",total)

# Q2.
# Given the age and height of a person,write a Python program to determine if the person is
# eligible for a roller coaster ride.To be eligible, the person must be at least 10 years old and
# have a height of 130 cm or more.

# A:
# age=int(input("enter age"))
# h=int(input("enter height"))
# if(age>=10 and h>=130):
#     print(" Congratulation!! you are eligible for roller coaster ride")
# else:
#     print("oops!!! you are not eligible")

# Q3
# Accept the marks of English, Math and Science, Social Studies Subject and display the
# stream allotted according to following
# All Subjects more than 80 marks - Science Stream
# English >80 and Math, Science above 50 -Commerce Stream
# English > 80 and Social studies > 80 - Humanities

# A:
# eng=int(input("Enter mark of english"))
# mat=int(input("Enter mark of maths"))
# sci=int(input("Enter mark of science "))
# ss=int(input("Enter mark of social studies"))
# if(eng>80 and mat>80 and sci>80 and ss>80):
#     print(" You can join in Science stream")
# elif(eng>80 and mat>50 and sci>50):
#     print("You are eligible for Commerce stream")
# elif(eng>80 and ss>80):
#     print("You are eligible for Humanities ")
# else:
#     print('you are not eligible')

# Q4
# Accept the number of days from the user and calculate the charge for library according to
# following
# Till five days: Rs 2/day.
# Six to ten days: Rs 3/day.
# 11 to 15 days: Rs 4/day
# After 15 days : Rs 5/day

# A:
# day=int(input("enter days"))
# if(day<=5):
#     cost=day*2
#     print(cost)
# elif(day>=6 and day<=10):
#     cost=day*3
#     print(cost)
# elif(day>=11 and day<=15):
#     cost=day*4
#     print(cost)
# elif(day>15):
#     cost=day*5
#     print(cost)

# Q5
# Write a programme that takes a user’s age as input.
# If the age is greater than or equal to 18, ask the user if they have a valid id.
# If they have a valid id, print you are allowed to enter.
# If they don’t have a valid id print sorry you need a valid id to enter.
# If the age is less than 18, print you are not allowed to enter.

# A:
# age=int(input("Enter age"))
# if(age>=18):
#     id = input("do you have id")
# if(id=="yes"):
#     print("you are allowed to enter")
# elif(age<18):
#     print("you are not allowed to enter")
# else:
#     print("sorry you need a valid id to enter")


# Q6
# Write a programme that takes a number as input and
# checks if it is positive, negative, or zero.
# If it is positive, ask the user if they want to square the number.
# If they choose a square, print its square.
# If it is negative, ask the user if they want to find its absolute value.
# If they choose to find the absolute, print its absolute value.
# If the value is zero, Print ‘the value is zero’.

# A:
# num=int(input("Enter a number"))
# if(num>0):
#     print(num," is positive")
# sqr=input("do you want to square the number")
# if(sqr=="yes"):
#     print("square is",num**2)
# elif(num<0):
#     print(num," negative")
# abs=input("do you want to find absolute value")
# if(abs=="yes"):
#     print("absolute value is ",-1*num)
# elif(num==0):
#     print("zero........!")