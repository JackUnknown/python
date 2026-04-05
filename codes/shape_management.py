from classShape import *

shapelst=[]

def displayAll(lst = shapelst):
    for shape in lst:
        print(shape)

def addNewShape(ch):
    cid = int(input('Enter CID: '))
    color = input('Enter Color Name: ')
        
    if ch == 1:
        side1 = int(input("Enter side 1: "))
        side2 = int(input("Enter side 2: "))
        height = int(input("Enter height: "))
        base = int(input("Enter base: "))
        shape = Triangle(cid,color,side1,side2,height,base)
    elif ch == 2:
        radius = int(input("Enter radius of circle: "))
        shape = Circle(cid,color,radius)
    elif ch == 3:
        length = int(input("Enter length: "))
        breadth = int(input("Enter breadth: "))
        shape = Rectangle(cid,color,length, breadth)
    shapelst.append(shape)
    return True


def searchById(cid):
    for pos, c in enumerate(shapelst):
        if c.get_cid() == cid:
            return pos,c
    else:
        return -1, None
    
def searchByName(color):
    for pos, c in enumerate(shapelst):
        if c.get_color() == color:
            return pos,c
    else:
        return -1, None

def getArea(cid):
    pos, shape = searchById(cid)
    if pos!= -1:
        return shape.calculateArea(), True
    return 0.0, False

def getPerimeter(cid):
    pos, shape = searchById(cid)
    if pos!= -1:
        return shape.calculatePerimeter(), True
    return 0.0, False

def deleteById(cid):
    pos, shape = searchById(cid)
    if pos!= -1:
        ans = input('Do you want to delete (y/n)') 
        if ans == 'y':
            shapelst.pop(pos)
            return 1
        else:
            return 2
    else:
        return 3
    
def changeRadius(cid, new_radius):
    pos, shape = searchById(cid)
    if shape!= None and isinstance(shape,Circle):
        shape.set_radius(new_radius)
        return True
    else:           
        return -1
    
def findCount():
    triangle_cnt=0
    circle_cnt=0
    rectangle_cnt=0
    for shape in shapelst:
        if isinstance(shape,Triangle):
            triangle_cnt += 1
        if isinstance(shape,Circle):
            circle_cnt += 1
        if isinstance(shape,Rectangle):
            rectangle_cnt += 1
    return triangle_cnt, circle_cnt, rectangle_cnt


choice = 0

while choice != 9:
    choice = int(input(''' 
1. Add new Shape
2. Delete Shape
3. Change Radius
4. Display all
5. Search by id
6. Count Shapes
7. Calculate Area
8. Caculate Perimeter
9. Exit
                       
Enter your Choice: 
'''))
    match choice:
        case 1: 
            ch = int(input('''
1. Triangle
2. Circle 
3. Rectangle
                           
Enter your choice:
'''))
                        
            status = addNewShape(ch)
            if status:
                print("Shape Added")
            else:
                print('Shape not added')
            
        case 2: 
            cid = int(input('Enter shape id: '))
            status = deleteById(cid)
            if status == 1:
                print('Found Delete sucessful')
            elif status == 2:
                print('Found and not Delete')
            elif status == 3:
                print('Not found')
            
        case 3: 
            cid = int(input('Enter shape id: '))
            new_radius = int(input('Enter new radius: '))
            
            status = changeRadius(cid,new_radius)
            if status:
                print('Modification done')
            else:
                print('Not found')
            
        case 4: 
            displayAll()
            
        case 5: 
            cid = int(input("Enter the shape id: "))
            pos, shape = searchById(cid)
            if pos != -1:
                print(shape)
            else:
                print('Not found') 
            
        case 6: 
            triangle_cnt, circle_cnt, rectangle_cnt = findCount()
            print(f'Trangle count : {triangle_cnt}')
            print(f'Circle count : {circle_cnt}')
            print(f'Rectangle count : {rectangle_cnt}')
            pass
        case 7: 
            cid = int(input('Enter shape id: '))
            area, status = getArea(cid)
            if status:
                print('Area : ' , area)
            else:
                print('Not found')
                
        case 8: 
            cid = int(input('Enter shape id: '))
            perimeter, status = getPerimeter(cid)
            if status:
                print('Perimeter : ' , perimeter)
            else:
                print('Not found')
            
        case 9:  
            print('Exitng......')
            pass
        case others: 
            print('Wrong choice')
            pass