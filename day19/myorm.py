from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "数据库+数据库驱动://帐号:密码@IP:Port/database?charset=utf8"
# 编码: "encoding='utf8'"
# `echo=True`会打印一大堆日志, 方便调试. 生产环境可以关闭.
engine = create_engine('mysql+pymysql://root:dajidali@localhost:3306/tedu?charset=utf8',
                       encoding='utf8', echo=True)

# 声明映射
# 通过声明类, 来定义基类
Base = declarative_base()

# 创建会话类
# ORM访问数据库的句柄被称为session
Session = sessionmaker()
session = Session(bind=engine)


# 有了基类, 就可以创建映射类
# 如果表已经存在并且结构一样, 则不会运行, 也不会报错
# 如果表已存在并且结构不一样, 则运行报错
# 如果要迁移或修改数据库, 应该使用模块 alembic
class Departments(Base):
    # 在对应数据库种创建的表名
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    # String对应的数据库类型就是 VARCHAR
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return '<Department(dep_name={})>'.format(self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    gender = Column(String(10))
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '<Employee(emp_name={})>'.format(self.emp_name)


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    award = Column(Integer)

    def __str__(self):
        return '<Salary(emp_id={}, basic={}, award={})>'.format(self.emp_id,
                                                    self.basic, self.award)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
