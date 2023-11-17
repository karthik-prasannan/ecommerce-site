# a join caluse is used to combine rows from 2 or more tables based on a related column between them

# create a new table with fields
# id,product_name,feature

import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# sql="create table product(id int auto_increment,product_name varchar(50),color varchar(50),primary key(id))"
# mycursor.execute(sql)
# mydb.commit()
# print("table created successfully")

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# a=int(input('enter the number of datas'))
# for i in range(a):
#     mycursor=mydb.cursor()
#     product_name=input('enter the product name')
#     color=input('enter the color')
#     sql="insert into product(product_name,color) values('%s','%s')"%(product_name,color)
#     mycursor.execute(sql)
#     mydb.commit()
# print("table created successfully")

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# # sql='select table_name1.column_name1,table_name2.column_name2,table_name2.columnname1,table_name2.column_name2
# # from table_name1 inner join on table_name2 on table_name1.id=table_name2.id'
# sql=sql='select laptop.product_name,laptop.price,product.product_name,product.color from laptop inner join product on laptop.id=product.id'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     print(i)







# create a table with field id,student_name,roll,school_name
# create another table marklist id, maths,chemistry,english
# inner join student and marklist using roll_no
# student_name,maths,chemistry,english


# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# sql="create table student_marklist(id int auto_increment,student_name varchar(50),roll int,school_name varchar(50),primary key(id))"
# mycursor.execute(sql)
# mydb.commit()
# print("table created successfully")

import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# sql="create table marklist(id int auto_increment,roll_no int,maths int,chemistry int,english int,primary key(id))"
# mycursor.execute(sql)
# mydb.commit()
# print("table created successfully")


# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# a=int(input('enter the student number'))
# for i in range(a):
#     roll_no=int(input('enter the roll'))
#     maths=int(input('enter math mark'))
#     chemistry=int(input('enter che mark'))
#     english=int(input('enter eng mark'))
#     sql="insert into marklist(roll_no,maths,chemistry,english)values(%d,%d,%d,%d)"%(roll_no,maths,chemistry,english)
#     mycursor.execute(sql)
#     mydb.commit()
# print('data added successfully')

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# a=int(input('enter the student number'))
# for i in range(a):
#     roll=int(input('enter the roll'))
#     student_name=input('enter the name')
#     school_name=input('enter school name')
#     sql="insert into student_marklist(roll,student_name,school_name)values(%d,'%s','%s')"%(roll,student_name,school_name)
#     mycursor.execute(sql)
#     mydb.commit()
# print('data added successfully')

mydb=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="embloyee"
)
mycursor=mydb.cursor()
sql='select student_marklist.student_name,marklist.maths,marklist.chemistry,marklist.english from student_marklist inner join marklist on student_marklist.roll=marklist.roll_no'
mycursor.execute(sql)
a=mycursor.fetchall()
print('student_name\t\tmaths\tchemistry\t\tenglish')
for i in a:
    print('\t',i[0],
          '\t\t',i[1],'\t',
          '\t',i[2],'\t',
          '\t\t',i[3])



