#One of the items is not a country. Please use Python and the file containing the list of countries (attached) as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist , then print it out.
#Please take a look at the following list:

checklist = ["Portugal", "Germany", "Munster", "Spain"]
with open("countries-clean.txt","r") as file:
    data=file.readlines()
    data=[i.strip("\n") for i in data]
for i in checklist:
    if i not in data:
        checklist.remove(i)
print(checklist)
'''
checklist = ["Portugal", "Germany", "Munster", "Spain"]
 
with open("countries-clean.txt", "r") as file:
    content = file.readlines()
 
content = [i.rstrip('\n') for i in content]
checked = [i for i in checklist if i in content]
 
print(checked)
'''
