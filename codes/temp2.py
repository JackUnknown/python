n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1>n2 and n1>n3:
    print(f"{n1} is maximum")
elif n2>n1 and n2>n3:
    print(f"{n2} is maximum")
else:
    print(f"{n3} is maximum")
    
#----------------------------------------------------------#

for i in range(1,11,2):
    print(i,end=' ')
print()

#----------------------------------------------------------#

num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")
    
#----------------------------------------------------------#

num=3456
sum1=0
while num>0:
    d=num%10
    num=num//10
    sum1=sum1+d
print(f"digit sum is {sum1}")

#----------------------------------------------------------#

#Find number prime or not prime?
num = int(input("Enter the number: "))
for i in range(2,num//2+1):
    if num%i==0:
        print("Not prime")
        break
else:
    print("Prime")
    
#----------------------------------------------------------#

num = int(input("Enter the number: "))
match num:
    case 10:
        print("Number is 10")
    case 20:
        print("Number is 20")
    case others:
        print("Number is not 10 or 20")
  
#----------------------------------------------------------#
        
color=input("Enter the color: ")
match color:
    case 'Red'|'Yellow':
        print('Color is Red of yellow')
    case 'green':
        print("color is green")
    case _:
        print("color is blue")

#----------------------------------------------------------#

s = "This is string"; 
print(s[::2])

#----------------------------------------------------------#

# 1,   ABC,   40,  50,  60
# 2,   XYZ,   60,  70,  80
# 3,   PQR,   80,  90,  70