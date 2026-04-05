# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:38:03 2026

@author: anilk
"""

num=int(input("enetr number"))

for i in  range(2,(num//2)+1):
    if num%i==0:
        print(f"The number {num} is not prime")
        break
else:
    print(f"The number {num} is prime")
    
    

   
        
        