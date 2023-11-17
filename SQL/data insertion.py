import pymysql

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# a=int(input('enter the number'))
# for i in range(a):
#     mycursor=mydb.cursor()
#     name=input('enter name')
#     email=input('enter email')
#     phone=int(input('enter phone number'))
#     sql="insert into table_name(name,phone,email)values('%s',%d,'%s')"%(name,phone,email)
#     mycursor.execute(sql)
#     mydb.commit()
# print('data added successfully')


# create a table product_details
# prod_id
# prod_name
# price
# customer_name
# customer_phone

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
#     price=int(input('enter the price'))
#     customer_name=input('enter the name')
#     customer_phone=int(input('enter the phone number'))
#     sql="insert into laptop(product_name,price,customer_name,customer_phone) values('%s',%d,'%s','%d')"%(product_name,price,customer_name,customer_phone)
#     mycursor.execute(sql)
#     mydb.commit()
# print("table created successfully")