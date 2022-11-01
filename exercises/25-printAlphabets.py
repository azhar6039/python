import string
for i in range(65,91):
    print(chr(i) ,end='')
print()
for letter in string.ascii_lowercase:
    print(letter , end='')

#string  is a built-in module and string.ascii_lowercase  returns a string object containing all 26 letters of the English alphabet. Then we simply iterate through that string and print out the string item
