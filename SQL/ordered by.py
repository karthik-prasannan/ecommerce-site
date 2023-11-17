# ordered by in mysql is a keyword that is used to sort records in ascenting order or in descenting order

import pymysql

### ascenting order?

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='select * from table_name order by name'
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     id=i[0]
#     name=i[1]
#     email=i[2]
#     phone=i[3]
#     print('id=',id,'name=',name,'email=',email,'phone=',phone)

# select product name and price from product table order the product by price?

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='select product_name,price from laptop order by price'
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     product_name=i[0]
#     price=i[1]
#     print('product name=',product_name,'price=',price)

###descenting order

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='select product_name,price from laptop order by price desc'
# mycursor.execute(sql)
# data=mycursor.fetchall()
# for i in data:
#     product_name=i[0]
#     price=i[1]
#     print('product name=',product_name,'price=',price)


mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='embloyee'
)
mycursor=mydb.cursor()
sql='select customer_name,product_name from laptop order by customer_name asc,product_name desc'
mycursor.execute(sql)
data=mycursor.fetchall()
for i in data:
    customer_name=i[0]
    product_name=i[1]
    print('customer_name=',customer_name,'product name=',product_name)
