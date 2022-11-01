#Please complete the code so that it prints out the expected output.

a = [1, 2, 3] 

for i in range (0,len(a)):
    print("Item "+ str(a[i])+" has index "+ str(i) )

for index,item in enumerate(a):
    print("Item %s has index %s" % (item,index))