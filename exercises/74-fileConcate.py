#Please concatenate https://pythonhow.com/media/data/sampledata.txt with https://pythonhow.com/media/data/sampledata_x_2.txt to a single text file. The content of the output file should look like below.
import pandas
data=pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2=pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
data3=pandas.concat([data,data2])
data3.to_csv("exercises/sampledata2.txt",index=0)