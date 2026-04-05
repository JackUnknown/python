from emp_service import *

choice = 0
while choice != 8:
    choice =int(input('''
*****************************
1. Add new employee
2. Delete employee
3. Update salary employee
4. Display in sorted order of name
5. Display all name
6. Search by id
7. Search by name
8. Exit 
*****************************
Enter your choice: '''
)) 
    match choice:
        case 1:
            status = addNewEmployee()
            if status:
                print("Employee added")
            else:
                print("Error")
        case 2:
            empid = int(input("Enter employee id to delete the employee:"))
            status = deleteEmployee(empid)
            if status:
                print('Employee deleted')
            else:
                print('Not found')
            
        case 3:
            empid = int(input("Enter employee id to modify salary:"))
            new_sal=float(input("Enter new salary"))
            status = updateSalary(empid,new_sal)
            if status:
                print('Salary updated')
            else:
                print("Not found")
    
        case 4:
            sorByName()
        case 5:
            displayAllEmployees()
        case 6:
            empid = int(input("Enter the id to search: ")) 
            pos, emp = searchById(empid)
            if pos != -1:
                displayAllEmployees([emp])
            else:
                print("ID not found.")
        case 7:
            name = input("Enter the name:")
            lst = searchByName(name)
            if lst != None:
                displayAllEmployees(lst)
            else:
                print("Not found")
        case 8:
            print('\nExiting....')
            break
        case others:
            print("Wrong choice")