# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 08:35:52 2026

@author: anilk
"""
def displaydiamond(n):
    spcnt=n//2
    for i in range(1,n+1,2):
        print(" "*spcnt,end=" ")
        print("*"*i)
        spcnt=spcnt-1
    spcnt=1
    for i in range(n-2,0,-2):
        print(" "*spcnt,end=" ")
        print("*"*i)
        spcnt=spcnt+1
        
        
n=int(input("enter number of lines"))
if n%2==0:
    print("the number should be odd")
else:
    displaydiamond(n)