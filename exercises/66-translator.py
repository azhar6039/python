#Create an English to Portuguese translation program.The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
word=input("enter a word: ")
if word in d:
    print(d[word])
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def vocabulory(word):
    return d[word]
word=input("enter a word: ")
print(vocabulory(word))