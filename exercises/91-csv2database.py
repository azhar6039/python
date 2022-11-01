#add ten more countries file o the database
import sqlite3
import pandas as pd
con=sqlite3.connect('database.db')
cur=con.cursor()

data=pd.read_csv('ten_more_countries.txt')
df=pd.DataFrame(data)
#df.to_sql('countries',con=con , if_exists='append',  index=False)
for index,row in data.iterrows():
    print(row["Country"],row['Area'])
    cur.execute("insert into countries values(NULL,?,?,NULL)",(row["Country"],row['Area']))
con.commit()
con.close()