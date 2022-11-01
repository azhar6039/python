# Please download the attached countries-raw.txt file. The file contains the list of country names, but it also contains some unnecessary text among the countries. 
#Please clean the list with Python by generating a new text file that contains a flawless list of country names without any other text or brake lines in it. The new file content should look like in the expected output.
# Load the existing file content to a list and then use list comprehensions with if statements inside to iterate through the list items and check the items if they are equal to things like "Top of Page," "\n" and so on.
with open("countries_raw.txt","r") as file:
    data=file.readlines()
data=[i.strip("\n") for i in data]
data=[i for i in data if i !=""]
data=[i for i in data if len(i)!=1]
data=[i for i in data if i!="Top of Page"]
with open("countries-clean.txt","w") as file1:
    for i in data:
        file1.write(i+"\n")
'''
with open("countries_raw.txt","r") as file:
    data= file.readlines()
    list=[]
    for i in data:
        x=i.strip("\n")
        list.append(x)
for i in list:
    if i=='':
        list.remove(i)
for i in list:
    if len(i)==1:
        list.remove(i)
for i in list:
    if i =="Top of Page":
        list.remove(i)
with open("countries-clean.txt","w") as file1:
    for i in list:
        file1.write(i+"\n")

'''