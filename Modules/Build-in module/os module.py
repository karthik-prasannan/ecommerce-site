# os module = operating system
# module in python that is used to interact with the operating system

# getcwd()=method that is used to get the current working directory(to identify the path)

import os
# cwd=os.getcwd()
# print(cwd)

# raw string(r)=used to remove special characters from the path

# mkdir():method used to create directory named path with specified numeric mode

# os.mkdir(r'C:\Users\karth\PycharmProjects\python class\new')  #put r to remove the special character in /n
# print('success')

# listdir():get the list of all files and directories in a specified directory

# lst=os.listdir(r'C:\Users\karth\PycharmProjects\python class')
# print(lst)

# rmdir():used to remove empty directory
# os.rmdir(r'C:\Users\karth\PycharmProjects\python class\new')
# print('directory deleted......')

# remove():used to remove or delete file path

os.remove(r'C:\Users\karth\PycharmProjects\python class\jaba.py')
print('file deleted')

print(os.name)

# windows NT is a Microsoft Windows personal computer operating system
# NT:New technology