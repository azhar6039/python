#checklist = ["Portugal", "Germany", "Spain"] add these to countries missing file and create new file

'''
checklist = ["Portugal", "Germany", "Spain"]
with open("countries_missing.txt","r") as file:
    data=file.readlines()
for i in checklist:
    data.append(i+"\n")
data.sort()
with open("countries_added_missing.txt","w") as file1:
    for i in data:
        file1.write(i)
'''
checklist = ["Portugal", "Germany", "Spain"]       
checklist = [i+"\n" for i in checklist]
with open("countries_missing.txt","r") as file:
    data=file.readlines()
updated_list=sorted(checklist+data)
with open("countries_added_missing.txt","w") as file1:
    for i in updated_list:
        file1.write(i)