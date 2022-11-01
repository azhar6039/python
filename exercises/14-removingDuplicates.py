#Complete the script so that it removes duplicate items from the list a
a = ["1", 1, "1", 2]
print(list(set(a)))


"""
a = ["1", 1, "1", 2]
b=[]
for i in a:
    if i  not in b:
        b.append(i)
print(b)

using ordered list
from collections import OrderedDict
a = ["1", 1, "1", 2]
print(list(OrderedDict.fromkeys(a)))

"""