from datetime import datetime

from day19.myorm import Departments, Employees, Salary, session


dep_hr = Departments(dep_name='人事部')
dep_dev = Departments(dep_name='开发部')
emp_bob = Employees(
    emp_name='bob',
    gender='male',
    phone='13355667788',
    email='bob@tedu.cn',
    dep_id=1,
)
salary_bob_201803 = Salary(
    date=datetime.date(datetime.now()),
    emp_id=1,
    basic=10000,
    award=5000
)
session.add_all((dep_hr, dep_dev))
session.commit()
session.add(emp_bob)
session.commit()
session.add(salary_bob_201803)
session.commit()
