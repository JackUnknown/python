# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 10:04:54 2026

@author: anilk
"""
#packing of tuple
a=1,2,'test',3
x=(10,20)
y=10,  #tuple of size 1
print(type(y))


def f1(a,b):
    a=a+10
    b=b+20
    return a,b   #return tuple

x,y=f1(10,20)
print(x,y,sep=":")   #10:20

#variable number of parameters
def add(a,b,*t):
    s=a+b
    print("tuple",t)
    for num in t:
        s=s+num
    return s
    
print(add(12,34))
sumnum=add(1,2,3,5,23,56) 
print(sumnum) 

a=1,2,3,4
print(a.index(3))


#it will convert to list
lst=list(a)
    
#to convert into tuple use tuple function
t1=tuple(lst)    
    
    
    

