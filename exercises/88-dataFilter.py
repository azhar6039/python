# Create a script that uses the attached countries_by_area.txt  file as data source and prints out the top 5 most densely populated countries
from operator import index
import pandas as pd
data=pd.read_csv("countries_by_area.txt",index_col=0)
df=pd.DataFrame(data)
df['density']=df['population_2013']/df['area_sqkm']
x=df.nlargest(5,'density')
y=x['country'].to_csv(index=False)
print(y[7:])
'''
x=df.sort_values(by='density',ascending=False)
for index, row in x[:5].iterrows():
    print(row["country"])
'''

