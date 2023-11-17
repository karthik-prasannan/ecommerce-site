import pymysql


# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='alter table student_marklist add location varchar(200)'
# mycursor.execute(sql)
# mydb.commit()
# print('column addeed successfully')



#
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# location=input('enter location')
# sql='update student_marklist set location="%s" where id=%d'%(location,id)
# mycursor.execute(sql)
# mydb.commit()
# print('database updated....')



# sql='alter table marklist add total int as(maths+chemistry+english)

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='alter table marklist add total int as (maths+chemistry+english)'
# mycursor.execute(sql)
# mydb.commit()
# print('column added successfully')


# #query to drop column
# #sql='alter table student drop location'

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='alter table student_marklist drop location' #drop=delete
# mycursor.execute(sql)
# mydb.commit()
# print('column dlted successfully')


### sql="drop table table_name"(to dlt a table)

### sql="truncate table table_name"(to dlt rows from the table but the table structure remains)

# dlt database #

### sql="drop database database_name"





