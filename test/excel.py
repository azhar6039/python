import langdetect
#print(langdetect.detect("Geeksforgeeks is a computer science portal for geeks"))
import openpyxl
mywb = openpyxl.load_workbook('sample.xlsx')
print(mywb.sheetnames)
sheet = mywb.active

text_column = sheet['A']

# Print the contents
for x in range(1,len(text_column)): 
    #print(text_column[x].value)
    lang=langdetect.detect(text_column[x].value)
    print(type(lang))
    if lang=="en":
        sheet["B"+str(x+1)]="English"
    elif lang=="ru":
        sheet["B"+str(x+1)]="Russia"
    else:
        sheet["B"+str(x+1)]=lang
    
mywb.save("test.xlsx")