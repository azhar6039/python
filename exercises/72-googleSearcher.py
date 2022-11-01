#create a script that let user type a search and open the browser for that search word
#Hint: You could use the webbrowser module for this.
import webbrowser
word=input("enter word for search: ")
webbrowser.open(word)
webbrowser.open("https://www.google.com/search?q="+word)
webbrowser.open("https://google.com/search?q=%s" % word)