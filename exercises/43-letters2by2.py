#Create a script that generates a file where all letters of the English alphabet are listed two in each line.
import string
file=open("text2.txt","w")
x=''
for letter in string.ascii_lowercase:
    x=x+letter
a=x[::2]
b=x[1::2]
print(a)
print(b)
for i,j in zip(a,b):
    z=i+j
    file.write(z+"\n")
