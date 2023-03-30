import pymysql as mysql
con=mysql.connect(user="root",password="root",database="Student",host="localhost")
c=con.cursor()
id=int(input("Enter Id:"))
n=input("Enter Name:")
sql_query="update info set name=%s where id= %s"
arr=(n,id)
c.execute(sql_query,arr)
con.commit()
print('Record Submitted...')
con.close()