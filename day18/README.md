# 数据库

## 介绍

### 持久存储

3种存储机制:

- 文件
- 数据库
- 其他的一些变种
    - 现有系统的API
    - ORM
    - 文件管理器
    - 电子表格
    - 配置文件
    
### 基本的数据库操作和SQL语言

1. 底层存储(文件系统)
2. 用户界面(命令行, GUI)
3. 数据库(基于服务器, 基于文件的)
4. 组件(有些数据库使用游标的概念来表示SQL命令 查询 取回结果等)
    1. 插入
    2. 更新
    3. 删除
    4. 查询
5. SQL(绝大多数大小写不敏感)(基本风格: 关键字大写, 使用分号来结束一条sql语句)

#### SQL(结构化查询语言)

1. 创建数据库:
    ```sql
    CREATE DATABASE test;
    GRANT ALL ON test.* to user(s);
    ```
2. ...

### ER 模型(实体, 关系)

ER图:

- 方框: 实体集
- 关系: 菱形(一对一, 一对多)
- 属性: 椭圆

### 数据库範式

第一范式, 第二, 第三, 巴斯科德, 第四, 第五

**第一范式**:
原子性, 不可再分.

**第二...*:
以第一为基础
要求实体的属性完全依赖于主关键字.
要求数据库表中的每个实例或记录必须被唯一的区分

##第三...**:
非主属性不依赖与其他的非主属性(基于第二...)

### 数据库约束

- 主键约束
    - 主关键字
    - 只有一列被指定为主关键字, image和text类型不能被指定为主关键字
    - 不允许指定主关键字列有NULL属性
- 外键约束(表之间的关系)
    - 一个表种的一个列或多个列的组合和其他表中的主关键字相同
- 唯一性约束
    - 某一列唯一性
- 检查约束
    - 自定义的检查条件
- 非空约束
    - 如姓名

## mysql(mariadb)

1. 安装: `yum install -y mariadb-server`
2. 启动服务: `systemctl start mariadb`
3. 设置开机自启动: `systemctl enable mariadb`
4. 默认用户名为root, 密码为空. 修改root密码为: dajidali  `mysqladmin password dajidali`
5. 登陆数据库: `mysql -uroot -pdajidali`

**查看数据库**:
```
MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| test               |
+--------------------+
4 rows in set (0.00 sec)

```

**创建数据库:**
```
MariaDB [(none)]> CREATE DATABASE tarena DEFAULT CHARSET utf8;
Query OK, 1 row affected (0.00 sec)
```

**切换数据库:**
```
MariaDB [(none)]> USE tarena;
Database changed
```

**查看表:**
```
MariaDB [tarena]> SHOW TABLES;
Empty set (0.00 sec)
```

**创建表:**
```sql
CREATE TABLE departments (dep_id INT(4), dep_name VARCHAR(20));
```

**查看表结构:**
```
MariaDB [tarena]> DESC departments;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| dep_id   | int(4)      | YES  |     | NULL    |       |
| dep_name | varchar(20) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```

**删除表**:
`DROP TABLE departments;`

**创建更多约束的表**:
`CREATE TABLE departments (dep_id INT(4), dep_name VARCHAR(20) NOT NULL UNIQUE, PRIMARY KEY(dep_id));`

**创建员工表:** 外键

`CREATE TABLE employees(emp_id INT(4), emp_name VARCHAR(20) NOT NULL, gender ENUM('male', 'female'), birth_date DATETIME, phone_number VARCHAR(11), email VARCHAR(50), dep_id INT(4), PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id));`

**创建工资表**:
`CREATE TABLE salary(auto_id INT(4) AUTO_INCREMENT, date DATETIME, emp_id INT(4), basic INT(4), award INT(4), PRIMARY KEY(auto_id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id));`

**查看创建表的语句**:
```
MariaDB [tarena]> SHOW CREATE TABLE salary;
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table  | Create Table                                                                                                                                                                                                                                                                                                                                                                       |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| salary | CREATE TABLE `salary` (
  `auto_id` int(4) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `emp_id` int(4) DEFAULT NULL,
  `basic` int(4) DEFAULT NULL,
  `award` int(4) DEFAULT NULL,
  PRIMARY KEY (`auto_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 |
+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

```sql
INSERT INTO departments VALUES (1, '人事部');
INSERT INTO salary (date, emp_id, basic, award) VALUES ('2018-02-10', 1, 10000, 2000);
DELETE FROM departments WHERE dep_id=3;
UPDATE departments SET dep_name='人力资源部' WHERE dep_name='人事部';
INSERT INTO departments VALUES (2, '行政部'), (3, '运维部'), (4, '财务部'), (5, '市场部'), (6, '销售部');
SELECT * FROM departments ORDER BY dep_id;
SELECT * FROM departments ORDER BY dep_id DESC ;
SELECT * FROM departments ORDER BY dep_id LIMIT 3;
SELECT * FROM departments ORDER BY dep_id LIMIT 3, 2; # m,n 起始值(从0开始)m, 偏移n
SELECT emp_name, phone_number FROM employees;
SELECT emp_name AS 姓名, phone_number AS 电话号码 FROM employees;
SELECT date, emp_id, basic+salary.award FROM salary;
SELECT date, emp_id, basic+salary.award FROM salary WHERE basic+salary.award > 20000;
SELECT e.emp_name, s.date, s.basic+s.award AS money FROM employees as e JOIN salary s ON e.emp_id = s.emp_id;
SELECT count(*) FROM departments;
```

## PyMySQL模块

安装`pip install pymysql`
可以设置`~/.pip/pip.conf`为:

```
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host = mirrors.aliyun.com
```

## 下周

sql archemy...