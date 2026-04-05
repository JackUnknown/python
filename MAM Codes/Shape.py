# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:23:01 2026

@author: anilk
"""
from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,id=0,color=""):
        self.__id=id
        self.__color=color
    #setter and getter
    def set_id(self,id):
        self.__id=id
    def get_id(self):
        return self.__id
    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    def __str__(self):
        return f" id:{self.__id} color:{self.__color}"
    @abstractmethod
    def calculatearea(self):
        pass
    @abstractmethod
    def calculateperimeter(self):
        pass

class Triangle(Shape):
    
    def __init__(self,id=0,color="",s1=0,s2=0,h=0,b=0):
        super().__init__(id,color)
        self.__s1=s1
        self.__s2=s2
        self.__h=h
        self.__b=b
    
    def set_s1(self,s1):
        self.__s1=s1
    def get_s1(self):
        return self.__s1
    def set_s2(self,s2):
        self.__s2=s2
    def get_s2(self):
        return self.__s2
    def set_b(self,b):
        self.__b=b
    def get_b(self):
        return self.__b
    def set_h(self,h):
        self.__h=h
    def get_h(self):
        return self.__h
    
    def calculatearea(self):
        return 0.5*self.__b*self.__h
    
    def calculateperimeter(self):
        return self.__s1+self.__s2+self.__b
    
    def __str__(self):
        return super().__str__()+f" s1:{self.__s1},s2:{self.__s2},b:{self.__b},h:{self.__h}"

class Circle(Shape):
    pi=3.14
    def __init__(self,id=0,color="",r=0):
        super().__init__(id,color)
        self.__r=r
        
        #setter and getter
        
    def set_r(self,r):
        self.__r=r
    def get_r(self):
        return self.__r 
        
    def calculatearea(self):
        return Circle.pi*self.__r*self.__r
        
    def calculateperimeter(self):
        return 2*Circle.pi*self.__r
    def __str__(self):
        return super().__str__()+f" radius:{self.__r}"
        
        
if __name__=='__main__':
    
    t1=Triangle(12,"blue",2,5,3,9);
    print(t1)
    c1=Circle(1,"red",4);
    print(c1)
        


