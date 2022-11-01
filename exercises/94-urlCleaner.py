#Please download the attached urls.txt file. The file contains some broken URLs. Here's what the file contains:
#Please use Python to remove the "s" from "https" and add another forward slash next to the existing slash, so the content looks like in the expected output.
#http://www.google.com output for 
'''input (https:/www.google.com
https:/www.yahoo.com
https:/www.stackoverflow.com
https:/www.pythonhow.com)'''
with open("urls.txt","r") as file:
    data=file.readlines()
with open("urls.txt","w") as file:
    for i in data:
        x=i.replace("https","http")
        y=x[:5]+'/'+x[5:]
        file.write(y)
