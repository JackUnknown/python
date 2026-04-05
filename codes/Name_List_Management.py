
lst = ['ABC', 'DEF', 'GHI', 'JKL']

    
def displayAll():
    for idx, nm in enumerate(lst,1):
        print(f"{idx} {nm}")
        
def addname(name):
    lst.append(name)
    print(lst)
    return True
   
def deletename(name):
    if name in lst:
        lst.remove(name)
        return True
    else:
        return False

def searchname(oname):
    if oname in lst:
        return lst.index(oname), lst.count(oname)
    else:
        return -1,0
    
def updatename(oname, nname):
    pos,cnt = searchname(oname)
    if pos != -1:
        lst[pos] = nname
        return True
    else:
        return False

def displaySortedname(ch):
    if ch == 1:
        for nm in sorted(lst):
            print(nm)
    else:
        for nm in sorted(lst, reverse=True):
            print(nm)

choice = 0 
while choice != 7:
    choice =int(input('''
*****************************
1. Add new name
2. Delete name
3. Update name
4. Display all name
5. Search name
6. Display in sorted order
7. Exit 
*****************************
Enter your choice: '''
)) 
    match choice:
        case 1:
            name = input("\nEnter the name: ")
            status = addname(name)
            if status == True:
                print(f"{name} added to the list")            
            else:
                print('Error')
        case 2:
            name = input("\nEnter the name: ")
            status = deletename(name)
            if status == True:
                print(f"{name} deleted from the list")            
            else:
                print('Error')
        case 3:
            oname = input("\nEnter the old name: ")
            nname = input("Enter the new name: ")
            status = updatename(oname, nname)
            if status == True:
                print(f"{oname} updated to {nname} in the list")
            else:
                print('Error')
        case 4:
            print('\nNames from the list : ')
            displayAll()
        case 5:
            name = input("\nEnter the name to search: ")
            pos, cnt = searchname(name)
            if pos == -1:
                print(f"{name} is not in the list")
            else:
                print(f"{name} is at {pos} index {cnt}")
        case 6:
            ch=int(input("\n1. Ascending\n2. Descending\n"))
            displaySortedname(ch)
        case 7:
            print('\nExiting....')
            break
        case others:
            print("Wrong choice")
