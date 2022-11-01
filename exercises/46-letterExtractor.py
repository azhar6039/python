#write a script that extracts letters from 26 files and print as list
from string import ascii_lowercase


list=[]
for i in ascii_lowercase:
    with open("letters/"+i+".txt","r") as file:
        line=file.read().strip("\n")
        list.append(line)

print(list)