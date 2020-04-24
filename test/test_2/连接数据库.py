import pymysql

# 打开数据库
db = pymysql.connect('10.0.51.162','root','Admin@casc.ac.cn','test')

# 使用cursor()方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print ("Database version : %s " % data)

# 关闭数据库
db.close()