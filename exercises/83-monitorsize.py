#Write a script that detects and prints out your monitor resolution.
'''
import screeninfo
for m in screeninfo.get_monitors():
    print("width: %s height: %s"%(m.width,m.height))

'''
from screeninfo import get_monitors
x=get_monitors()[0].width
y=get_monitors()[0].height
print(x,y)