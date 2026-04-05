# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 12:06:21 2026

@author: anilk
"""

lst=[34,20,1,4,56,37]
#see the list in sorted ascending order, 
#but original list will remain same 
for num in sorted(lst):
    print(num)
     
print(lst)

#see the list in sorted descending order, 
#but original list will remain same 
for num in sorted(lst,reverse=True):
    print(num)
    
print(lst)

#see the list in reverse order, 
#but original list will remain same 
for num in reversed(lst):
    print(num)
    
print(lst)


#zip is used to navigate through multiple list parallely
lst=[1,2,3,4]
lst1=['Pune','Mumbai','Nashik']
for x in zip(lst,lst1):
    print(x[0],"---->",x[1])

for x,y in zip(lst,lst1):
    print(x,"---->",y)
    
    
lst=[12,23,11,4,3]

#enumerate will assign the number starting from 0
#and can be used as index of value
for num in enumerate(lst): #[(0,12),(1,23)]
    print(num)
    print(num[0],"---->",num[1])
    
for i,num in enumerate(lst): #[(0,12),(1,23)]
     print(i,"---->",num)    

#enumerate will assign the number starting from 11
#and can be used as number to the values    
for i,num in enumerate(lst,11): #[(11,12),(12,23)]
     print(i,"---->",num)    






