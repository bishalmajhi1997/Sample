#append file-current contents will not be deleted
f=open("myfile2.txt","a")
s=input("Enter text:")
f.write(s)
f.close()
