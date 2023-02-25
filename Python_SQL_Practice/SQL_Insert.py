import pymysql as mysql
con=mysql.connect(user="root",password="root",database="Student",host="localhost")
c=con.cursor()
id=int(input("Enter Id:"))
n=input("Enter Name:")
sql_query="insert into info values(%s,%s)"
arr=(id,n)
c.execute(sql_query,arr)
con.commit()
print('Record Submitted...')
con.close()