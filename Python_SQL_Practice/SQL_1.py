import pymysql as mysql
con=mysql.connect(user="root",password="root",database="Student",host="localhost")
c=con.cursor()
sql_query="insert into info values(5,'rdj')"
c.execute(sql_query)
con.commit()
print('Record Submitted...')
con.close()