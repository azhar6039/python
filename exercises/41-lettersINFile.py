#Create a script that generates a text file with all letters of the English alphabet inside it, one letter per line.
file=open("text.txt","w")
line=[]
for i in range(65,91):
    line.append(chr(i)+'\n')
file.writelines(line)