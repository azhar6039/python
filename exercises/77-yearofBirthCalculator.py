#Create a script that asks the user to enter their age, and the script calculates the user's year of birth and prints it out in a string like in the expected output. Please make sure you generate the current year dynamically.
#https://strftime.org/
import pandas as pd
age=input("please enter your current age:")
time=pd.to_datetime('today').strftime("%Y")
b_year=int(time)-int(age)
print("We think you were born back in %s"%b_year)

'''

from datetime import datetime
 
age = int(input("What's your age? "))
year_birth = datetime.now().year - age
print("We think you were born back in %s" % year_birth)
'''