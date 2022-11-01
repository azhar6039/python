#take input recursively from user and append to a file and needs to end the program if value is CLOSE. and continue to append when we ran for next time
file=open("file_writer.txt","a+")

while True:
    data=input("enter a value:")
    if data !="CLOSE":
        file.write(data+"\n")
        continue
    else:
        break