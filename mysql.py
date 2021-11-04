# import pymysql
#
#
# # 打开数据库链接
# db = pymysql.connect(host='localhost', user='root', password='', database='cyx', port=3306, charset='utf8')
# # 使用cursor()方法创建一个游标对象
# cursor = db.cursor()
# # 使用execute()方法执行sql,如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # sql语句创建表
# sql = '''create table 2020年每个月的销售情况(     # 根据自己的需要添加字段
#         observation_type varchar(20),
#         observation_point varchar(40),
#         observation_time datetime,
#         average_value float,
#         max_value float,
#         min_value float,
#         momentary_value float,
#         temperature float)
# '''
# cursor.execute(sql)
# db.close()

# import MySQLdb
# import pandas as pd
#
# filePath = 'data.xlsx'
# data = pd.read_excel('data.xlsx')
# con = MySQLdb.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     db='cyx',
#     charset='utf8'
# )
#
# c = con.cursor()  # 游标对象
# query = "insert into 2020年每个月的销售情况 values(%s,%s,%s,%s)"
# for r in range(0, len(data)):
#     observation_point = data.iloc[r, 1]
#     observation_time = data.iloc[r, 2]
#     average_value = data.iloc[r, 3]
#     max_value = data.iloc[r, 4]
#     min_value = data.iloc[r, 5]
#     momentary_value = data.iloc[r, 6]
#     temperature = data.iloc[r, 7]
#
#     values = (
#         observation_type, observation_point, observation_time, average_value, max_value, min_value, momentary_value,
#         temperature)
#     c.execute(query, values)
#
# con.commit()
# con.close()
