# "create table table_name(id int auto_increment,name varchar(50),email varchar(50),phone bigint(10),primary key(id))"




# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='create table table_name(id int auto_increment,name varchar(50),email varchar(50),phone bigint(10),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()    #commit refers to the saving of data permenently after a set changes
# print('table created successfully')

# create a table product_details
# prod_id
# prod_name
# price
# customer_name
# customer_phone

# import pymysql
# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# sql="create table laptop(id int auto_increment,product_name varchar(50),price float(10),customer_name varchar(50),customer_phone bigint(10),primary key(id))"
# mycursor.execute(sql)
# mydb.commit()
# print("table created successfully")