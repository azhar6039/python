#create a program to generate a password of 6 characters from random from all(char,num,special char)
import random
import string
characters=string.ascii_letters + string.digits + string.punctuation
string1=''
def password(letters):
    global string1
    for i in range(letters):
        string1=string1+random.choice(characters)
    return string1
letters=input("enter number of letters for password: ")
password1=password(int(letters))
print(password1)


'''
import random
 
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)
'''