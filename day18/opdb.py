import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='dajidali',
    db='tarena',
    charset='utf8'
)

# 创建游标
cursor = conn.cursor()
# 每次对数据库表作修改, 必须要commit
# 插入
sql_insert1 = 'INSERT INTO departments VALUES (%s, %s)'
sql_insert2 = 'INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s, %s)'
# result = cursor.execute(sql_insert1, (7, '行政部'))
employees = [
    (3, '孙三', 'male', '1990-06-08', '15987963542', 'sunsan@test.com', 2),
    (4, '李四', 'female', '1998-09-12', '13333445566', 'lisi@test.com', 3),
]
cursor.executemany(sql_insert2, employees)
conn.commit()

# 查询
sql_select1 = 'SELECT * FROM departments ORDER BY dep_id'
cursor.execute(sql_select1)
result1 = cursor.fetchone() # 游标会向后移动
print(result1)
result2 = cursor.fetchmany(2)
print(result2)
result3 = cursor.fetchall()
print(result3)

cursor.close()
conn.close()
