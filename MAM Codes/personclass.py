from abc import ABC,abstractmethod
class Person:
    def __init__(self,pid=0,pname="",mob="",em=""):
        #private members
        self.__pid=pid
        self.__pname=pname
        self.__mob=mob
        #protected member
        self._email=em
    
    #setter getter 
    def set_pid(self,pid):
        self.__pid=pid
        
    def get_pid(self):
        return self.__pid
    
    def set_pname(self,pnm):
        self.__pname=pnm
        
    def get_pname(self):
        return self.__pname
    
    def set_mob(self,m):
        self.__mob=m
        
    def get_mob(self):
        return self.__mob
    
    def set_email(self,m):
        self.__email=m
        
    def get_email(self):
        return self.__email
    
    def __str__(self):
        return f"ID: {self.__pid} name: {self.__pname} Mobile:{self.__mob} Email:{self._email}"
        
class Employee(Person,ABC):
    def __init__(self,pid=0,pname="",mob="",em="",dt="",dg=""):
        #parent constructor
        super().__init__(pid,pname,mob,em)
        self.__dept=dt
        self.__desg=dg
    #setter and getter
    def set_dept(self,dt):
        self.__dept=dt
        
    def get_dept(self):
        return self.__dept
    
    def set_desg(self,dg):
        self.__desg=dg
        
    def get_desg(self):
        return self.__desg
    
    @abstractmethod
    def calculateSal(self):
        pass
    
    def __str__(self):
        return super().__str__()+f"Department: {self.__dept} Designation: {self.__desg}"
        
class SalariedEmp(Employee):
    def __init__(self,pid=0,pname="",mob="",em="",dt="",dg="",s=0):
        super().__init__(pid,pname,mob,em,dt,dg)
        self.__sal=s
        self.__bonus=s*0.10
    
    #setter and getter
    def set_sal(self,s):
        self.__sal=s
        
    def get_sal(self):
        return self.__sal
    
    def set_bonus(self,b):
        self.__bonus=b
        
    def get_bonus(self):
        return self.__bonus
    
    def calculateSal(self):
        print("calculatesal in SalariedEmp")
        return self.__sal+0.10*self.__sal+0.15*self.__sal-0.08*self.__sal+self.__bonus
     
    def calculateBonus(self,perc):
        self.__bonus=self.__sal*perc
        return self.__bonus
    
    def __str__(self):
        return super().__str__()+f" Salary : {self.__sal} bonus: {self.__bonus}"

class ContractEmp(Employee):
    def __init__(self,pid=0,pname="",mob="",em="",dt="",dg="",hrs=0,charges=0):
        super().__init__(pid,pname,mob,em,dt,dg)
        self.__hrs=hrs
        self.__charges=charges
    #setter and getter
    def set_hrs(self,h):
        self.__hrs=h
        
    def get_hrs(self):
        return self.__hrs
    
    def set_charges(self,h):
        self.__charges=h
        
    def get_charges(self):
        return self.__charges
   
    def calculateSal(self):
        print("calculatesal in ContractEmp")
        return self.__hrs*self.__charges
    
    def __str__(self):
        return super().__str__()+f" Hrs: {self.__hrs} Charges: {self.__charges}"
        
if __name__=='__main__':
    #e=Employee(12,'Sanajay','11111','ss@gmail.com','HR','Manager')    
    #print(e)
    
    #e1=Employee(pid=13,pname='Archana',mob='11111',dt='HR',dg='Manager')    
    #print(e1) 

    s1=SalariedEmp(14,'Mugdha','22222','mm@gmail.com','admin','Manager',23456)
    print(s1)
    print(isinstance(s1,SalariedEmp))
    #polymophism
    print("salary:"+str(s1.calculateSal()))
    
    #child specific function
    if isinstance(s1,SalariedEmp()):
        print("Bonus : ",s1.calculateBonus(0.10))
    
    s1=ContractEmp(15,'Tanaya','333','ttt@gmail.com','admin','assitant',45,6000)
    print(s1)
    print(isinstance(s1,ContractEmp))
    print(f"charges:{s1.calculateSal()}")
    
    
    
