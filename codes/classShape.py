
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,cid=0,color=''):
        self.__cid=cid
        self.__color=color

        
    def set_cid(self,cid):
        self.__cid=cid
    def get_cid(self):
        return self.__cid
    
    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color
    
    @abstractmethod
    def calculateArea(self):
        pass
    
    @abstractmethod
    def calculatePerimeter(self):
        pass
    
    def __str__(self):
        return f'''
    CID: {self.__cid}
    Color: {self.__color}
    '''

class Triangle(Shape):
    def __init__(self,cid=0,color='', side1=0,side2=0,height=0,base=0):
        #parent constructor
        super().__init__(cid,color)
        self.__side1=side1
        self.__side2=side2
        self.__height=height
        self.__base=base
        
    def set_side1(self,side1):
        self.__side1=side1
    def get_side1(self):
        return self.__side1
    
    def set_side2(self,side2):
        self.__side2=side2
    def get_side2(self):
        return self.__side2
        
    def set_height(self,height):
        self.__height=height
    def get_height(self):
        return self.__height

    def set_base(self,base):
        self.__base=base
    def get_base(self):
        return self.__base
    
    def calculateArea(self):
        return (0.5 * self.__height * self.__base)
    
    def calculatePerimeter(self):
        return self.__side1 +self.__side2+self.__base
    
    def __str__(self):
        return super().__str__()+f'''Side1: {self.__side1}
    Side2: {self.__side2}
    Height: {self.__height}
    Base: {self.__base}
    '''

class Circle(Shape):
    pi = 3.142
    def __init__(self,cid=0,color='',radius=0):
        super().__init__(cid,color)
        self.__radius=radius
        
    def set_radius(self,radius):
        self.__radius=radius
    def get_radius(self):
        return self.__radius
    
    def calculateArea(self):
        return (Circle.pi * self.__radius * self.__radius)
    
    def calculatePerimeter(self):
        return (2*Circle.pi*self.__radius)
    
    def __str__(self):
        return super().__str__()+f'''Radius: {self.__radius}'''
class Rectangle(Shape):
    def __init__(self,cid=0,color='',length=0, breadth=0):
        super().__init__(cid, color)
        self.__length=length
        self.__breadth=breadth
        
    def set_length(self,length):
        self.__length=length
    def get_length(self):
        return self.__length
    
    def set_breadth(self,breadth):
        self.__breadth=breadth
    def get_breadth(self):
        return self.__breadth
    
    def calculateArea(self):
        return self.__length * self.__breadth
    
    def calculatePerimeter(self):
        return 2*(self.__length+self.__breadth)
    
    def __str__(self):
        return super().__str__()+f'''Length: {self.__length}
    Breadth: {self.__breadth}
    '''
    

if __name__=='__main__':
    # s = Shape(1,'Red')
    # print(s)
    
    t = Triangle(2,'Blue',4,6,8,10)
    print(t)
    print(isinstance(t, Triangle))
    print("Area of Triangle: ",t.calculateArea())
    print("Perimeter of Triangle: ",t.calculatePerimeter())
        
    c = Circle(3,'Green', 10)
    print(c)
    print(isinstance(c, Circle))
    print("Area of Circle: ",c.calculateArea())
    print("Circumference of Circle: ",c.calculateCircumference())
    
    r = Rectangle(4,'Yellow',10,12)
    print(r)
    print(isinstance(r, Rectangle))
    print("Area of Rectangle: ",r.calculateArea())
    print("Perimeter of Rectangle: ",r.calculatePerimeter())