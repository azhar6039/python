#Please download the words1.txt file from the attachment and then create a Python function that takes a text file as input and returns the number of words contained in the text file.
with open('C:/Users/ashaik/Desktop/vscode/python/exercises/words1.txt') as file:
    lines=file.read()
def wordCounter(a):
    count=a.split()
    return len(count)
s=wordCounter(lines)
print(s)

