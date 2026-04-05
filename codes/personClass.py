from abc import ABC, abstractmethod

class Person:
    def __init__(self,pid=0,pname='', mobno=0, email=''):
        self.__pid=pid
        self.__pname=pname
        self.__mobno=mobno
        self._email=email
        
    def set_pid(self,pid):
        self.__pid=pid
    def get_pid(self):
        return self.__pid
    
    def set_pname(self,pnm):
        self.__pname=pnm
    def get_pname(self):
        return self.__pname
    
    def set_mobno(self,mNo):
        self.__pid=mNo
    def get_mobno(self):
        return self.__mobno
    
    def set_email(self,em):
        self.__email=em
    def get_email(self):
        return self.__email
    
    def __str__(self):
        return f'''
                PID: {self.__pid}
                Name: {self.__pname}
                Mobile Number: {self.__mobno}
                Email: {self._email}
                '''

class Employee(Person,ABC):
    def __init__(self,pid=0,pname='', mobno=0, email='', dept='',desg=''):
        #parent constructor
        super().__init__(pid,pname,mobno,email)
        self.__dept=dept
        self.__desg=desg
    
    def set_dept(self,dept):
        self.__dept=dept
    def get_dept(self):
        return self.__dept

    def set_desg(self,desg):
        self.__desg=desg
    def get_desg(self):
        return self.__desg
    
    @abstractmethod
    def calculateSal(self):
        pass
    def __str__(self):
        return super().__str__()+f'''Department: {self.__dept}
                Desgination: {self.__desg}
                '''

class SalariedEMP(Employee):
    def __init__(self,pid=0,pname='', mobno=0, email='', dept='',desg='', salary=0):
        super().__init__(pid,pname,mobno,email,dept,desg)
        self.__salary=salary
        self.__bonus=salary*0.10
        
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    
    def set_bonus(self,bonus):
        self.__bonus=bonus
    def get_bonus(self):
        return self.__bonus
    
    def calculateSal(self):
        return self.__salary+ 0.10*self.__salary+0.15*self.__salary-0.08*self.__salary+self.__bonus
    
    def calculateBonus(self, perc):
        self.__bonus=self.__salary * perc
        return self.__bonus
    
    def __str__(self):
        return super().__str__()+f'''Salary: {self.__salary}
                Bonus: {self.__bonus}
                '''
class ContractEMP(Employee):
    def __init__(self,pid=0,pname='', mobno=0, email='', dept='',desg='', hrs=0, charges=0):
        super().__init__(pid,pname,mobno,email,dept,desg)
        self.__hrs=hrs
        self.__charges=charges
        
    def set_hrs(self,hrs):
        self.__hrs=hrs
    def get_hrs(self):
        return self.__hrs
    
    def set_charges(self,charges):
        self.__charges=charges
    def get_charges(self):
        return self.__charges
    
    def calculateSal(self):
        return self.__hrs * self.__charges
    
    def __str__(self):
        return super().__str__()+f'''Hours: {self.__hrs}
                Charges: {self.__charges}
                '''
    

if __name__=='__main__':
    p = Person(1,'ABC', 9876543210,'abc@email.com')
    print(p)
    
    # e = Employee(2,'XYZ',9874563210, 'xyz@gamil.com','HR','Head')
    # print(e)
    
    s = SalariedEMP(3,'MNO', 1236547980, 'mno@gamil.com', 'Sales', 'MGR', 50000)
    print(s)
    print(isinstance(s, SalariedEMP))
    print("Total Salary: ",s.calculateSal())
    
    #child specific function
    if isinstance(s, SalariedEMP):
        print(f'Bonus : {s.calculateBonus(0.50)}')
        
    s = ContractEMP(4,'PQR', 4567891230, 'pqr@mai.com', 'Security', 'Guard', 12, 1000)
    print(s)
    print(isinstance(s, ContractEMP))
    print(f"Total charges: {s.calculateSal()}")
    
    