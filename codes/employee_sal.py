with open('employee.txt') as fh:
    s = 0
    for ln in fh:
        emplst = ln.rstrip('\n').split(',')
        s = s + int(emplst[-1])
        
print(f'Sum of salary: {s}')    


dept_sal = {}
with open('employee.txt') as fh:
    for ln in fh:
        emplst = ln.rstrip('\n').split(',')
        dept = emplst[2]
        salary = int(emplst[-1])
        
        if dept not in dept_sal:
            dept_sal[dept] = 0
            
        dept_sal[dept] += salary
        
for dept, total in dept_sal.items():
    print(f"{dept} : {total}")
    
sal = {}
with open('employee.txt') as fh:
    for ln in fh:
        emplst = ln.rstrip('\n').split(',')
        name = emplst[1]
        salary = int(emplst[-1])
        
        if name not in sal:   
            sal[name] = salary
        
for name, salary in sal.items():
    print(f"{name} : {salary}")