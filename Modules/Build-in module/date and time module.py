#python datetime module supplies classes to work with date and time
#these classes provide a number of funnction to deal with dates,times and time intervals

import datetime

#date():it is a constructor to convert datas into date format
# mydate=datetime.date(1996,12,11)
# print(mydate)

# a= int(input('enter the year'))
# b=int(input('enter the month'))
# c=int(input('enter the date'))
# date=datetime.date(a,b,c)
# print(date)
#
# answer
#
# enter the year2001
# enter the month7
# enter the date7
# 2001-07-07

#calling the today
#function of date class

#datetoday()

# today=datetime.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# answer=will print today date

# datetime.now():display the current date and time

# today=datetime.datetime.now()
# print('current date and time is',today)

#find difference b/w 2 dates?

# date1=datetime.datetime(2023,5,16)
# date2=datetime.datetime(2001,7,7)
# diff=date1-date2
# print('difference between dates =',diff)
#
# answer
# difference between dates = 7983 days, 0:00:00

# from datetime import timedelta
# d=datetime.date.today()
# d+=timedelta(days=15)
# print(d)
#
# answer
# 2023-05-31


# date1=datetime.datetime(2023,5,16,10,5,57)
# date2=datetime.datetime(2001,7,7,12,12,12)
# diff=date2-date1
# print(diff)

# find date before 20 days
# from datetime import timedelta
# d=datetime.date.today()
# d-=timedelta(days=20)
# print(d)

