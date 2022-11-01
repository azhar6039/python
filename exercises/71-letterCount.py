#Count the number of "a" characters in this text file: http://www.pythonhow.com/data/universe.txt
import requests
url="http://www.pythonhow.com/data/universe.txt"
response=requests.get(url)
data=response.text
count_a=data.count("a")
count=0
for i in data:
    if i=="a":
        count=count+1

print(count)
print(count_a)
#both ways work