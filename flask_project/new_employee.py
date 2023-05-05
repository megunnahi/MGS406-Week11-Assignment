import mysql.connector as sql

conn = sql.connect(host= 'localhost', user = 'James', password = 'bob14228')
cur = conn.cursor()

print(conn)

cmd = "CREATE DATABASE new_employee"
cur.execute(cmd)

conn.close()

conn2 = sql.connect(host = 'localhost', user = 'James', password = 'bob14228', database = 'new_employee')
cur2 = conn2.cursor()

tbl = "CREATE TABLE employee ( EmpID varchar(30) PRIMARY KEY, EmpName varchar(30), EmpGender varchar(30), EmpPhone varchar(30), EmpBdate varchar(30))"
cur2.execute(tbl)

conn2.close()
