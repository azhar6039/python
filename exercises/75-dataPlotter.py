#use https://pythonhow.com/media/data/sampledata.txt  and create a data plot
import pandas as pd
import pylab as plt
data=pd.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data.plot.scatter(x='x',y='y',s = 100)
plt.show()