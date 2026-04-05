lst=['Revati','Rajan','Ashu','Atharva']

def addname(name):
    lst.append(name)
    return True

def displayAll():
    for idx,nm in enumerate(lst,1):
        print(f"{idx}) {nm}")

def deletename(name):
    if name in lst:
        lst.remove(name)
        return True
    else:
        return False
def searchName(oname):
    if oname in lst:
        return lst.index(oname),lst.count(oname)
    else:
        return -1,0
    
def updatename(oname,nname):
    pos,cnt=searchName(oname)
    if pos!=-1:
        lst[pos]=nname
        return True
    else:
        return False
    
def displaySortedname(ch):
    if ch==1:
        for nm in sorted(lst):
            print(nm)
    else:
        for nm in sorted(lst,reverse=True):
            print(nm)
            
        
choice=0
while choice!=7:
    choice=int(input("""
                     1. add new name
                     2. delete name
                     3. update name
                     4. display all
                     5. search name
                     6. display in sorted order
                     7.exit
                     """))
    match choice:
        case 1:
            name=input("enter name")
            status=addname(name)
            if status:
                print("name added")
            else:
                print("name not added")
           
        case 2:
            name=input("enter name")
            status=deletename(name)
            if status:
                print("name deleted")
            else:
                print("name not deleted")
        case 3:
            oname=input("enter name to modify")
            nname=input("enter newname")
            status=updatename(oname,nname)
            if status:
                print("name updated")
            else:
                print("name not updated")
            pass
        case 4:
            displayAll()
            
        case 5:
            name=input("enter name")
            pos,cnt=searchName(name)
            if pos!=-1:
                print(f"name found at {pos} count: {cnt}")
            else:
                print("name not found")
            
        case 6:
            ch=int(input("1. Ascending \n 2. Descending\n"))
            displaySortedname(ch)
        case 7:
            print("Thank you for visiting.....")
        case others:
            print("wrong choice")
        
        
        
        
        
        
        
        