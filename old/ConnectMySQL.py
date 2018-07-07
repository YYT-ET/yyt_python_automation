import pymysql
# -*- coding: utf-8 -*-
'''
# 打开数据库连接
db=pymysql.connect("localhost","root","111111","python" )
#  使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
#  使用 execute()  方法执行 SQL 查询
cursor.execute("select * from student where id = 3")
#  使用 fetchone() 方法获取单条数据.data = cursor.fetone()
# 获取多条数据
data = cursor.fetchall()
print ( data)
#  关闭数据库连接
db.close()
'''

try:
 db1=pymysql.connect("127.0.0.1","root","111111","python",charset="utf8")
 cursor1 = db1.cursor()
 try:
    cursor1.execute('insert into student(Name,Sex,Age) VALUES ("新建","man",9)')
    db1.commit()
   # data1 = cursor1.fetchall()
   # print(data1)
 except:
     db1.rollback()
 finally:
     db1.close()

except pymysql.err.OperationalError:
    print(pymysql.err.OperationalError)