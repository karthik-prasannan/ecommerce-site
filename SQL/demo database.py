# import pymysql
# mydd=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydd.cursor()
# sql='create database embloyee'
# mycursor.execute(sql)
# print('database created successfully')



# create a table employee_details
# emp_id
# emp_name
# age
# emp_phone


import pymysql
mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='employee'
)
mycursor=mydb.cursor()
sql='create table employee(emp_id int auto_increment,emp_name varchar(50),age int,emp_phone bigint(10),primary key(emp_id))'
mycursor.execute(sql)
mydb.commit()
print('table created')