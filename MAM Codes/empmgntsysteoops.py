from personclass import *
emplst=[]

def addNewEmployee(ch):
    pid=int(input("enter pid"))
    pnm=input("enetr pname")
    m=input("enetr mobile")
    em=input("enetr email")
    dt=input("enetr dept")
    dg=input("enetr desg")
    if ch==1:
        s=float(input("enter salary"))
        e=SalariedEmp(pid,pnm,m,em,dt,dg,s)
    elif ch==2:
        hrs=float(input("enter hrs"))
        c=float(input("enter charges"))
        e=ContractEmp(pid,pnm,m,em,dt,dg,hrs,c)
    emplst.append(e)
    return True

#search the employee on id, and return
#pos and emp object
def searchById(eid):
    for pos,e in enumerate(emplst):
        if(e.get_pid()==eid):
            return pos,e
    else:
        return -1,None

#find salary of given empid
def getSalary(eid):
    pos,emp=searchById(eid)
    if emp!=None:
        return emp.calculateSal(),True
    else:
        return 0.0,False
        
#find bonus of given empid   
def getBonus(eid):
    pos,emp=searchById(eid)
    if emp!=None and isinstance(emp,SalariedEmp):
        return emp.calculateBonus(0.10)
    else:
        return 0.0,False
    
    
#modify sal and desg based on id
def modifyById(eid,nsal,ndg):
    pos,emp=searchById(eid)
    if emp!=None:
        emp.set_desg(ndg)
        if isinstance(emp, SalariedEmp):
            emp.set_sal(nsal)
            
        elif isinstance(emp, ContractEmp):
            emp.set_charges(nsal)
        return True
    else:
        return False
    
def deletebyId(eid):
    pos,emp=searchById(eid)
    if pos!=-1:
        ans=input("do you want to delete(y/n)")
        if ans=="y":
           emplst.pop(pos)
           return 1
        else: 
           return 2
    else:
        return 3
        
    
def displayAll(lst=emplst):
    for emp in lst:
        print(emp)
    

choice=0
while choice!=9:
    choice=int(input("""
                     1. Add new employee
                     2. delete employee
                     3. modify employee
                     4. display all
                     5. display by id
                     6. display by name
                     7. calaculate salary
                     8. calculate bonus
                     9. exit
                     choice: """))
                     
    match choice:
        case 1:
            ch=int(input("1. Salaried \n 2. Contract\n 3. vendor"))
            status=addNewEmployee(ch)
            if status:
                print("Employee added")
            else:
                print("employee not added")
        case 2:
            eid=int(input("enetr empid"))
            status=deletebyId(eid)
            if status==1:
                print("deleted successfully")
            elif status==2:
                print("Found but not deleted")
            else:
                print("not found")
        case 3:
            eid=int(input("enetr empid"))
            nsal=float(input("enter new sal"))
            ndg=input("enter designation")
            status=modifyById(eid,nsal,ndg)
            if status:
                print("modification done")
            else:
                print("not found")
        case 4:
            displayAll()
            
        case 5:
            pass
        case 6:
            pass
        case 7:
            eid=int(input("enetr empid"))
            s,status=getSalary(eid)
            if status:
                print("salary : ",s)
            else:
                print("Not found")
            
        case 8:
            eid=int(input("enetr empid"))
            s,status=getBonus(eid)
            if status:
                print("Bonus : ",s)
            else:
                print("Not found")
            
        case 9:
            print("Thank you for visiting......")
        case others:
            print("wrong choice")
        