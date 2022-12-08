# directory contains folders
import os
print(os.getcwd())
# getcwd is get current working directory.
print(os.listdir())

# Create a directory
# os.mkdir("mymm")#mkdir is make directory
# print(os.listdir())

# rename a dir
# os.rename("mymm","myimages")
# print(os.listdir())



# check dir
print(os.getcwd())
check_dir=os.path.isdir("F:\FSD2\Programming\p_language\python\module")
print(check_dir)
# delete/remove the dir
os.rmdir("mypics")
print(os.listdir())
