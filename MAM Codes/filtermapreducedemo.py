# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 11:01:25 2026

@author: anilk
"""

lst1=[]
lst=[1,12,3,14,10,7,3,4]
for num in lst:
    if num%2==0 and num>5:
       lst1.append(num) 
print(lst,lst1)  

#list compression operator
lst2=[num for num in lst if num%2==0 and num>5]     
print(lst,lst2)


lst3=list(filter(lambda num:num%2==0 and num>5,lst))


lst4=[]
for num in lst:
     lst4.append(num*num)

lst6=[num*num for num in lst] 
    
lst5=list(map(lambda num:num*num,lst) )    
     
import functools
s=0
for num in lst:
    s=s+num
    
s=functools.reduce(lambda acc,num:acc+num,lst)
print(s) 

print(f"Sum: {sum(lst)}")
print(f"min: {min(lst)}")
print(f"max: {max(lst)}")
    
s=functools.reduce(lambda acc,num:acc+num,lst,100)  


lst1=['python','perl 6.4','java','C++ prog'] 
s=functools.reduce(lambda acc,s:acc+s[0:3], lst1,'')
print(s)   

s=functools.reduce(lambda acc,s:acc if len(acc)>len(s) else s ,lst1)                    
print(s) 

    

