#print today day,date, momth and year
import pandas as pd
time=pd.to_datetime('today')
month=time.month_name()
year=time.year
day=time.day_name()
date=time.day
print("Today is %s, %s %s,%s"%(day,month,date,year))
time1=time.strftime("%A,%B %d,%Y")
print(time1)