import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# c=mydb.cursor()
# id=int(input('enter the id:'))
# name=input('enter the name:')
# sql="select * from table_name where id=%d and name='%s'"%(id,name)
# c.execute(sql)
# fetch=c.fetchone()
# id=fetch[0]
# name=fetch[1]
# print(id,name)


# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='select product_name,price,customer_name from laptop'
# mycursor.execute(sql)
# fetch=mycursor.fetchall()
# print(fetch)


# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql="select price,customer_name,product_name from laptop"
# mycursor.execute(sql)
# fetch=mycursor.fetchall()
# for i in fetch:
#     price=i[1]
#     customer_name=i[2]
#     product_name=i[0]
#     print('price',price,'customer name',customer_name,'product name',product_name)



# sql='select * from table name where not condition'

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# customer_name=input('enter customer name')
# sql="select * from laptop where not customer_name='%s'"%customer_name
# mycursor.execute(sql)
# fetch=mycursor.fetchall()
# print(fetch)


## to update

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id'))
# name=input('enter the name')
# sql="update table_name set name='%s' where id=%d"%(name,id)
# mycursor.execute(sql)
# mydb.commit()
# print('database updated.........')

##multipe data updation

## update customer_name and phone number using id?

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id : '))
# customer_name=input('enter the name : ')
# customer_phone=int(input('enter the number : '))
# sql="update laptop set customer_name='%s',customer_phone=%d where id=%d"%(customer_name,customer_phone,id)
# mycursor.execute(sql)
# mydb.commit()
# print('database updated....')


##update number using email and name
##sql=update table set phone=%d where email='%s'and name='%s'

##update product_price using id and product_name?

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# product_name=input('enter the product name')
# price=int(input('enter the price'))
# sql="update laptop set price=%d where id=%d and product_name='%s'"%(price,id,product_name)
# mycursor.execute(sql)
# mydb.commit()
# print('database updated......')
