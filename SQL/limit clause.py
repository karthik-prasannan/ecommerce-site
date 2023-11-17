import pymysql

# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# limit=int(input('enter the limit'))
# sql="select * from laptop limit %d"%limit       ##doesn't need condition(where).
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     print('id=',id,'name=',name)

#
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# product_name=input('enter the product')
# limit=int(input('enter the limit'))
# sql="select * from laptop where product_name='%s' limit %d"%(product_name,limit)
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     print('id=',id,'name=',name,'price=',price)



