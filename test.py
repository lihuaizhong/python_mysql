import pymysql
db = pymysql.connect("118.24.219.83","root","zabbixpwd","taobao")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用预处理语句创建表
sql="""CREATE TABLE student3 (id tinyint(5) zerofill auto_increment not null comment '学生学号', name varchar(20) default null comment '学生姓名', age tinyint default null comment '学生年龄', class varchar(20) default null comment '学生班级', sex char(5) not null comment '学生性别', unique key (id) )engine=innodb charset=utf8;; """ 
sql="""CREATE TABLE employee( empno INT PRIMARY KEY comment '雇员编号', ename VARCHAR(20) comment '雇员姓名', job VARCHAR(20) comment '雇员职位', mgr INT comment '雇员上级编号', hiredate DATE comment '雇佣日期', sal DECIMAL(7,2) comment '薪资', deptnu INT comment '部门编号' );"""
sql=""" select * from employee where ename in ('猴子','张飞');"""
re=cursor.execute(sql)
re = cursor.fetchall()
for row in re:
    print(row[0])
# 关闭数据库连接
db.close()
