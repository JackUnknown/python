'''
1. Write a program that asks the user how many days are in a month, and what day of 
the 
week the month begins on (0 for Monday, 1 for Tuesday, etc), and then prints a calendar for 
that month. 
For example, here is the output for a 31-day month that begins on day 5 (Saturday): 
''' 
num_days = int(input("How many days are in the month? "))
start_day = int(input("Start day (0=Mon, 1=Tue, ..., 6=Sun): "))

print("\nMon Tue Wed Thu Fri Sat Sun")
print("-" * 27)

print("    " * start_day, end="")

current_pos = start_day
for day in range(1, num_days + 1):
    print(f"{day:3}", end=" ")
    
    current_pos += 1
    
    if current_pos == 7:
        print()
        current_pos = 0
            
print("\n")

'''
2. Define a procedure histogram() that takes a list of integers and prints a histogram to 
the screen. For 
example, histogram([4, 9, 7]) should print the following: 
**** 
********* 
******* 
'''
def histogram(lst):
    for n in lst:
        print('*' * n)   
lst = list(map(int,input("Enter the elements of the list: ").split()))
print()
histogram(lst)


'''
3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as  
"Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit 
on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic 
sonatas", "I roamed under it as a tired nude Maori",  "Rise to vote sir", or the 
exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing 
are usually ignored. 
'''

phrase = input("Enter a phrase to check: ")

clean_phrase = "".join(char.lower() for char in phrase if char.isalnum())

if clean_phrase == clean_phrase[::-1] and clean_phrase != "":
    print(f"'{phrase}' is a palindrome.")
else:
    print(f"'{phrase}' is not a palindrome.")

'''
4.  A pangram is a sentence that contains all the letters of the English alphabet at least 
once, for example: The quick brown fox, jumps over the lazy dog!!!!.  
Your task here is to write a function to check a sentence to see if it is a pangram or 
not. 
'''
import string

def is_pangram(str1):
    set1 = set(string.ascii_lowercase)
    
    set2 = set(str1.lower())

    return set1.issubset(set2)

str1 = input("Enter a sentence to check for a pangram: ")

if is_pangram(str1):
    print("Given sentence is a pangram!")
else:
    print("Given sentence is NOT a pangram.")


'''5. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in 
the plain text is replaced by a letter some fixed number of positions down the alphabet. For 
example, with a shift of 3, A would be replaced by D, B would become E, and so on. The 
method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 
("rotate by 13 places") is a widely used  
 
example of a Caesar cipher where the shift is 13. In Python, the key for ROT-13 may be 
represented by means of the following dictionary 
 
 {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 
'p':'c', 
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 
'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'} 
Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, 
you will be able to read the following secret message: 
 
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! 
 
Note that since English has 26 characters, your ROT-13 program will be able to both encode 
and decode texts written in English. 
'''



 
'''
6. Given a dictionary of students and their favourite colours: 
 
people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'} 
1. Find out how many students are in the list 
2. Change Lisa’s favourite colour 
3. Remove 'Jenny' and her favourite colour 
4. Sort and print students and their favourite colours alphabetically by name 
'''

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'} 

stud_cnt = len(people)
print(f"Total students: {stud_cnt}")

people['Lisa'] = 'Green'
print(f"Updated Lisa's color: {people['Lisa']}")

del people['Jenny']
print(f"Dictionary after removing Jenny: \n{people}")

print("\nStudents sorted by name:")
for k in sorted(people.keys()):
    print(f"{k}: {people[k]}")


'''
7. Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's 
language"). 
That is, double every consonant and place an occurrence of "o" in between.  
 
For example, translate("this is fun") should return the string "tothohisos isos fofunon". 
 '''
def translate(text):
    vowels = "aeiouAEIOU"
    result = ""
    
    for char in text:
        if char.isalpha() and char not in vowels:
            result += char + 'o' + char
        else:
            result += char
    return result

message = input("Enter a message: ")
translated_message = translate(message)

print(f"Original: {message}")
print(f"Robber's Language: {translated_message}")
 
 
'''
8. Write a program that contains a function that has one parameter, n, representing an integer 
greater than 0. The function should return n! (n factorial). Then write a main function that calls 
this function with the values 1 through 20, one at a time, printing the returned results. This is 
what your output should look like: 
1 1 
2 2 
3 6 
4 24 
5 120 
6 720 
7 5040 
8 40320 
9 362880 
10 628800 
'''
def calculate_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def main():
    for i in range(1, 21):
        factorial_value = calculate_factorial(i)
        print(f"{i} {factorial_value}")

if __name__ == "__main__":
    main()
    
    
'''
9. Write a recursive sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1: 
1, if x = 1 
x + sum from 1 to x-1  if x > 1 
Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 
+ 10 
 
def main(): 
          # compute and print 1 + 2 + ... + 10 
          print sum(10) 
def sum(x): 
          # you complete this function recursively 
  
main() 
'''
def main(): 
    print(sum_recursive(10)) 

def sum_recursive(x): 
    if x == 1:
        return 1
    else:
        return x + sum_recursive(x - 1)

main()


'''
10.  Define a function overlapping() that takes two lists and returns True if they have at least one 
member in common, False otherwise. 
'''
def overlapping(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    return not set1.isdisjoint(set2)

list1 = list(map(int,input("Enter first list elements: ").split()))
list2 = list(map(int,input("Enter second list elements: ").split()))
print(overlapping(list1, list2))

''' 
11.  Write a function find_longest_word() that takes a list of words and returns the length of the 
longest one. 
'''
def find_longest_word(word_list):
    longest = 0
    
    for word in word_list:
        if len(word) > longest:
            longest = len(word)
            
    return longest

word_list = list(map(str,input("Enter word list elements: ").split()))
print(f"Longest length: {find_longest_word(word_list)}") 


'''
12. Write a function filter_long_words() that takes a list of words and an integer n and returns the 
list of words that are longer than n 
'''
def filter_long_words(word_list, n):
    long_words = []
    
    for word in word_list:
        if len(word) > n:
            long_words.append(word)
            
    return long_words

word_list = list(map(str,input("Enter word list elements: ").split()))
n = int(input("Integer : "))
result = filter_long_words(word_list, n)
print(f"Words longer than {n}: {result}")


'''
13. Define a simple "spelling correction" function correct() that takes a string and sees to it that 
1) two or more occurrences of the space character is compressed into one, and 
2) inserts an extra space after a period if the period is directly followed by a letter. 
 
       e.g. correct("This is very           funny and cool.Indeed!") 
              should return "This is very funny and cool. Indeed!" 
'''

'''
14.  In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A 
simple set of heuristic rules can be given as follows: 
 If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.) 
 If the verb ends in ie, change ie to y and add ing 
 For words consisting of consonant-vowel-consonant, double the final letter before adding 
ing 
 By default just add ing 
Your task in this exercise is to define a function make_ing_form() which given a verb in 
infinitive form 
returns its present participle form. Test your function with words such as lie, see, move and 
hug.
'''
def make_ing_form(verb):
    vowels = ('a', 'e', 'i', 'o', 'u')
    
    # Rule 1: Exceptions for verbs ending in 'e'
    exceptions = ('be', 'see', 'flee', 'knee')
    if verb in exceptions:
        return verb + "ing"

    # Rule 2: Ends in 'ie' -> change to 'y' + 'ing'
    if verb.endswith('ie'):
        return verb[:-2] + "ying"

    # Rule 3: Ends in 'e' -> drop 'e' + 'ing'
    if verb.endswith('e'):
        return verb[:-1] + "ing"

    # Rule 4: Consonant-Vowel-Consonant (CVC) doubling
    # We check the last three characters
    if len(verb) >= 3:
        c1 = verb[-3]
        v1 = verb[-2]
        c2 = verb[-1]
        
        if (c1 not in vowels) and (v1 in vowels) and (c2 not in vowels):
            return verb + c2 + "ing"

    # Rule 5: Default
    return verb + "ing"

# --- Testing the function ---
test_words = ["lie", "see", "move", "hug", "go", "flee"]
for word in test_words:
    print(f"{word} -> {make_ing_form(word)}")
    

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

