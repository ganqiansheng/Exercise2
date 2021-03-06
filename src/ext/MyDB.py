import os.path
import sys
from PyQt5.QtSql import QSqlDatabase,QSqlQuery

def CreateDB():
    db= QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('./db/database.db')
    if not db.open():
        print('无法建立数据库连接')
        return False

    query=QSqlQuery()

    # 添加表student
    query.exec("create table student(ID int primary key,name varchar(20),sex varchar(2),age int, major varchar(20))")

    # 添加记录
    query.exec("insert into student values(1,'张三1','男',20,'计算机')")
    query.exec("insert into student values(2,'李四1','男',19,'经管')")
    query.exec("insert into student values(3,'王五1','男',22,'机械')")
    query.exec("insert into student values(4,'赵六1','男',21,'法律')")
    query.exec("insert into student values(5,'小明1','男',20,'英语')")
    query.exec("insert into student values(6,'小李1','女',19,'计算机')")
    query.exec("insert into student values(7,'小张1','男',20,'机械')")
    query.exec("insert into student values(8,'小刚1','男',19,'经管')")
    query.exec("insert into student values(9,'张三2','男',21,'计算机')")
    query.exec("insert into student values(10,'张三3','女',20,'法律')")
    query.exec("insert into student values(11,'王五2','男',19,'经管')")
    query.exec("insert into student values(12,'张三4','男',20,'计算机')")
    query.exec("insert into student values(13,'小李2','男',20,'机械')")
    query.exec("insert into student values(14,'李四2','女',19,'经管')")
    query.exec("insert into student values(15,'赵六3','男',21,'英语')")
    query.exec("insert into student values(16,'李四2','男',19,'法律')")
    query.exec("insert into student values(17,'小张2','女',22,'经管')")
    query.exec("insert into student values(18,'李四3','男',21,'英语')")
    query.exec("insert into student values(19,'小李3','女',19,'法律')")
    query.exec("insert into student values(20,'王五3','女',20,'机械')")
    query.exec("insert into student values(21,'张三4','男',22,'计算机')")
    query.exec("insert into student values(22,'小李2','男',20,'法律')")
    query.exec("insert into student values(23,'张三5','男',19,'经管')")
    query.exec("insert into student values(24,'小张3','女',20,'计算机')")
    query.exec("insert into student values(25,'李四4','男',22,'英语')")
    query.exec("insert into student values(26,'赵六2','男',20,'机械')")
    query.exec("insert into student values(27,'小李3','女',19,'英语')")
    db.close()
    return True

if __name__=='__main__':
    CreateDB()