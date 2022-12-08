# pickle load/unpickling
import pickle
f=open('students.dat',"rb")
s=pickle.load(f)
s.display()
f.close()