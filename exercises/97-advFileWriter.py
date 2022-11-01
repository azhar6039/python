#take input recursively from user and append to a file and save the content when user gives "SAVE" and needs to end the program if value is CLOSE. and continue to append when we ran for next time
file=open("adv_file_writer.txt","a+")
while True:
    data=input("enter a value: ")
    if data=="SAVE":
        file.close()
        file=open("adv_file_writer.txt","a+")
    elif data=="CLOSE":
        break
    else:
        file.write(data+"\n")
