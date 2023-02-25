import pymysql as mysql
con=mysql.connect(user="root",password="root",database="Student",host="localhost")
c=con.cursor()
id=int(input("Enter Id To Check the Record:"))
sql_query="select * from info where id=%s"
arr=(id,)
c.execute(sql_query,arr)
row=c.fetchone()
if row==None:
    print("Record Not Found....")
else:
    print(row)
con.commit()
con.close()