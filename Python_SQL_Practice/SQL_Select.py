import pymysql as mysql

con = mysql.connect(user="root", password="root", database="Student", host="localhost")
c = con.cursor()

sql_query = "select * from info"
c.execute(sql_query)
# fetchone
# row=c.fetchone()
# print(row) #print as a tuple....
# print(row[0],row[1]) #print as a element...
# con.commit()

# fetchall
# rows=c.fetchall()
# print(rows)
# for x in rows:
#     print(x)

# fetchmany
# rows=c.fetchmany(4)
# print(rows)
# for r in rows:
#     print(r)
#     print(r[0],r[1])
con.close()
