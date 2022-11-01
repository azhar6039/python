r=int(input())
if(r%2==1):
    print('Weird')
elif r%2==0 and 2<=r<=5:
    print('Not Weird')
elif r%2==0 and 6<=r<=20:
    print('Weird')
else:
    print('Not Weird')