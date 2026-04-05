from studentclass import Student

studlst = []

def addNewStudent():
    sid = int(input("    Enter id: "))
    sname = input("    Enetr name: ")
    m1 = float(input("    Enter m1: "))
    m2 = float(input("    Enter m2: "))
    m3 = float(input("    Enter m3: "))
    s = Student(sid,sname,m1,m2,m3)
    studlst.append(s)
    return True
    

def displayAll(lst = studlst):
    for s in lst:
        print(s)
    
def displayById(sid):
    for idx, s in enumerate(studlst):
        if s.get_sid() == sid:
            return idx, s
    else:
        return -1, None

def calculatePercentById(sid):
    for idx,s in enumerate(studlst):
        if s.get_sid() == sid:
            return s.calculatePercent()
    else:
        return False
    

choice = 0
while choice != 5:
    choice=int(input("""
    *****************************
    1. Add new student
    2. Display all students
    3. Display student by id
    4. Calculate total percentage of student by id
    5. Exit
    *****************************
    Enter your choice: """
    ))
        
    match choice:
        case 1:
            status = addNewStudent()
            if status:
                print("    Student added")
            else:
                print("    Student not added")
        case 2:
            print()
            print("\tStudent Details: ")
            displayAll()
            pass
        case 3:
            sid = int(input("\tEnter the id of student: "))
            pos, stud = displayById(sid)
            if pos != -1:
                print(stud)
            else:
                print('Not found') 
        case 4:
            sid = int(input("\tEnter the id of student: "))
            perc = calculatePercentById(sid)
            print(f"\tPercentage of marks: {perc}")
        case 5:
            print('\nExiting....')
            pass
        case others:
            pass