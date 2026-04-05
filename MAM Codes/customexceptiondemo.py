#custom exceptions
class InvalidSalaryError(Exception):
    def __init__(self,msg="invalid salary"):
        self.__msg=msg
    def __str__(self):
        return self.__msg
        
    
try:
    salary=float(input("enter salary"))
    if salary >=5000:
        print(salary)
    else:
        raise InvalidSalaryError("salary cannot be < 5000")
except ValueError as e:
    print(e)
    