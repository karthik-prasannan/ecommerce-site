import pymysql

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id delete'))
# sql='delete from table_name where id=%d'%id
# mycursor.execute(sql)
# mydb.commit()
# print('row deleted')

##delete using product name and customer name?

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# product_name=input('enter the product name')
# customer_name=input('enter customer name')
# sql="delete from laptop where product_name='%s' and customer_name='%s'"%(product_name,customer_name)
# mycursor.execute(sql)
# mydb.commit()
# print('row deleted')


mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='embloyee'
)
mycursor=mydb.cursor()
product_name=input('enter the product name')
customer_name=input('enter customer name')
sql='select product_name,customer_name from laptop'
mycursor.execute(sql)
a=mycursor.fetchall()
for i in a:
    if product_name==i[0] and customer_name==i[1]:
        sql1="delete from laptop where product_name='%s' and customer_name='%s'"%(product_name,customer_name)
        mycursor.execute(sql1)
        mydb.commit()
        print('success')
        break
else:
    print('data not found')

