#input is password and need to check atleast 1 digit ,1 uppercase and 5 digits lenghth else print password is not fine
str=input("enter a password: ")
if any(ch.isdigit() for ch in str)==True and any(ch.isupper() for ch in str)==True and len(str)>=5:
    print("password is good")
else:
    print("password is not fine")
'''
while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Password is not fine")
'''