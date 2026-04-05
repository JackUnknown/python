#using exception handling
try:
    fh = open("test1.txt")
    for line in fh:
        print(line.rstrip('\n'))
except:
    print('Error occured')                
finally:
    fh.close()
    
    
    
#using exception handling
try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    
    ans = a/b
    print(ans)
except ValueError as e:
    print('Error occured enter int')
    print(e)
except (ZeroDivisionError, KeyError) as e:
    print('Division 0')
    print(e)   
    
    
    
    
    

#as soon as with finishes it will close the file
with open("test1.txt") as fh:
    for line in fh:
        print(line.rstrip('\n'))


import re        
#copy of the file
with open("test1.txt") as fh:
    with open("test2.txt","a") as fh1:
        for line in fh:
            m = re.search(r'\d$', line)
            if m!= None:
                fh1.write(line.lower())

def divide(x,y):
    ans = x/y
    return ans
    
try:
    a = int(input('Enter number1: '))
    b = int(input('Enter number2: '))
    
    ans = divide(a,b)
    print(ans)
except ValueError as e:
    print('Error occured enter integer')
    print(e)
except (ZeroDivisionError, KeyError) as e:
    print('Division 0')
    print(e)  
except Exception as e:
    print("Error occered")
    print(e)
    
    
    
    
def divide(x,y):
    try:
        ans = x/y
        return ans
    except ZeroDivisionError as e:
        print(e)
        raise e       #rethrow exception


for i in range(3):    #Limit number of attempts: give 3 chances
    try:
        a = int(input('Enter number1: '))
        b = int(input('Enter number2: '))
        
        ans = divide(a,b)
        print(ans)
        break
    except ValueError as e:
        print('Error occured enter integer')
        print(e)
    except (ZeroDivisionError, KeyError) as e:
        print('Division 0')
        print(e)  
    except Exception as e:
        print("Error occered")
        print(e)
        
    

for i in range(3):   
    try:
        salary = float(input('Enter the salary: '))    
        
        if salary >= 5000:
            print(salary)
        elif salary < 0:
            raise ValueError('Salary cannot be negative')
        else:
            raise ValueError('Salary cannot less than 5000')
    except ValueError as e:
        print(e)
        

#--------------------------------------------------------------------------#
        
        
# Customized Exception:
    
class InvalidSalaryError(Exception):
    def __init__(self,msg="Invalid Salary"):
        self.__msg=msg
    def __str__(self):
        return self.__msg

for i in range(3):   
    try:
        salary = float(input('Enter the salary: '))    
        
        if salary >= 5000:
            print(salary)
        elif salary < 0:
            raise InvalidSalaryError('Salary cannot be negative')
        else:
            raise InvalidSalaryError('Salary cannot less than 5000')
    except InvalidSalaryError as e:
        print(e)
    except ValueError as e:
        print(e)
        
        
        
#--------------------------------------------------------------------------#        
                
        
class NumberNotFoundError(Exception):
    def __init__(self, msg = 'Entered Wrong number'):
        self.__msg = msg
    def __str__(self):
        return self.__msg


n = 23
cnt=0
while True:
    try:        
        cnt+=1
        num = int(input('Enter number : '))
        if num != n:
            raise NumberNotFoundError(f'OOPs!! you lose again --> {cnt}')
        else:
            print('Got it')
            break
    except NumberNotFoundError as e:
        print(e)        