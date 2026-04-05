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