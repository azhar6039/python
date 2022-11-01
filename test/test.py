import langid
#lang = langid.classify("Geeksforgeeks是面向极客的计算机科学门户") 
#print(lang)
import openpyxl
mywb = openpyxl.load_workbook('Finaltext.xlsx')
print(mywb.sheetnames)
sheet = mywb.active

text_column = sheet['D']

# Print the contents
for x in range(1,len(text_column)): 
    #print(text_column[x].value)
    lang=langid.classify(str(text_column[x].value))
    sheet["L"+str(x+1)]=str(lang)
    #print(type(lang))
    '''
    if "en" in str(lang):
        sheet["L"+str(x+1)]="English"
    elif "ru" in str(lang):
        sheet["L"+str(x+1)]="Russia"
    else:
        sheet["L"+str(x+1)]=str(lang)
    
    '''
    
mywb.save("test.xlsx")