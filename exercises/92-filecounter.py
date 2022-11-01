#read number files with .py extension in files folder
import glob
files=glob.glob("files/*.py")
count=0
for i in files:
    count=count+1
print(count)
files1=glob.glob1('files','.py')
print(len(files))