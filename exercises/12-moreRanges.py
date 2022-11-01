#Complete the script so that it produces the expected output. Please use my_range  as input data.
my_range =range(1, 21)
list=[]
for i in my_range:
    sum=i*10
    list.append(sum)
print(list)

"""
list compreshion
my_range = range(1, 21)
print([10 * x for x in my_range])
"""