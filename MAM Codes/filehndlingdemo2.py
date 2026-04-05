from studentclass import *
studlst=[]

with open("student.txt") as fh:
    for ln in fh:
        lst=ln.rstrip("\n").split(",")
        print(lst)
        s=Student(int(lst[0]),lst[1],int(lst[2]),int(lst[3]),int(lst[4]))
        studlst.append(s)
        
s1=Student(15,'Sanjay',77,87,88)
studlst.append(s1)
print(studlst)
print("adding data to the file")


with open("student.txt","w") as fh1:
    for s in studlst:
        sstr=f"{s.get_sid()},{s.get_sname()},{s.get_m1()},{s.get_m2()},{s.get_m3()}\n"
        fh1.write(sstr)


        