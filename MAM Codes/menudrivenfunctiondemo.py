# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:08:02 2026

@author: anilk
"""
#checks whether the given number is prime or not
def checkprime(num=5):
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    else:
        return True
    
#display table of the given number
def printtable(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
       
#find factorial of the given number
def findFactorial(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

#find digit addition of the number
def digitaddition(num):
    s=0
    while num>0:
        d=num%10
        num=num//10
        s=s+d
    return s

import sys
choice=0
while choice!=5:
    choice=int(input("""
                     1. check prime
                     2. find factorial
                     3. display table
                     4. digit addition
                     5. exit
                     choice:"""))
    match choice:
        case 1:
            num=int(input("Enter number"))
            status=checkprime(num)
            if status:
                print(f"The number {num} is prime")
            else:
                print(f"The number {num} is not prime")
        case 2:
            num=int(input("Enter number"))
            result=findFactorial(num)
            print(f"Factorial of {num} : {result}")
            pass
        case 3:
            num=int(input("Enter number"))
            printtable(num)
            pass
        case 4:
            num=int(input("Enter number"))
            result=digitaddition(num)
            print(f"digit addition : {num}--->",result)
            pass
        case 5:
            print("Thank you for visiting......")
            #sys.exit(0)
        