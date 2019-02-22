import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "ming")

#使用cursor()方法创建游标
cursor = db.cursor()

#SQL查询语句
sql="select * from emp"

#使用execute()方法执行SQL
#cursor.execute("select version()")
cursor.execute(sql)

#获取所有记录列表
result = cursor.fetchall()

#打印结果：
for row in result:
    empno = row[0]
    ename = row[1]
    job = row[2]
    mgr = row[3]
    hiredate = row[4]
    sal = row[5]
    comm = row[6]
    deptno = row[7]

    print("empno=%s, ename=%s, job=%s, mgr=%s, hiredate=%s, sal=%s, comm=%s, deptno=%s" % \
          (empno,ename,job,mgr,hiredate,sal,comm,deptno)
          )

#关闭数据库连接
db.close()