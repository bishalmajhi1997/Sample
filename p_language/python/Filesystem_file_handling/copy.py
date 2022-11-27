# Copy File
f=open("img2.png","rb")
f1=open("horse.png","wb")
for i in f:
    f1.write(i)