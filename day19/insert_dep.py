from day19.sqlalchemy_conn import Departments, engine
from sqlalchemy.orm import sessionmaker


# 创建实例时, 并不会真正在表中添加记录
dep_hr = Departments(dep_name='人事部')
dep_dev = Departments(dep_name='开发部')
dep_ops = Departments(dep_name='运维部')

# 创建会话类
# ORM访问数据库的句柄被称为session
Session = sessionmaker()
session = Session(bind=engine)
# 添加一行
session.add(dep_hr)
# 添加多行, 参数为可迭代对象
session.add_all((dep_dev, dep_ops))
session.commit()
