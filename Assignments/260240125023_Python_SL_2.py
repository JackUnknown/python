# Assignment SL 2
# Name: Digvijay Vikas Sawant
# PRN: 260240125023

'''
Python assignments 
1. Write a menu driven program to practice String functions 
Design following meu 
a. display characters from even position 
b. display characters from odd position 
c. display length of a string 
d. add a at the end of string length times 
e. exit 
'''

s = input("Enter a string: ")

choice = 0
while choice != 'e':
    choice=input('''
a. display characters from even position 
b. display characters from odd position 
c. display length of a string 
d. add a at the end of string length times 
e. exit 
Enter your choice (a-e): ''')
    match choice:
        case 'a':
            print(f"Characters at even positions: {s[::2]}")
            
        case 'b':
            print(f"Characters at odd positions: {s[1::2]}")
            
        case 'c':
            print(f"Length of the string: {len(s)}")
            
        case 'd':
            l = len(s)
            new_str = s + ('a' * l)
            print(f"Modified string: {new_str}")
            
        case 'e':
            print("Exiting....")
            break
        case others:
            print("Invalid choice! Please select between a and e.")
        
        
'''
2. Write a program to accept a string from user.  
Accept a second string from user to search and find all occurrences of in the given string. 
e.g  
s1=This is string 
check=is 
is-2 
is-5 
count=2 
s1=”this is cat and cat is cute, where is your cat?” 
check=cat 
cat-8 
cat-16 
cat-43 
count=3 
'''
s1 = input("Enter first string: ")
check = input("Enter second string: ")

count = 0
start_index = 0

print(f"\nSearching for '{check}' in given string...")

while True:
    idx = s1.find(check, start_index)
    
    if idx == -1:
        break
        
    print(f"{check}-{idx}")
    
    count += 1
    start_index = idx + 1

print(f"count={count}")


'''
3. Write a menu driven program to practice List functions. Validate input data wherever 
required. 
Display following menu: 
1. Accept Data 
a) add at last position 
b) add at given position 
2. Delete data by value 
display message deleted successfully  
or not found 
3. delete data by position 
a) delete last element 
b) delete from particular position 
4. sort  
a) ascending  
b) descending 
5. reverse 
6. Print in sorted order without changing original list 
7. print in reverse order without changing original list 
8. display data 
a) normal  
b) numbered 
'''

data_list = []

while True:
    choice = int(input('''
1. Accept Data 
    a) add at last position 
    b) add at given position 
2. Delete data by value
3. delete data by position 
    a) delete last element 
    b) delete from particular position 
4. sort  
    a) ascending  
    b) descending 
5. reverse 
6. Print in sorted order without changing original list 
7. print in reverse order without changing original list 
8. display data 
    a) normal  
    b) numbered

Enter choice (1-9): '''))

    match choice:
        case 1:
            sub = input("  a) Last position\n  b) Given position\n  Choice: ").lower()
            val = input("  Enter value to add: ")
            if sub == 'a':
                data_list.append(val)
            elif sub == 'b':
                try:
                    pos = int(input(f"  Enter position (0-{len(data_list)}): "))
                    data_list.insert(pos, val)
                except ValueError: print("  Invalid position!")

        case 2:
            val = input("  Enter value to delete: ")
            if val in data_list:
                data_list.remove(val)
                print("  Deleted successfully.")
            else:
                print("  Value not found.")

        case 3:
            if not data_list: 
                print("  List is empty!")
                continue
            sub = input("  a) Delete last\n  b) Particular position\n  Choice: ").lower()
            if sub == 'a':
                data_list.pop()
                print("  Last element deleted.")
            elif sub == 'b':
                try:
                    pos = int(input(f"  Enter position (0-{len(data_list)-1}): "))
                    data_list.pop(pos)
                    print(f"  Element at {pos} deleted.")
                except (ValueError, IndexError): print("  Invalid position!")

        case 4:
            sub = input("  a) Ascending\n  b) Descending\n  Choice: ").lower()
            if sub == 'a':
                data_list.sort()
            elif sub == 'b':
                data_list.sort(reverse=True)
            print("  List sorted.")

        case 5:
            data_list.reverse()
            print("  Original list reversed.")

        case 6:
            # sorted() returns a new list
            print("  Sorted order:", sorted(data_list))
            print("  (Original remains unchanged)")

        case 7:
            # Slicing [::-1] creates a reversed copy
            print("  Reverse order:", data_list[::-1])
            print("  (Original remains unchanged)")

        case 8:
            sub = input("  a) Normal\n  b) Numbered\n  Choice: ").lower()
            if sub == 'a':
                print("  List:", data_list)
            elif sub == 'b':
                for i, val in enumerate(data_list):
                    print(f"  {i}: {val}")

        case 9:
            print("Exiting....!")
            break

        case others:
            print("Invalid choice, please select 1-9.")




'''
4.  Create two lists to store cities and locations by accepting values from user.  
Display 1st city  and 1st location 
then 2nd city and 2nd location .......    (zip function) 
'''

cities_input = input("Enter city names separated by space: ")
locations_input = input("Enter corresponding locations separated by space: ")

cities = cities_input.split()
locations = locations_input.split()

if len(cities) != len(locations):
    print(f"\nNote: Lists are uneven ({len(cities)} cities vs {len(locations)} locations).")
    print("Zip will stop at the shortest list length.")

print("\n--- Paired Results ---")

for city, location in zip(cities, locations):
    print(f"City: {city} | Location: {location}")



'''
5. Create a list and exchange the values as index and index as values. 
lst=[12, 1, 3, 7, 8, 5, 8] 
     0   1  2  3  4  5  6 
Output should be as follows. 
initial list 
lst1=[-1 ,1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] 
modified list 
lst1=[-1 ,1, -1, 2, -1, 5, -1, 3, 6, -1, -1, -1, 0] 
'''
lst = [12, 1, 3, 7, 8, 5, 8]
    
max_val = max(lst)

lst1 = [-1] * (max_val + 1)
print(f"Initial list:\n{lst1}")

for i, val in enumerate(lst):
    lst1[val] = i

print(f"\nModified list:\n{lst1}")


'''
6. Write a menu driven program to practice Set functions.  
Write a program to accept names from users and store it in a set. 
Display the following menu: 
print("1. delete element if exists otherwise do not show any errr") 
print("2. add a elemet") 
print("3. create one more set") 
print("4. union of 2 sets") 
print("4. intersection of 2 sets") 
print("5. difference of 2 sets") 
print("6. convert set into frozenset") 
print("6. exit")  
'''

names_input = input("Enter names separated by space for Set 1: ").split()
set1 = set(names_input)
set2 = set()  

while True:
    print("1. Delete element (No error if missing)")
    print("2. Add an element")
    print("3. Create Set 2")
    print("4. Union of Set 1 & Set 2")
    print("5. Intersection of Set 1 & Set 2")
    print("6. Difference (Set 1 - Set 2)")
    print("7. Convert Set 1 to Frozenset")
    print("8. Display current sets")
    print("9. Exit")
    
    choice = int(input("\nEnter choice: "))

    match choice:
        case 1:
            name = input("Enter name to delete: ")
            # discard() removes the element but does NOT raise an error if not found
            set1.discard(name)
            print(f"Set 1 now: {set1}")

        case 2:
            name = input("Enter name to add: ")
            set1.add(name)
            print("Added successfully.")

        case 3:
            names2 = input("Enter names for Set 2: ").split()
            set2 = set(names2)
            print(f"Set 2 created: {set2}")

        case 4:
            print(f"Union: {set1.union(set2)}")

        case 5:
            print(f"Intersection: {set1.intersection(set2)}")

        case 6:
            print(f"Difference (S1 - S2): {set1.difference(set2)}")

        case 7:
            f_set = frozenset(set1)
            print(f"Frozenset created: {f_set}")

        case 8:
            print(f"Set 1: {set1}")
            print(f"Set 2: {set2}")

        case 9:
            print("Exiting...")
            break

        case others:
            print("Invalid option. Please choose 1-9.")


'''
7. Generate a list of lists (NOTE: List should get generated dynamically) 
Accept a number from user and check last digit of the number. 
If it is 1 then add it in the list at 1st position. 
If 0 then it should get added at list in 0th position. 
e.g list should look as follows 
[[10],[51],[52]] 
[[10,30,20,40],[11,31,41,31],[22,32,42]....] 
if user enter 15 then the resultant list should be 
[[10,30,20,40],[11,32,41,31],[22,32,42],[],[],[15]] 
'''
master_list = [[] for _ in range(10)]

# print("Enter numbers to categorize (type 'done' to finish):")

while True:
    user_input = input("Enter numbers to categorize (type 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break
        
    number = int(user_input)
    last_digit = number % 10
    master_list[last_digit].append(number)
    
    print(f"Current Status: {master_list}")

print("\nFinal Resultant List:")
print(master_list)


'''
8. Create a list to store strings in a list in following manner list 
[dxz,axz,bat,rat,cat,pat,bbc,bbm,cbm,....]         
pat axz 
All list with same character at second position should be consecutive. 
If user adds sat, then the resultant list will be: 
[bat,rat,cat,sat,bbc,bbm,cbm,....] 
If user adds pick, then it should be added at  
[bat,rat,cat,bbc,bbm,cbm,pick]
'''
master_list = ["bat", "rat", "cat", "bbc", "bbm", "cbm"]

while True:
    print(f"\nCurrent List: {master_list}")
    new_word = input("Enter a string to add (or 'exit'): ").lower()
    
    if new_word == 'exit':
        break
    
    if len(new_word) < 2:
        print("String must have at least 2 characters.")
        continue

    # Target character at 2nd position
    target_char = new_word[1]
    
    # Find the last occurrence of a string with the same 2nd character
    last_index = -1
    for i, word in enumerate(master_list):
        if len(word) > 1 and word[1] == target_char:
            last_index = i
    
    # If match found, insert after the last element of that group
    if last_index != -1:
        master_list.insert(last_index + 1, new_word)
    else:
        # If no match found, append to the end
        master_list.append(new_word)

print("\nFinal Resultant List:")
print(master_list)



# SL 1 

'''    
15. Write a program  to accept empno, employee name, Salary, Designation 
write the details into a file empdata.dat as : separated values as follows 
empno:empname:salary:designation  
 
Write another program to read contents from the file 
If designation is manager then add bonus=2000 in the salary and display on the screen 
If designation is analyst then add bonus=1500 in the salary 
otherwise add bonus=1000 in the salary 
 
steps to write data into file 
step 1 
    open file empdata.dat in append mode 
Step2   
    Accept empno in variable eno 
    ename in var en 
    salary in var sal 
    designation in var desig 
step 3 
    concatenate all the variable to convert : separated list 
Step 4 
    Write the concatenated string into file 
Step5 
    Repeat step 2 to step 4 till user wants to enter new data 
Step 6 
    Close the file 
 
steps to write data into file 
Step 1: 
   Open file empdata.dat in read mode 
Step 2 
   Read the next  line from file 
Step 3 
   Split the line at : position 
Step 4  
   Check the designation and increase the salary accordingly and display it 
Step 5 
    Repeate step 2 to 4 till file finishes 
Step 6 
    Close the file 
'''

def write_data():
    with open('empdata.dat', 'a') as fh:
        while True:
            eno = input("Enter Emp No: ")
            en = input("Enter Name: ")
            sal = input("Enter Salary: ")
            desig = input("Enter Designation: ")
            
            # Step 3 & 4: Concatenate with : and write
            line = f"{eno}:{en}:{sal}:{desig}\n"
            fh.write(line)
            
            choice = input("Do you want to add more? (y/n): ")
            if choice.lower() != 'y':
                break

def read_and_display():
    try:
        with open('empdata.dat', 'r') as fh:
            print("\n--- Employee Salary Processing ---")
            for ln in fh:
                # Step 3: Split at :
                emplst = ln.rstrip('\n').split(':')
                if len(emplst) < 4: continue
                
                name = emplst[1]
                sal = int(emplst[2])
                desig = emplst[3].lower()
                
                # Step 4: Logic for bonus
                if desig == "manager":
                    bonus = 2000
                elif desig == "analyst":
                    bonus = 1500
                else:
                    bonus = 1000
                
                total_sal = sal + bonus
                print(f"Name: {name} | Desig: {desig.capitalize()} | Total Salary: {total_sal}")
    except FileNotFoundError:
        print("File not found.")

write_data()
read_and_display()


'''
16. Object oriented programming 
 
Write a class MyClass it contains 2 members 
One number and one string 
Write default constructor, parametrized constructor 
Overload +,*,- operator 
 
Ob1=MyClass(12,”abcdserdf”) 
Ob2=Myclass(13,”bxc”) 
Ob3=ob1+ob2      
 
+ - will do the addition of the numbers and Concat 1st 3 characters  of both strings. 
‘-   - subtract numbers and concat last 3 characters of the string 
   
‘*   will do the multiplication of numbers and  
      Concat 1 st character of string length times with first character of second string. 
      ‘aaaaaaaaabbb’ 
'''
class MyClass:
    def __init__(self, num=0, text=""):
        self.num = num
        self.text = text

    def __add__(self, other):
        new_num = self.num + other.num
        new_text = self.text[:3] + other.text[:3]
        return MyClass(new_num, new_text)

    def __sub__(self, other):
        new_num = self.num - other.num
        new_text = self.text[-3:] + other.text[-3:]
        return MyClass(new_num, new_text)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_text = (self.text[0] * len(self.text)) + (other.text[0] * len(other.text))
        return MyClass(new_num, new_text)

    def __str__(self):
        return f"Num: {self.num}, String: {self.text}"

ob1 = MyClass(20, "abce")
ob2 = MyClass(10, "defg")
print(f"Addition: {ob1 + ob2}")
print(f"Subtraction: {ob1 - ob2}")
print(f"Multiplication: {ob1 * ob2}")


'''
17. Inheritance 
 
Create a Person class 
pid,pname,emailed,mobno 
Write init ,setter and getter,display method 
 
Create a class Employee child of Person 
Dept,desg,sal 
Write init,setter,getter, override display method 
Write method calculateNetSal  - 
Netsal=sal+10% of sal+15% of sal-5% of sal  
  
Create a class Member is child of Person 
membertype, amtPaid 
Write init,setter,getter, override display method, 
'''
class Person:
    def __init__(self, pid, pname, email, mobno):
        self.pid = pid
        self.pname = pname
        self.email = email
        self.mobno = mobno
        
    def set_pid(self,pid):
        self.pid=pid
    def get_pid(self):
        return self.pid
    
    def set_pname(self,pnm):
        self.pname=pnm
    def get_pname(self):
        return self.pname
    
    def set_mobno(self,mNo):
        self.pid=mNo
    def get_mobno(self):
        return self.mobno
    
    def set_email(self,em):
        self.email=em
    def get_email(self):
        return self.email

    def display(self):
        print(f"ID: {self.pid}, Name: {self.pname}, Email: {self.email}, Mobile: {self.mobno}")

class Employee(Person):
    def __init__(self, pid, pname, email, mobno, dept, desg, sal=0):
        super().__init__(pid, pname, email, mobno)
        self.dept = dept
        self.desg = desg
        self.sal = sal
    
    def set_dept(self,dept):
        self.dept=dept
    def get_dept(self):
        return self.dept

    def set_desg(self,desg):
        self.desg=desg
    def get_desg(self):
        return self.desg
    
    def set_sal(self,sal):
        self.sal=sal
    def get_sal(self):
        return self.sal

    def calculateNetSal(self):
        return self.sal + (0.10 * self.sal) + (0.15 * self.sal) - (0.05 * self.sal)

    def display(self):
        super().display()
        print(f"Dept: {self.dept}, Desg: {self.desg}, Net Salary: {self.calculateNetSal()}")

class Member(Person):
    def __init__(self, pid, pname, email, mobno, membertype, amtPaid):
        super().__init__(pid, pname, email, mobno)
        self.membertype = membertype
        self.amtPaid = amtPaid
    
    def set_mtype(self, mtype): 
        self.mtype = mtype
    def get_mtype(self): 
        return self.mtype

    def set_amtPaid(self, amt): 
        self.amtPaid = amt
    def get_amtPaid(self): 
        return self.amtPaid

    def display(self):
        super().display()
        print(f"Type: {self.membertype}, Amount Paid: {self.amtPaid}")

print("--- Employee Details ---")
e1 = Employee(101, "ABC", "abc@email.com", "9876543210", "IT", "Analyst", 50000)
e1.display()

print("\n--- Member Details ---")
m1 = Member(501, "Rahul", "rahul@email.com", "9988776655", "Gold", 2000)
m1.display()


'''
18. Database Assignment 
Write a program to display choices to user 
1. Insert---- call insertDept function 
2. Delete---- call deleteDept – delete a particular record 
3. Update---- call updateDept – update details of particular department 
4. Display All --- call displayAllDept – display only department name 
5. Display  ------ call displayDept – display a particular department 
6. Displaydept – will display all the locations which contains or in it 
7. Exit
'''

import pymysql

def displayAllDept():
    cur.execute('Select dname from department')
    print("\nDepartment Names:\n")
    for row in cur.fetchall():
        print(f'Department Name = {row[0]}')

def insertDept():
    did = int(input('Enter Department Id: '))
    dname = input('Enter Department name: ')
    loc = input('Enter Department location: ')
    cur.execute('Insert into department values(%s, %s, %s)', (did, dname, loc))
    conn.commit()

def deleteDept(did):
    cur.execute('Delete from department where did = %s', (did,))
    conn.commit()
    return True

def updateDept(did, dname, loc):
    cur.execute('update department set dname = %s, loc = %s where did = %s', (dname, loc, did))
    conn.commit()
    return True

def displayDept(did):
    cur.execute('Select * from department where did = %s', (did,))
    row = cur.fetchone()
    if row:
        print(f'Id = {row[0]} Name = {row[1]} Location = {row[2]}\n')
    else:
        print(f"No department found with ID {did}")

def displayDeptLocWithOr():
    cur.execute("Select loc from department where loc like '%or%'")
    print("\nLocations containing 'or':\n")
    results = cur.fetchall()
    if results:
        for row in results:
            print(f'Location = {row[0]}')
    else:
        print("No locations found containing 'or'.")

conn = None
try:
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='bda123', db='bdalab')
    if conn != None:
        print('Connection successful')
    else:
        print('Connection failed')
except Exception as e:
    print(f"Error connecting to database: {e}")

try:
    if conn is not None:
        cur = conn.cursor()
        choice = 0 
        while choice != 7:
            choice = int(input('''\n*****************************
1. Insert Department
2. Delete Department
3. Update Department
4. Display All Department Names
5. Display Specific Department
6. Display Locations with 'or'
7. Exit 
*****************************
Enter your choice: '''
)) 
            match choice:
                case 1:
                    insertDept()
                    print('Department Added Successfully')
                case 2:
                    did = int(input('Enter id of the department to delete: '))
                    status = deleteDept(did)
                    if status:
                        print('Department deleted successfully')
                case 3:
                    did = int(input('Enter id of the department to update: '))
                    dname = input('Enter new department name: ')
                    loc = input('Enter new location: ')
                    status = updateDept(did, dname, loc)
                    if status:
                        print('Department details updated successfully')
                case 4:
                    displayAllDept()
                case 5:
                    did = int(input('Enter id of the department: '))
                    displayDept(did)
                case 6:
                    displayDeptLocWithOr()
                case 7:
                    print('\nExiting....')
                    break
                case _:
                    print("Wrong choice, please try again.")
    else:
        print('Application failed to start due to connection issues.')

except Exception as e:
    print(f"An error occurred during execution: {e}")
finally:
    if conn is not None:
        cur.close()  
        conn.close()
        print("Connection closed.")