print("hello world");
a=23
b=233

if a>b:
    print("Maximum is a", a)
    print("End of if")
else:
    print("Maximum is b", b)
    print("End of else")
print("Outsied if")

#------------------#

for i in range(5):
    print(i)
    
#------------------#    

age = 25
if age>=3 and age<6:
    print("KG")
elif age>=6 and age<14:
    print("Primary")
else:
    print("College")
    
#------------------#    
    
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
a=n1+n2
print("Addition of",n1,"and", n2,"=",a)
print("Addition of " + str(n1) + " and " + str(n2) + " = " + str(a))
print(f"Addition of {n1} and {n2} = {a}")
print("Addition of {0} and {1} = {2}".format(n1,n2,a))

#------------------#

print("Hello ",end='')
print("World")

#------------------#

print(4,5,6,7,8,sep=',')

#------------------#

lst = [10,20,30]

lst.insert(4,40)
print(lst)
lst.extend([50,60])
print(lst)
lst.pop(5)
print(lst)
lst.append(60)
print(lst)
len(lst)
lst.append('test')
print(lst)
lst.extend('test')
print(lst)

lst.remove(60)
print(lst)

lst.count(10)
lst1=lst.copy()

lst.reverse()
print(lst)
print(lst1)

lst.sort(reverse=True)
print(lst)

print(lst1)


(a,b)=10,20
print(a)
print(b)

a=10,
print(a)
print(type((a)))


def f1(a,b):
    a=a+10
    b=b+20
    return a,b

x,y = f1(10,20)
print(x,y, sep=':')

def add(a,b=10,*t):
    s=a+b
    for num in t:
        s+=num
    return s

print(add(5,1))
summ = add(10,20,30)
print(summ)

a=1,2,3,4,5
print(a.index(2))


lst=list(a)
print(lst)
lst.sort(reverse=True)

a=tuple(lst)
print(a)

lst1=[]
lst=[1,12,3,14,10,7,3,4]
for num in lst:
    if num%2 == 0 and num>5:
        lst1.append(num)
print(lst,lst1)
        
#Q. Get numbers that are divisible by 2 and greater than 5
# List compression
lst2 = [num for num in lst if num%2 == 0 and num>5 ]
print(lst2)

#Lambda filter
lst3 = list(filter(lambda num: num%2 == 0 and num>5,lst))
print(lst3)

#Q. Square of each number using Lambda map
lst4=list(map(lambda num:num*num,lst))
print(lst4)


#reduse function
import functools
s=0
s=functools.reduce(lambda acc,num: acc+num,lst)
s=functools.reduce(lambda acc,num: acc+num,lst, 100) #initialize acc to 100
print(s)

s=functools.reduce(lambda acc,num: acc-num,lst) 
s=functools.reduce(lambda acc,num: acc-num,lst, 100) #initialize acc to 100
print(s)



str_lst= ['python', 'perl', 'java', 'C++ prog']
#Q. use reduce function to find string concat of first 3 letters of every string in the list
str1 = functools.reduce(lambda acc,str1 : acc+str1[:3],str_lst,'')
print(str1)

#Q. use reduce function to find string with max length
str2 = functools.reduce(lambda acc,str2:acc if len(acc)>len(str1) else str2 ,str_lst)
print(str2)


lst1 = [12,23,14,21,9,5]

for num in sorted(lst1):
    print(num)
print(lst1)

for num in reversed(lst1):
    print(num)
print(lst1)

lst1 = [1,2,3,4]
lst2 = ['Mumbai', 'Pune', 'Sangli']

for num in zip(lst1,lst2):
    print(num)
    
for x,y in zip(lst1,lst2):
    print(x,"---->",y)
    
lst1 = [12,23,14,21,9,5]

for num in enumerate(lst1):
    print(num)
    
for num in enumerate(lst1,1):
    print(num[0], num[1])
    
for i, num in enumerate(lst1):
    print(i, num)
    
for i, num in enumerate(lst1,11):
    print(i,"---->",num)
    
    
    
    

for i in range(1,5,1):
    print('*')
    print(' ' * i, sep='')        

    
# Set
    
s={1,2,3}
s.add(4)
s
s.add((5,6))  
s.add([7,8])
s.update([7,8]) 
s.update((9,10))  
s.remove(1000) 
s.pop()
s.discard(1111)
ss=s.copy()




s1={1,2,3,4,5}
s2={4,5,11,12}
s1.union(s2)
s1|s2
s1.intersection(s2)
s1&s2
s1.difference(s2)
s1-s2
s2.difference(s1)
s2-s1
s1.symmetric_difference(s2)
s1^s2
s2.symmetric_difference(s1)
s2^s1

s1.difference_update(s2)
s1=s1-s2
s1
s2

s1.symmetric_difference_update(s2)
s1=s1^s2





# Dictionary

d1={'a':100,'b':200}
d2={'a':200, 'c':400, 'x':500}
d1.update(d2)
d1
d2
d3={**d1,**d2}
d3

d= {'DAC':240,'DBDA':60, 'DVLSI':80}
d
d['dhpcsa']=70
d['DBDA'] = 100

d.keys()
d.values()
d.items()

print(d['DAC'])

v=d.get('DAC')
print(v)

v=d.get('qwe', -10)
print(v)

v=d.setdefault('DAI', 60)
print(v)

k,v=d.popitem()
print(k,v)

v=d.pop('dhpcsa',-1)
print(v)

v=d.pop('DAI',-1)
print(v)


for k in d.keys():
    if d[k] > 80:
        print(k)
        
for k,v in d.items():
    if v > 80:
        print(k)

#-------------------------------------#
'''
*
**
***
****
*****
'''
n = 5
for i in range(1,n+1):
    print('*' * i)

#-------------------------------------#

'''
*****
****
***
**
*
'''
n = 5
for i in range(n,0,-1):
    print('*' * i)

#-------------------------------------#
'''
    *
   **
  ***
 ****
*****
'''
n = 5
space=n-1
for i in range(1,n+1):
    print(' ' * space,end='')
    print('*' * i)
    space-=1
    
#-------------------------------------#
'''
*****
 ****
  ***
   **
    *
'''
n = 5
space=0
for i in range(n,0,-1):
    print(' ' * space,end='')
    print('*' * i)
    space+=1
#-------------------------------------#

def displayDiamond(num):
    space_count=num//2
    
    for i in range(1,num+1,2):
        print(' ' * space_count, end='')
        print('*' * i)
        space_count-=1
    
    space_count=1
    for i in range(num-2,0,-2):
        print(' ' * space_count , end='')
        print('*' * i)
        space_count += 1
        
        
num = int(input('Enter the number of lines(Only odd number):'))
if num%2 ==0:
    print("Enter odd numbers only!!")
else:
    displayDiamond(num)
    
    
#-------------------------------------#
