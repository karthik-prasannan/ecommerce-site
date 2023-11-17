import pymysql

# mydb=pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="embloyee"
# )
# mycursor=mydb.cursor()
# sql='select * from table_name'
# # * is a universal symbol that is used to select all datas
# mycursor.execute(sql)
# a=mycursor.fetchall()
# # fetchall():it is used to fetch all datas and return a list of tuple
# print(a)
# for i in a:
#     id=i[0]
#     name=i[1]
#     email=i[2]
#     phone=i[3]
#     print('id=',id,'name=',name,'email=',email,'phone=',phone)


# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='embloyee'
# )
# mycursor=mydb.cursor()
# sql='select * from laptop'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# print(a)
# for i in a:
#     id=i[0]
#     product_name=i[1]
#     price=i[2]
#     name=i[3]
#     number=i[4]
#     print('id=',id,'product name=',product_name,'price=',price,'name=',name,'number=',number)