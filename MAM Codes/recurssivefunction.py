# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:47:45 2026

@author: anilk
"""

def addition(a,b):
    a=a+10
    b=b+20
    return a+b

def myf1(x=3,y=5):
    x=x+100
    y=y+200
    return x,y


def factorial(n):
    if n==1:
        #print(f"ending recurssion by returning 1")
        return 1
    else:
        #print(f"calling factorial({n-1}) and n={n}")
        return n*factorial(n-1)
    
factorial(5)


import math
  
    
    