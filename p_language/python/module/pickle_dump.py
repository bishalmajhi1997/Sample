# pickle dump
import pickle,students
f=open("students.dat","wb")
s=students.Student(1,"sam",88)
pickle.dump(s,f)
f.close()
