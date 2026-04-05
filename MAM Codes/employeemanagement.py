emplst=[{'empid': 16, 'ename': 'sanjay', 'sal': 55444.0, 'skill': ['java'], 'dept': {'dno': 121, 'dname': 'HR'}},{'empid': 14, 'ename': 'Gauri', 'sal': 45678.0, 'skill': ['Excel', 'Word', 'gmail'], 'dept': {'dno': 122, 'dname': 'Admin'}}]

#add new employee in the list as dictionary
def addnewEmployee():
    empid=int(input("enetr id"))
    ename=input("enetr name")
    sal=float(input("enter salary"))
    dno=int(input("enter dno"))
    dname=input("enter dname")
    lst=[]
    ans='y'
    while ans=='y':
        skill=input("enter skill")
        lst.append(skill)
        ans=input("continue (y/n)")
    
    emp={'empid':empid,'ename':ename,'sal':sal,'skill':lst,'dept':{'dno':dno,'dname':dname}}  
    emplst.append(emp)
    print(emp)
    return True

#generate list based on name
def searchByName(name):
    lst=[]
    for e in emplst:
        if e['ename']==name:
            lst.append(e)
    if len(lst)>0:
        return lst
    else:
        return None
    
#display data in sorted order
def sortByName():
    lst=emplst.copy()
    lst.sort(key=lambda e:e['ename'])
    displayAll(lst)

#search by id and return position and emp dictionary
def searchById(empid):
    for idx,emp in enumerate(emplst):
        if emp['empid']==empid:
            return idx,emp
    else:
        return -1,None
    
#update salary by id
def updateById(empid,sal):
    pos,emp=searchById(empid)
    if pos!=-1:
        emp['sal']=sal
        #emplst[pos]['sal']=sal
        return True
    else:
        return False
        
#display all employees
def displayAll(lst=emplst):
     for e in lst:
         print(f"empid: {e['empid']} ,ename: {e['ename']} Salary : {e['sal']}")
         print(f"Skills: {",".join(e['skill'])}")
         print(f"Department: {e['dept']['dname']}")
         print("-"*80)

choice=0
while choice!=8:
    print(emplst)
    choice=int(input("""
                     1. add new employee
                     2. delete the employee
                     3. update salary
                     4. display in  sorted order of name
                     5. display all
                     6. search by id
                     7. search by name
                     8. exit
                     choice:
                     """))
    match choice:
        case 1:
            status=addnewEmployee()
            if status:
                print("employee addeds")
            else:
                print("employee not added")
        case 2:
            pass
        case 3:
            empid=int(input("enter empid to modify sal"))
            sal=float(input("enter sal"))
            status=updateById(empid,sal)
            if status:
                print("updated successfully")
            else:
                print("not found")
        case 4:
            sortByName()
        case 5:
            displayAll()
            pass
        case 6:
            pass
        case 7:
            name=input("enter name to search")
            lst=searchByName(name)
            if lst!=None:
                displayAll(lst)
            else:
                print("Not found")
        case 8:
            print("Thank you for visiting....")
        case others:
            print("wrong choice")
        
