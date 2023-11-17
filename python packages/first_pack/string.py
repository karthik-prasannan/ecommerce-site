# 2)str_upper() #count the no:of uppercase in a string
# 3)str_lower() #'" " " " " " " " "lower case in a string
# 4)str_rev()  #

def chrlen(x):
    count=0
    for i in x:
        if ' ' not in i:
            count+=1
    return(count)

def upper(y):
    count=0
    for i in y:
        if i.isupper():
            count+=1
    return(count)

def lower(y):
    count=0
    for i in y:
        if i.islower():
            count+=1
    return (count)

def rev(z):
    a=z[::-1]
    return(a)







# python packages:
# package is te collection of related modules
# __init__.py : it is a file that is used to convert a directory into a package