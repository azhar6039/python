#Please create an empty file (manually as you normally create Python files) and name it requests.py . Make sure the file has that name exactly.Executing the script will throw an error. Please fix something to make the program print out the expected output. You should not modify the code itself, but something else.
'''
import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])
'''
import requests
 
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
r = requests.get("http://www.pythonhow.com", headers = headers)
print(r.text[:100])