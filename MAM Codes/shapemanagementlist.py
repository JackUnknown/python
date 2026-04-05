# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:51:15 2026

@author: anilk
"""

from Shape import *

shape_list=[]
choice=0

def addnewshape(ch):
    id=int(input("Enter id: "))
    color=input("Enter color")
    
    if ch == 1:
        s1=int(input("Enter side 1: "))
        s2=int(input("Enter side 3: "))
        b=int(input("Enter base: "))
        h=int(input("Enter height: "))
        sh1=Triangle(id,color,s1,s2,h,b)
    elif ch == 2:
        r=int(input("Enter radius: "))
        sh1=Circle(id,color,r)
    shape_list.append(sh1)
    return True

def displayall():
    for shape in shape_list:
        print(shape)
def searchbyid(sid):
    for pos,shape in enumerate(shape_list):
        if shape.get_id()==sid:
            return pos,shape
    else:
        return -1,None
    
def getarea(sid):
    pos,s=searchbyid(sid)
    if pos!=-1:
        return s.calculatearea()
    else:
        return -1
def getperimeter(sid):
    pos,s=searchbyid(sid)
    if pos!=-1:
        return s.calculateperimeter()
    else:
        return -1
    
def changeradius(sid,new_radius):
    pos,s=searchbyid(sid)
    if pos!=-1 and isinstance(s,Circle):
        s.set_r(new_radius)
        return True
    else:
        return False
    
def findcount():
    ccount=0
    tcount=0
    for shape in shape_list:
        if isinstance(shape,Circle):
            ccount+=1
        elif isinstance(shape,Triangle):
            tcount+=1
    return ccount,tcount
while choice!=8:
    choice=int(input("""
                     1.Add new shape
                     2.Display all
                     3.Display by id
                     4.Area
                     5.Permimeter
                     6.Change radius
                     7.count shapes
                     8.exit
                     Enter your choice:
                     """))
    match choice:
        case 1:
            ch=int(input("1.Triangle/n2.Circle"))
            status=addnewshape(ch)
            if status:
                print("shape added successfully")
            else:
                print("shape addition failed")
        case 2:
            displayall()
        case 3:
            sid=int(input("Enter sid: "))
            pos,s=searchbyid(sid)
            if pos == -1:
                print("Shape not found")
            else:
                print(f"shape {s} found at {pos}")
        case 4:
            sid=int(input("Enter sid:"))
            area=getarea(sid)
            if area!=-1:
                print(f"Area:{area}")
            else:
                print("Not Found")
        case 5:
            sid=int(input("Enter sid:"))
            perimeter=getperimeter(sid)
            if perimeter!=-1:
                print(f"Perimeter:{perimeter}")
            else:
                print("Not Found")
        case 6:
            sid=int(input("Enter sid: "))
            new_radius=int(input("Enter new radius: "))
            status=changeradius(sid,new_radius)
            if status:
                print("Radius changed.")
            else:
                print("not found!")
        case 7:
            circle_count,triangle_count=findcount()
            print(f"The number of circles are: {circle_count}")
            print(f"The number of Triangles are: {triangle_count}")
        case 8:
            print("Thank you for visiting ...")
        case others:
            print("Invalid Choice")