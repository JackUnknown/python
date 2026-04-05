#import studentclass as s1
from studentclass import Student
studlst=[]

def addNewStudent():
    sid=int(input("enter id"))
    sname=input("enetr name")
    m1=float(input("enter m1"))
    m2=float(input("enter m2"))
    m3=float(input("enter m3"))
    s=Student(sid,sname,m1,m2,m3)
    studlst.append(s)
 
def displayAll(lst=studlst):
    for s in lst:
        print(s)
    
def searchById(sid):
    for idx,s in enumerate(studlst):
       if s.get_sid()==sid: 
           return idx,s
    else:
        return -1,None



choice=0
while choice!=4:
    choice=int(input("""
                     1. add Student
                     2. display all
                     3. display by id
                     4.exit
                     choice:
                     """))
    match choice:
        case 1:
            status=addNewStudent()
            if status:
                print("student added")
            else:
                print("student not added")
            
        case 2:
            displayAll()
            pass
        case 3:
            sid=int(input("enetr id"))
            pos,stud=searchById(sid)
            if stud!=None:
                print(stud)
            else:
                print(f"Student with id {sid} not found");
            pass
        case 4:
            print("Thank you for visiting...")
            pass
        case others:
            print("wrong choice")
        
        
        
        
        