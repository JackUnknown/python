class Student:
    def __init__(self, sid=0,sname='',m1=0,m2=0,m3=0):
        self.__sid = sid
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
    
    def set_sid(self, sid):
        self.__sid = sid
    
    def get_sid(self):
        return self.__sid
        
    def set_sname(self,snm):
        self.__sname = snm
    
    def get_sname(self):
        return self.__sname
    
    def set_m1(self,m):
        self.__m1 = m
    
    def get_m1(self):
        return self.__m1
    
    def set_m2(self,m):
        self.__m2 = m
    
    def get_m2(self):
        return self.__m2
    
    def set_m3(self,m):
        self.__m3 = m
    
    def get_m3(self):
        return self.__m3
      
    def calculatePercent(self):
        return (self.__m1+self.__m2+self.__m3)/3
    
    
    def __str__(self):
        return f''' 
    Id: {self.__sid}
    Name: {self.__sname}
    Marks 1: {self.__m1}
    Marks 2: {self.__m2}
    Marks 3: {self.__m3}
    '''
                
if __name__ == '__main__':       
    s = Student(1,'ABC',70,80,90)
    print(s)
    print(f"Name : {s.get_sname()}")