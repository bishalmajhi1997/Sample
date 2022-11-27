# File are where we store or organise our data.
# opening a file 
# f=open("filename","mode")
# closing a file:
# f.close()
# models
# w=write to a file .Everyone it write new content to the file.
# r=read from the file
# append to the file.current contents are not overridden.
# binary files
# wb,rb,ab
# write string to a file
f=open("myfile.txt","w")
s=input("Enter text:")
f.write(s)
f.close()
# reading in file
f=open("myfile.txt","r")
s=f.read()
print(s)
f.close()
