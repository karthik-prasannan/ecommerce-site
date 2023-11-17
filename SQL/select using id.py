import pymysql

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id'))
# sql='select * from table_name where id=%d'%id
# mycursor.execute(sql)
#
# a=mycursor.fetchone()
# # fetchone:it is used to fetch a single row of data,it returns a single tuple
#
# print(a)
# id=a[0]
# name=a[1]
# email=a[2]
# number=a[3]
# print('id=',id,'name=',name,'email=',email,'number=',number)

##from product table fetch data using name,print product name and price

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
#
# name=input('enter the name')
# sql="select * from table_name where name='%s'"%name
# mycursor.execute(sql)
# a=mycursor.fetchone()
# name=a[1]
# number=a[3]
# print('name=',name,'number=',number)