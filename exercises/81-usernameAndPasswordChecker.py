#input is password and need to check atleast 1 digit ,1 uppercase and 5 digits lenghth else print password is not fine and print exact reason. but before ask for user name if username is already exits in users.txt ask to give new user name
'''
while True:
    list=[]
    user=input("Enter username: ") 
    with open("users.txt","r") as file:
        data=file.readlines()
    for i in data:
        x=i.strip("\n")
        list.append(x)   
    if user in list:
        print("username already exist")
        continue
    notes=[]
    pas=input("enter password: ")
    if not any(ch.isdigit() for ch in pas):
        notes.append("password needs atleast one digit")
    if not any(ch.isupper() for ch in pas):
        notes.append("password needs atleast one uppercase")
    if len(pas)<5:
        notes.append("password lenth should be min 5")
    if len(notes)==0:
        print("password is fine")
        break
    else:
        print("please note the following")
        for note in notes:
            print(note)

'''
while True:
    user=input("enter user name: ")
    with open ("users.txt","r") as file:
        data=file.readlines()
        usr=[i.strip("\n") for i in data]
    if user in usr:
        print("username already exist")
        continue
    else:
        print("username is fine")
        break
while True:
    notes=[]
    pas=input("enter your password: ")
    if not any(ch.isdigit() for ch in pas):
        notes.append("You need at least one number")
    if not any(ch.isupper() for ch in pas):
        notes.append("You need at least one uppercase")
    if not len(pas)>=5:
        notes.append("You need at least 5 characters")
    if len(notes)==0:
        print("password is fine")
        break
    else:
        print("check the following")
        for note in notes:
            print(note)
        break

        
