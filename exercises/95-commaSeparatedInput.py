# get user input comma separated and add them to a file , if user runs again , new value need to be appended
input=input("enter values :")
data=input.split(',')
with open("comma_separated.txt","a+") as file:
    for i in data:
        file.write(i+"\n")
