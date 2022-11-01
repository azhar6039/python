#write a script that extracts letters from 26 files and match the letters in string python and print them only
import glob
files=glob.glob("letters/*.txt")
string="python"
list2=[]
for i in files:
    with open(i,"r") as file:
        char=file.read().strip("\n")
        if char in string:
            list2.append(char)

print(list2)