#access the database and print the countries having more than 2,000,000 area

'''
import sqlite3
import pandas as pd
con=sqlite3.connect('database.db')
df =pd.read_sql_query("Select * from countries", con)
df2=df.loc[df['area']>2000000 , 'country']
print(df2)
'''
import sqlite3
con=sqlite3.connect('database.db')
cur=con.cursor()
cur.execute('select country from countries where area>=2000000')
row=cur.fetchall()
con.close()
for i in row:
    print(i[0])