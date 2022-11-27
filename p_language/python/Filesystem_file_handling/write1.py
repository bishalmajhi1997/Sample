# writing multiple strings to the file
f=open("myfile1.txt","w")
print("enter the txt,type # when you are done")
s=" "
while s!="#":
    s=input()
    f.write("\n")
    f.write(s)
f.close()