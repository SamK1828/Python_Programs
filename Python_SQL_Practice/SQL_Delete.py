import pymysql as mysql
con=mysql.connect(user="root",password="root",database="Student",host="localhost")
c=con.cursor()
id=int(input("Enter the Id To be Deleted:"))

sql_query="delete from info where id=%s"
arr=(id,)
c.execute(sql_query,arr)
con.commit()
print('Record Submitted...')
con.close()