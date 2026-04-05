emplst = [{'emp_id':1,'emp_name':'ABC', 'emp_sal':1000, 'skill' : ['java', 'python'], 'dept':{'dno':101, 'dname':'HR'}}, 
          {'emp_id':2,'emp_name':'XYZ', 'emp_sal':2000, 'skill' : ['perl', 'c++'], 'dept':{'dno':102, 'dname':'Sales'}}
          ]

#Add new employee in the list as dictionary
def addNewEmployee():
    emp_id= int(input("Enter the id of the employee : "))
    emp_name= input("Enter the name of the employee : ")
    emp_sal= float(input("Enter the salary of the employee : "))
    dno= int(input("Enter the dept number of the employee : "))
    dname= input("Enter the name of the department : ")
    lst = []
    ans = 'y'
    while ans == 'y':
        skill = input("Enter the skill :")
        lst.append(skill)
        ans = input("continue (y/n)")
    
    emp = {'emp_id':emp_id,'emp_name':emp_name, 'emp_sal':emp_sal, 'skill' : lst, 'dept':{'dno':dno, 'dname':dname}}
    emplst.append(emp)
    print(emp)
    return True
    

def displayAllEmployees(lst = emplst):
    print("Employee Details : ")
    print("*" * 80)
    for e in lst:
        print(f"Employee id:{e['emp_id']}\nEmployee name: {e['emp_name']}")
        print(f"Skills: {",".join(e['skill'])}")
        print(f"Salary : {e['emp_sal']}")
        print(f"Department: {e['dept']['dname']}")
        print("-"*80)


#Generating list based on name
def searchByName(name):
    lst= []
    for e in emplst:
        if e['emp_name'] == name:
            lst.append(e)
    if len(lst)>0:
        return lst
    else:
        return None
    
    
#Display data in sorted order
def sorByName():
    lst = emplst.copy()
    lst.sort(key=lambda e : e['emp_name'])
    displayAllEmployees(lst)
    
def searchById(empid):
    for idx, emp in enumerate(emplst):
        if emp['emp_id'] == empid:
            return idx, emp
    else:
        return -1, None
            
    
def updateSalary(empid,sal):
    pos, emp = searchById(empid)
    if pos != -1:
        emp['emp_sal']= sal
        #lst[pos]['emp_sal'] = sal
        return True
    else:
        return False
    
def deleteEmployee(empid):
    pos, _ = searchById(empid)
    if pos != -1:
        emplst.pop(pos)
        return True
    return False
