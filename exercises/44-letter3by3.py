import string
with open("text3.txt","w") as file:
    str=string.ascii_lowercase+" "
    for i,j,k in zip(str[::3],str[1::3],str[2::3]):
        file.write(i+j+k+"\n")

