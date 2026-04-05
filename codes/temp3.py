import re

s = 'Something is there somewhere'

m = re.search('s.*e', s, re.I | re.M)
m.span()
m.group()
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
else:
    print('Not found')
    
#---------------------------------------------#   
    
s = 'Something is there somewhere'

m = re.match('s.*e', s, re.I | re.M)
m.span()
m.group()
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
else:
    print('Not found')
    
#---------------------------------------------#   
    
s = 'Something is there somewhere'

m = re.search('s.*?e', s, re.I | re.M)
m.span()
m.group()
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
else:
    print('Not found')
    
#---------------------------------------------#   


s1 = "This is home"

m = re.search(r"^\w+\s\w+\s\w+", s1)
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
else:
    print('Not found')

#---------------------------------------------#   


s1 = "This is home"

m = re.search(r"^(\w+)\s(\w+)\s\w+", s1)
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
    print('group 1 : ' , m.group(1))
    print('group 2 : ' , m.group(2))
else:
    print('Not found')
    
#---------------------------------------------#   
  

s2 = "This is account number #XXXXX1234XXXXX"

m = re.search(r"#X{5}(\d{4})X{5}", s2)
if m != None:
    print('group: ' , m.group())
    print('Account number is: ' , m.group(1))
    print('span: ' , m.span(1))
else:
    print('Not found')

#---------------------------------------------#   



s3 = "My customer number is 2323 This is account number #XXXXX1234XXXXX"

m = re.search(r"#X{5}(\d{4})X{5}$", s3)
if m != None:
    print('group: ' , m.group())
    print('Account number is: ' , m.group(1))
    print('span: ' , m.span(1))
else:
    print('Not found')

#---------------------------------------------#   


s = 'Something is there somewhere'

lst = re.findall('s.*?e', s, re.I)

if lst != None:
    print(lst)
else:
    print('Not found')
    
#---------------------------------------------#   

   
s = 'Something is there somewhere'

mlst = re.finditer('s.*?e', s, re.I)

if mlst != None:
    for m in mlst:
        print('span: ' , m.span())
        print('group: ' , m.group())
else:
    print('Not found')
    
#---------------------------------------------#   


s = 'Something is there somewhere'
new_str=re.sub(r's.*?e', 'abcd', s, flags=re.I)
print(s,new_str)

#---------------------------------------------#  


s = 'Something is there somewhere'
new_str=re.sub(r's.*?e', 'abcd', s,count= 1, flags=re.I)
print(s,new_str)

#---------------------------------------------#  


s = 'Something is there somewhere'

myreg= re.compile("s.*?e", re.I)
m = myreg.search(s)
if m != None:
    print('span: ' , m.span())
    print('group: ' , m.group())
else:
    print('Not found')

#---------------------------------------------#  

s = 'Something is there somewhere'

lst = myreg.findall(s)
if lst != None:
    print(lst)
else:
    print('Not found')
