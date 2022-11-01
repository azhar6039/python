#Create a function that takes any string as input and returns the number of words for that string.
def stringspilter(a):
    count=a.split()
    return len(count)
strng=stringspilter("he is a good boy")
print(strng)