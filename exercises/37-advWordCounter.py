#Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
def advWordCounter(a):
    with open(a) as file:
        lines=file.read()
        x=lines.replace(',', ' ')
        
        count=x.split()
        return len(count)
print(advWordCounter('C:/Users/ashaik/Desktop/vscode/python/exercises/words2.txt'))