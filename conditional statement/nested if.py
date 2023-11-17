# Nested if

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# if a > b:
#     if a > c:
#         print("The largest is %d" % a)
#     else:
#         print("The largest is %d" % c)
# elif b > c:
#     print("The largest is %d" % b)
# else:
#     print("The largest is %d" % c)

#Largest of four numbers using nested if

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("enter third number: "))
# d = int(input("enter fourth number: "))
# if a > b:
#     if a > c:
#         if a > d:
#             print("The largest number %d" % a)
#         else:
#             print("The largest number %d" % d)
#     else:
#         print("The largest number %d" % c)
# elif b > c:
#     if b > d:
#         print("The largest number %d" % b)
#     else:
#         print("The largest number %d" % d)
# elif c > d:
#     print("The largest number %d" % c)
# else:
#     print("The largest number %d" % d)

# gender : male, female age :
#if gender = male age<18 : queue 1
#if gender = female age<18 : queue 1

#if gender = female and age>= 18 and age <=50 : queue 2
#if gender = female and age >50 : queue 3

#if gender = male and age >=18 and age <=50 : queue 4
#if gender = male and age >50 : queue 5

# gender = input("Enter your gender: ")
# age = int(input("Enter your age: "))
# if age > 0 and age < 18:
#     if gender == "male":
#         print("Queue 1")
#     elif gender == "female":
#         print("Queue 1")
#     else:
#         print("Enter a valid input")
# elif age >= 18 and age <= 50:
#     if gender == "female":
#         print("Queue 2")
#     elif gender == "male":
#         print("Queue 4")
#     else:
#         print("Enter a valid input")
# elif age > 50:
#     if gender == "female":
#         print("Queue 3")
#     elif gender == "male":
#         print("Queue 5")
#     else:
#         print("Enter a valid input")
# else:
#     print("Enter valid input")