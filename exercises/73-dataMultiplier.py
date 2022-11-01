# get data from https://pythonhow.com/media/data/sampledata.txt and multiply data by 2 and save it in new file
#Hint: The easiest way to do this is with pandas.
'''
import requests
url="https://pythonhow.com/media/data/sampledata.txt"
response=requests.get(url)
data=response.text
with open("exercises/sampledata.txt","w") as file:
    for i in data:
        if i.isnumeric():
            file.write(str(int(i)*2))
        else:
            file.write(i)
'''
import pandas
data=pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2=data*2
data2.to_csv("exercises/sampledata.txt",index=0)