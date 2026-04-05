from personClass import *

emplst=[]

def displayAll(lst = emplst):
    for emp in lst:
        print(emp)

def addNewEmployee(ch):
    pid = int(input('Enter PID: '))
    name = input('Enter Name: ')
    mobno = int(input('Enter mobile number: '))
    email = input('Enter email: ')
    dept = input('Enter dept: ')
    desg = input('Enter desg: ')
    
    if ch == 1:
        salary=float(input('Enter salary: '))
        e = SalariedEMP(pid,name,mobno,email, dept,desg, salary)
        pass
    elif ch == 2:
        hrs = float(input('Enter hours: '))
        charges =float(input('Enter charges: '))
        e = ContractEMP(pid,name,mobno,email, dept,desg, hrs,charges)
    
    emplst.append(e)
    return True


def searchById(eid):
    for pos, e in enumerate(emplst):
        if e.get_pid() == eid:
            return pos,e
    else:
        return -1, None
    
def searchByName(ename):
    for pos, e in enumerate(emplst):
        if e.get_pname() == ename:
            return pos,e
    else:
        return -1, None

def getSalary(eid):
    pos, emp = searchById(eid)
    if emp!= None:
        return emp.calculateSal(), True
    else:
        return -1, None
    
def getBonus(eid):
    pos, emp = searchById(eid)
    if emp!= None and isinstance(emp,SalariedEMP):
        return emp.calculateBonus(0.10), True
    else:
        return 0.0, False


def modifyById(eid,new_salary,new_desg):
    pos, emp = searchById(eid)
    if emp!= None:
        emp.set_desg(new_desg)
        if isinstance(emp, SalariedEMP):
            emp.set_salary(new_salary)
        elif isinstance(emp, ContractEMP):
            emp.set_charges(new_salary)
            
    return True


def deleteById(eid):
    pos, emp = searchById(eid)
    if pos!= -1:
        ans = input('Do you want to delete (y/n)') 
        if ans == 'y':
            emplst.pop(pos)
            return 1
        else:
            return 2
    else:
        return 3
    
choice = 0

while choice != 9:
    choice = int(input(''' 
1. Add new Employee
2. Delete employee
3. Modify employee
4. Display all
5. Display by id
6. Display by name
7. Calculate Salary
8. Calculate Bonus
9. Exit
                       
Enter your Choice: 
'''))
    match choice:
        case 1: 
            ch = int(input('''
                           1. Salried
                           2. Contract 
                           3. Vendor
                           
                           Enter your choice:
                           '''))
                        
            status = addNewEmployee(ch)
            if status:
                print("Employee Added")
            else:
                print('Employee not added')
            
        case 2: 
            eid = int(input('Enter emp id: '))
            status = deleteById(eid)
            if status == 1:
                print('Found Delete sucessful')
            elif status == 2:
                print('Found and not Delete')
            elif status == 3:
                print('Not found')
            
        case 3: 
            eid = int(input('Enter emp id: '))
            new_salary = int(input('Enter new salary: '))
            new_desg = input('Enter new desg: ') 
            
            status = modifyById(eid,new_salary,new_desg)
            if status:
                print('Modification done')
            else:
                print('Not found')
            
        case 4: 
            displayAll()
            
        case 5: 
            eid = int(input("\tEnter the emp id: "))
            pos, emp = searchById(eid)
            if pos != -1:
                print(emp)
            else:
                print('Not found') 
            
        case 6: 
            ename = input("Enter the emp name: ")
            pos, emp = searchByName(ename)
            if pos != -1:
                print(emp)
            else:
                print('Not found') 
            pass
        case 7: 
            eid = int(input('Enter emp id: '))
            salary, status = getSalary(eid)
            if status:
                print('Salary : ' , salary)
            else:
                print('Not found')
            
        case 8: 
            eid = int(input('Enter emp id: '))
            bonus, status = getBonus(eid)
            if status:
                print('Bonus : ' , bonus)
            else:
                print('Not found')
            
        case 9:  
            print('Exitng......')
            pass
        case others: 
            print('Wrong choice')
            pass