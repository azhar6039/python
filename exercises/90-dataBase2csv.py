#connect to database and get all rows which have area more than 2000000 and export to csv

'''
import sqlite3
import pandas as pd
conn=sqlite3.connect('database.db')
sql_query=pd.read_sql_query('select * from countries where area>=2000000',conn)
df=pd.DataFrame(sql_query)
df.to_csv("exported-data.csv",index=False)
'''
import sqlite3
import pandas as pd
conn=sqlite3.connect('database.db')
cur=conn.cursor()
cur.execute('select * from countries where area>=2000000')
rows=cur.fetchall()
conn.close()

df=pd.DataFrame.from_records(rows)
df.columns=["Rank","COUNTRY","AREA","POPULATION"]
df.to_csv("exported-data.csv",index=False)