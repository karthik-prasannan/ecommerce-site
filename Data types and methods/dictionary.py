#dictionary
#  it is a collection of key value pairs
#->unindexed
#->mutable
#->represent using {} brackets

#syntax
# dict={
#     'key1':'value1',
#     'key2':'value2',
#     'key3':'value3'
# }

person={
    'name':'karthik',
    100:200,
    'address':'abc123',
    'phone':123456789
}
print(person)

#type
print(type(person))

#access keys from dictionary

#keys()
print(person.keys())
#values
print(person.values())

#get()
a=person.get('name')
print(a)

b=person['phone']
print(b)

# a=input('enter the key')
# print(person[a])

#find the length of dictionry

b=len(person)
print(b)

#update method

person.update({'age':22})
print(person)                 #to add a new data

#user input updation
# a=input('enter the key')
# b=input('enter the value')
# person.update({a:b})
# print(person)

person['age']=24
print(person)

#pop method
person.pop('age')
print(person)

person.popitem()
print(person)

#dictionary iteration
# for i in (person.values()):
#     print(i)
for i in(person.keys()):
    print(i)

#item():it is a method that used to get both keys and values

for i,j in person.items():
    print(i,j)

#create a dictionary using user input
# dic={}
# a=int(input('enter the number'))
# for i in range(a):
#     b=input('enter the key')
#     c=input('enter the value')
#     if c.isdigit():
#         x=int(c)
#     elif'.' in c:
#         x=float(c)
#     else:
#         x=c
#     dic.update({b:x})
# print(dic)










