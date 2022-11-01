#Create an English to Portuguese translation program.The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source. In addition, try to return the message, "We couldn't find that word!" when the user enters a word that is not in the dictionary.
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def vocabulory(word):
    if word in d:
        print(d[word])
    else:
        print("That word doesn't exist!")
word=input("enter your word: ")
vocabulory(word)

'''
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def vocabulary(word):
    if word in d:
        return d[word]
    else:
        return "That word doesn't exist!"
word=input("enter your word: ")
print(vocabulary(word))
'''
d = dict(weather = "clima", earth = "terra", rain = "chuva") 
def vocabulary(word):
    try:
        return d[word]
    except:
        return "That word doesn't exist!"


word=input("enter your word: ")
print(vocabulary(word))
