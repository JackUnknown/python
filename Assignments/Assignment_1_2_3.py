'''Assignment No - 1,2,3
Name - Abhijeet Sawant
PRN = 260240125048
'''


'''
1. A student will not be allowed to sit in exam if his/her attendence is less than 75%. 
Take following input from user 
Number of classes held 
Number of classes attended. 
And print 
percentage of class attended 
Is student is allowed to sit in exam or not. 
'''

classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))

percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {percentage:.2f}%")

if percentage >= 75:
    print("Student IS allowed to sit in the exam.")
else:
    print("Student is NOT allowed to sit in the exam.")
    
    
    
'''
2. 1.accept amount from user and find the minimum number notes required to get the amount 
amount =512 
Notes: 2000,500,100,50,10,5,2,1 
500-1 note 
10  - 1 note 
2-  1 coin 
amount=20550 
2000 – 10 note 
500 – 1 note 
50 -1 note 
'''

amount = int(input("Enter amount: "))
notes = [2000, 500, 100, 50, 10, 5, 2, 1]

print(f"Minimum notes for {amount}:")
for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"{note} - {count} {'note' if note > 2 else 'coin'}")
        
        
'''
3. Modify the above question to allow student to sit if he/she has medical cause. Ask 
user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly. 
'''
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
medical_cause = input("Do you have a medical cause? (Y/N): ").upper()

percentage = (classes_attended / classes_held) * 100
print(f"Attendance Percentage: {percentage:.2f}%")

if percentage >= 75 or medical_cause == 'Y':
    print("Student IS allowed to sit in the exam.")
else:
    print("Student is NOT allowed to sit in the exam.")
    

'''
4. A school has following rules for grading system: 
a. Below 25 - F 
b. 25 to 45 - E 
c. 45 to 50 - D 
d. 50 to 60 - C 
e. 60 to 80 - B 
f. Above 80 - A 
Ask user to enter marks and print the corresponding grade.
'''

marks = int(input("Enter marks: "))

if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"

print(f"Your Grade is: {grade}")


'''
5. Print the output of following statements 
If 
x = 2 
y = 5 
z = 0 
then find values of the following expressions: 
a. x == 2 
b. x != 5 
c. x != 5 && y >= 5 
d. z != 0 || x == 2 
e. !(y < 10)
'''
x = 2 
y = 5 
z = 0

x == 2 
x != 5 
x != 5 and y >= 5 
z != 0 or x == 2 
not(y < 10)


'''
6. Accept number from user and check whether it is divisible by 5 and 11 
if divisible then display appropriate message. 
'''
num = int(input("Enter number: "))
if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print("Not divisible by both.")
    
    
'''
7. Write a program to calculate the electricity bill (accept number of unit from user) according 
to the following criteria : 
Unit                         Price                       
First 100 units            no charge                            
Next 100 units           Rs 5 per unit                           
After 200 units          Rs 10 per unit                          
(For example if input unit is 350 than total bill amount is Rs2000)
'''
units = int(input("Enter units: "))
bill = 0

if units <= 100:
    bill = 0
elif units <= 200:
    bill = (units - 100) * 5
else:
    bill = (100 * 5) + (units - 200) * 10

print(f"Total bill amount: Rs {bill}")


'''
8. Write a program to check whether the last digit of a number( entered by user ) is divisible by 
3 or not. 
'''
num = int(input("Enter number: "))
last_digit = num % 10

if last_digit % 3 == 0:
    print(f"Last digit {last_digit} is divisible by 3")
else:
    print(f"Last digit {last_digit} is not divisible by 3")


'''
9. Write a program to check whether an years is leap year or not 
the year is leap if it satisfies following condition 
• If the year is divisible by 100, then it should also be divisible by 400 then it is leap year 
• otherwise, all other years divisible by 4 and not divisible by 100 then it is leap year. 
'''
year = int(input("Enter year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


'''
10. Write a program to accept the price of a bike and display the road tax and 
insurance to be paid according to the following criteria . also display total amount to 
be paid. 
Cost price (in Rs)             Tax                  Inssurance       
> 100000                       15 %                    20%     
> 50000 and <= 100000          10%                     8%
<= 50000                       5%                      5%               
'''
price = int(input("Enter bike cost price: "))

if price > 100000:
    tax_perc = 15; ins_perc = 20
elif price > 50000:
    tax_perc = 10; ins_perc = 8
else:
    tax_perc = 5; ins_perc = 5

tax_amt = (tax_perc / 100) * price
ins_amt = (ins_perc / 100) * price
total = price + tax_amt + ins_amt

print(f"Tax: Rs {tax_amt}\nInsurance: Rs {ins_amt}\nTotal to be paid: Rs {total}")



#--------------------------------------------------------------------------------#



#LOOP Questions
'''
1. Accept 10 integers from user and print their average value on the screen 
'''

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
print("Average is:", sum(numbers) / len(numbers))



'''
2. Print the following patterns using loop : 
a. 
* 
** 
*** 
**** 
'''
for i in range(1, 5):
    print("*" * i)
    
    
'''    
b. 
  *                    
 ***                
***** 
 *** 
  * 
'''
n = 3

# Upper half
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))

# Lower half
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))


'''    
c. 
1010101
 10101 
  101
   1  
'''
   
n = int(input("Enter the number of digits for the first row: "))

for i in range(n, 0, -2):

    spaces = (n - i) // 2
    print(" " * spaces, end="")

    for j in range(i):
        if j % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")

    print()
    
'''   
d.  
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5 
'''

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


''' 
3. Write a program to find greatest common divisor (GCD)
or highest common factor (HCF) of given two numbers.
'''

a = int(input("First number: "))
b = int(input("Second number: "))

gcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i
print(f"GCD is {gcd}")


'''
4. Take integer inputs from user until he/she presses q 
( Ask to press q to quit after every integer input ). 
Print average and product of all numbers.
'''

nums = []
product = 1
while True:
    val = input("Enter number or 'q' to quit: ")
    if val.lower() == 'q':
        print('Exiting.....')
        break
    n = int(val)
    nums.append(n)
    product *= n

if nums:
    print("Average:", sum(nums)/len(nums))
    print("Product:", product)
    
    
'''
5. Given a number count the total number of digits in a number and 
also find sum of digits of the number. 
'''

num = input("Enter number: ")
digits = [int(d) for d in num]
print("Total digits:", len(digits))
print("Sum of digits:", sum(digits))


'''
6. To display the cube of the number upto given an integer. If the 
given integer is 5, then display cube of 1 to 4.
'''
n = int(input("Enter integer: "))
for i in range(1, n):
    print(f"Cube of {i} is {i**3}")
    
    
'''    
7. Accept 20 numbers from user and display sum of only even numbers. 
'''
even_sum = 0
for i in range(20):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even_sum += num
print("Sum of even numbers:", even_sum)


'''
8. Ask user number of terms to be generated of a series. 
generate numbers for the following series and find its addition 
[9 + 99 + 999 + 9999+……..] 
'''

terms = int(input("Number of terms: "))
total, start = 0, 9
for i in range(terms):
    total += start
    start = start * 10 + 9
print("Addition:", total)


'''
9. Write a program in python to display the sum of the series 
[ 1+x+x^2/2!+x^3/3!+....]. Go to the editor 
Test Data : 
Input the value of x :3 
Input number of terms : 5 
Expected Output : 
The sum is : 16.375000 
'''

import math
x = int(input("Value of x: "))
n = int(input("Number of terms: "))
total = 1.0
for i in range(1, n):
    total += (x**i) / math.factorial(i)
print(f"The sum is: {total:.2f}")


'''
10. Write a program in python to find the sum of the series 
[ x - x^3 + x^5 + ......]. Go to the editor 
Test Data : 
Input the value of x :2 
Input number of terms : 5 
Expected Output : 
The values of the series: 
2 -8 
32 -128 
512 
The sum = 410
'''

x = int(input("Value of x: "))
n = int(input("Number of terms: "))
total = 0
sign = 1
for i in range(n):
    term = (x**(2*i + 1)) * sign
    print(term)
    total += term
    sign *= -1
print("The sum =", total)



'''String Questions'''

'''
1. Given a string of odd length greater than 7, return a new string 
made of the middle three characters of a given String 
Given: 
str1 = "RakeshzipPetabb" 
Output 
zip 
str2 = "JazzbonAyxx" 
Output 
bon 
'''

def get_middle(s):
    mid = len(s) // 2
    return s[mid-1 : mid+2]

print(get_middle("RakeshzipPetabb")) 
print(get_middle("JazzbonAyxx"))


'''
2. Given two strings, s1 and s2, create a new string by appending 
s2 in the middle of s1 
Given: 
s1 = "Ault" 
s2 = "Kelly" 
Expected Output: 
AuKellylt 
'''

s1, s2 = "Ault", "Kelly"
mid = len(s1) // 2
res = s1[:mid] + s2 + s1[mid:]
print(res) 


'''
3. two strings, s1, and s2 return a new string made of the first, 
middle, and last characters each 
input string 
Given: 
s1 = "America" 
s2 = "Japan" 
Expected Output: 
AJrpan 
'''  

def mix_string(s1, s2): 
    first_char = s1[:1] + s2[:1] 
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1] 
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char 
    print("Mix String is ", res) 
s1 = "America" 
s2 = "Japan" 
mix_string(s1, s2) 


'''
4. Given an input string with the combination of the lower and upper case arrange characters 
in such a way that all lowercase letters should come first. 
'''
str1 = "PytHONStudy" 
lower = [] 
upper = [] 
for char in str1: 
    if char.islower(): 
        lower.append(char) 
    else: 
        upper.append(char) 
    sorted_string = ''.join(lower + upper) 
print("arranging characters giving precedence to lowercase letters:") 
print(sorted_string)

'''
5. create a third-string made of the first char of s1 then the last char of s2, Next, the second 
char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the 
result. 
Given: 
s1 = "Abc" 
s2 = "Xyz" 
Expected Output: 
AzbycX 
''' 

s1 = "Abc"
s2 = "Xyz"
s2 = s2[::-1] 
len1 = len(s1)
len2 = len(s2)
length = len1 if len1 < len2 else len2
result = ""
for i in range(length):
    result += s1[i] + s2[i]
result += s1[length:] + s2[length:]
print("Result:", result) 


'''  
6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also 
display the position 
Given: 
str1 = "Welcome to USA. usa awesome, isn't it?
'''

str1 = "Welcome to USA. usa awesome, isn't it?"
sub = "USA"
temp_str = str1.upper()
index = temp_str.rfind(sub)
print(f"Last occurrence of {sub} starts at index {index}")


'''
List examples 
''' 

'''
Write programs using lists in python 
1. Reverse a given list in Python 
aLsit = [100, 200, 300, 400, 500] 
output: 
[500, 400, 300, 200, 100] 
''' 
lst = [100, 200, 300, 400, 500] 
lst.reverse()
print(lst)


'''
2.  Concatenate two lists index-wise 
Given: 
list1 = ["M", "na", "i", "Raj"] 
list2 = ["y", "me", "s", "esh"] 
output: 
['My', 'name', 'is', 'Rajesh'] 
''' 

list1 = ["M", "na", "i", "Raj"] 
list2 = ["y", "me", "s", "esh"]
result = []
for x,y in zip(list1,list2):
    tp = (x+y)
    result.append(tp)
print(result)


'''
3.  Given a Python list of numbers. Turn every item of a list into its square 
aList = [1, 2, 3, 4, 5, 6, 7] 
output: 
[1, 4, 9, 16, 25, 36, 49] 
'''

List1 = [1, 2, 3, 4, 5, 6, 7] 
result = []
for i in List1:
    sq=i*i
    result.append(sq)
    
print(result)


'''
4. Concatenate two lists in the following order 
list1 = ["Hello ", "Welcome "] 
list2 = ["Students", "Sir"] 
output: 
['Hello Students ', 'Hello Sir', 'welcome Students ', 'Welcome Sir'] 
'''
list1 = ["Hello ", "Welcome "] 
list2 = ["Students", "Sir"] 
result=[]
for x in list1:
    for y in list2:
        result.append(x + " " + y)
print(result)


'''
5.  Given a two Python list. Iterate both lists simultaneously such that list1 should display item 
in original order and list2 in reverse order 
list1 = [10, 20, 30, 40] 
list2 = [100, 200, 300, 400] 
output: 
10 400 
20 300 
30 200 
40 100 
'''

list1 = [10, 20, 30, 40] 
list2 = [100, 200, 300, 400] 

for i,j in zip(list1,reversed(list2)):
    print(i , ' ' , j)


'''
6.  Remove empty strings from the list of strings 
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"] 
output: 
["Ashish",  "Atharva", "Amit",  "Revati"] 
'''

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"] 
for i in list1:
    if i=='':
        list1.remove(i)
print(list1) 
  
# OR

result = [name for name in list1 if name != ""]
print(result)


'''
7.  Add item 7000 after 6000 in the following Python List 
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
output: 
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] 
'''

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40] 
list1[2][2].append(7000)
print(list1)


'''
8.  Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look 
like the following list 
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
Sub List to be added = ["h", "i", "j"] 
output: 
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'] 
'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
sublist =['h','i','j']
list1[2][1][2].extend(sublist)
print(list1)


'''
9.  Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only 
update the first occurrence of a value 
list1 = [5, 10, 15, 20, 25, 50, 20] 
output: 
list1 = [5, 10, 15, 200, 25, 50, 20] 
'''

list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200
print(list1)


'''
10.  Given a Python list, remove all occurrence of 20 from the list 
list1 = [5, 20, 15, 20, 25, 50, 20] 
output: 
[5, 15, 25, 50]
'''

list1 = [5, 20, 15, 20, 25, 50, 20] 
list1 = [x for x in list1 if x != 20]
print(list1)

#OR

list1 = [5, 20, 15, 20, 25, 50, 20] 
for num in list1:
    if num == 20:
        list1.remove(num)
print(list1)


'''
Set examples 
''' 

'''
1. Add a list of elements to a given set 
Given: 
sampleSet = {"Yellow", "Orange", "Black"} 
sampleList = ["Blue", "Green", "Red",”Yellow”,”orange”] 
'''

sampleSet = {"Yellow", "Orange", "Black"} 
sampleList = ["Blue", "Green", "Red","Yellow","orange"]
sampleSet.update(sampleList)
print(sampleSet)


'''
2. display common elements from the given set 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
'''

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))


'''
3. Generate a new set with all items from both sets by removing numbers which are in both 
sets. 
set1 = {10, 20, 30, 40, 50,25} 
set2 = {30, 40, 50, 60, 70,100} 
o/p : order is not important 
{70, 10, 20, 60,25,100} 
'''

set1 = {10, 20, 30, 40, 50, 25} 
set2 = {30, 40, 50, 60, 70, 100} 
result = set1.symmetric_difference(set2)
print(result)


'''
4. Perform following operations on both sets and find the output 
Intersection, difference, union, difference, symmetric_difference, 
symmetric_difference_update, difference_update 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
'''

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 

print("Intersection:", set1.intersection(set2)) 
print("Difference (set1-set2):", set1.difference(set2)) 
print("Union:", set1.union(set2)) 
print("Symmetric Difference:", set1.symmetric_difference(set2)) 
set1.difference_update(set2) 
print("Set1 after difference_update:", set1)
set1.symmetric_difference_update(set2) 
print("Set1 after symmetric_difference_update:", set1)


'''
5. Update set1 by adding items from set2, which are > avg of all values in set1 
set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 
'''

set1 = {10, 20, 30, 40, 50} 
set2 = {30, 40, 50, 60, 70} 

avg = sum(set1) / len(set1) 
print("Average of set1:", avg)

for item in set2:
    if item > avg:
        set1.add(item)
print("Updated set1:", set1)


'''
6. Write a program to accept multiple values from user and add it in the set. And display only 
string with length of the strings>n (note: accept value of n from user) 
''' 

set1 = set()
n = int(input("Enter the minimum string length: "))
print("Enter values one by one. enter q to stop")
while True:
    value = input("Enter value: ")
    if value.lower() == 'q':
        break
    set1.add(value)

print(f"\nstrings with length of the strings > {n}:")
for item in set1:
    if len(item) > n:
        print(item)


'''
Dictionary examples 
''' 

'''
1. the two lists convert it into the dictionary 
keys = ['Ten', 'Twenty', 'Thirty'] 
values = [10, 20, 30] 
Expected output: 
{'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
'''

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d = dict(zip(keys, values))
print(d)


'''
2. Merge following two Python dictionaries into one 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
Expected output: 
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
'''

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} 
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50} 
dict3 = {**dict1, **dict2}  
print(dict3) 


'''
3. Display the value of key history from the following dictionary 
the value of key ‘history’ from the below dict 
sampleDict = {  
"class":{  
      "student":{  
         "name":"Mike", 
         "marks":{  
            "physics":70, 
            "history":80 
         } 
      } 
   } 
} 
'''

sampleDict = {  
"class":{  
      "student":{  
         "name":"Mike", 
         "marks":{  
            "physics":70, 
            "history":80 
         } 
      } 
   } 
} 
print(sampleDict['class']['student']['marks']['history'])
 

'''
4. Delete set of keys from a dictionary 
Given: 
sampleDict = { 
  "name": "Kelly", 
  "age":25, 
  "salary": 8000, 
  "city": "New york"   
} 
keysToRemove = ["name", "salary"] 
'''

sampleDict = { 
  "name": "Kelly", 
  "age":25, 
  "salary": 8000, 
  "city": "New york"   
} 
keysToRemove = ["name", "salary"]

for key in keysToRemove:
    sampleDict.pop(key, None)

print(sampleDict)


''' 
5. display all the keys with value 200 from the following dictionary. 
sampleDict = {'a': 100, 'b': 200, 'c': 300,’d’:200} 
''' 

sampleDict = {'a': 100, 'b': 200, 'c': 300,'d':200} 
for k,v in sampleDict.items():
    if v == 200:
        print(k,v)


'''
6. Rename key city to location in the following dictionary 
sampleDict = { 
  "name": "Kelly", 
  "age":25, 
  "salary": 8000, 
  "city": "New york" 
} 
Expected output: 
 
{ 
  "name": "Kelly", 
"age":25, 
"salary": 8000, 
"location": "New york" 
} 
''' 

sampleDict = { 
  "name": "Kelly", 
  "age":25, 
  "salary": 8000, 
  "city": "New york" 
} 
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)


'''
7. display the key of a maximum value from the following dictionary 
sampleDict = { 
'Physics': 82, 
'Math': 65, 
'history': 75 
} 
'''

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

max_key = None
max_value = 0 

for k, v in sampleDict.items():
    if v > max_value:
        max_value = v
        max_key = k

print("The key with the maximum value is:", max_key)

#OR

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}

max_key = max(sampleDict, key=sampleDict.get)
print(max_key)

'''
8. Accept name and new salary for a employee, modify salary of the employee. 
display appropriate message if salary modified. or if name not found. 
note : the new salary should be > current salary otherwise show message wrong salary. 
sampleDict = { 
'emp1': {'name': 'Jhon', 'salary': 7500}, 
'emp2': {'name': 'Emma', 'salary': 8000}, 
'emp3': {'name': 'Brad', 'salary': 6500} 
}
'''

sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

name = input("Enter employee name: ")
salary = int(input("Enter new salary: "))

found = False
for key, values in sampleDict.items():
    if values['name'] == name:
        found = True
        if salary > values['salary']:
            values['salary'] = salary
            print(f"Success: Salary updated for {name} to {values['salary']}")
        else:
            print("Wrong salary.")
        break

if not found:
    print("Name not found.")

