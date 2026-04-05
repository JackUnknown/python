from studentclass import *

studlst=[]

def readfromfile(fname):
    with open(fname) as fh:
        for ln in fh:
            lst = ln.rstrip('\n').split(',')
            print(lst)
            s = Student(int(lst[0]), lst[1],int(lst[2]), int(lst[3]), int(lst[4]))
            studlst.append(s)

def writetofile(fname):
    with open(fname,'w') as fh1:
        for s in studlst:
            stud_str = f"{s.get_sid()},{s.get_sname()},{s.get_m1()},{s.get_m2()},{s.get_m3()}\n"
            fh1.write(stud_str)
        

    
readfromfile('student.txt')
s1 = Student(4,'MNO',10,20,30)     
studlst.append(s1)
print('adding adtato the file')

writetofile('student.txt')