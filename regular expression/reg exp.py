# *) it is defined as a sequence of characters which are used to search for a pattern in a string
# *) module re is used for regular expression(regex) in python
# *)some built in function used in regular expression:

# 1)fullmatch() : it returns true if match is found
# 2)search() : it returns match object
# 3)findall() : it returns list that contains all match
# 4)split() : it returns a string has been split
# 5)sub() : it is used replace the matches

# --> a regular expression is created using mix of characters special sequence and sets

# characters:
# [] : it represents a set of characters
# \ : it represents special sequence
# ^ : it represents patterns present at the beginning of a string
# * : it represents 0 or more occurance [A-Z]*
# + : it represents 1 or more occurance [A-Z]+
# {} : specified number of occurance of pattern
# | (or) : it represents this or that character is present

# rules of regular expression(regex):
# x='[abc]+' : either a,b, or c
# x='[^abc]' : except abc
# x='[a-z]' : lower case a to z
# x='[A-Z]' : upper case A to Z
# x='[a-zA-Z]' : both lower and uppercase
# x='[0-9]' : it check the digits
# x='[a-zA-Z0-9]' : lower,uppercase or digit

# special sequence :
# x='\s' : check space
# x='\d' : check digit
# x='\D' : it returns string except numbers
# x='\w' : it returns a string contains a word

# quantifiers :
# x='[a]+' : it includes more numbers of a
# x='[a]*' : count including zero number of a
# x='[a]?' : a included or not included
# x='[a]{n}': n --> number
# x='[a]{n,k}' : n-->minimum number k-->maximum number

