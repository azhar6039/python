#input is password and need to check atleast 1 digit ,1 uppercase and 5 digits lenghth else print password is not fine and print exact reason
pas=input("enter your password: ")
if any(ch.isdigit() for ch in pas)==True:
    if any(ch.isupper() for ch in pas)==True:
        if len(pas)>=5:
            print("password is fine")
        else:
            print("please check the following:")
            print("password length is not 5 characters")
    elif len(pas)>=5:
        print("please check the following:")
        print("password should contain atleast one uppercase letter")
    else:
        print("please check the following:")
        print("password length is not 5 characters")
        print("password should contain atleast one uppercase letter")
elif any(ch.isupper() for ch in pas)==True:
    if len(pas)>=5:
        print("please check the following:")
        print("password should contain atleast one number")
    else:
        print("please check the following:")
        print("password length is not 5 characters")
        print("password should contain atleast one number")
elif len(pas)>=5:
    print("please check the following:")
    print("password should contain atleast one uppercase letter")
    print("password should contain atleast one number")
else:
    print("please check the following:")
    print("password length is not 5 characters")
    print("password should contain atleast one uppercase letter")
    print("password should contain atleast one number")

'''
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

'''