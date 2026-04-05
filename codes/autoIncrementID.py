class Student:
    count = 0
    
    @staticmethod
    def __generateId(snm,addr):
        Student.count+=1
        s = snm[0:2]+addr[0:2]+str(Student.count)
        
        return s
        
        
    def __init__(self, snm='',addr=''):
        self.__sid =Student.__generateId(snm,addr)
        
        self.__sname=snm
        self.__addr=addr
    
    
    def __str__(self):
        return f'Id: {self.__sid} Name: {self.__sname} Address: {self.__addr}'
    
if __name__=='__main__':
    s1= Student('ABC', 'Pune')
    print(s1)
    s2 = Student('PQR', 'Pune')
    print(s2)