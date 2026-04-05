#using exception handling
try:
    fh=open("test1.txt")
    for line in fh:
        print(line.rstrip('\n'))
except:
    print("error occured")
finally:
    fh.close()

    
#as soon as with finishes, it will close the file
with open("test1.txt") as fh:
    for line in fh:
        print(line.rstrip('\n'))

#copy of the file
with open("test1.txt") as fh:
    with open("test2.txt","w") as fh1:
        for line in fh:
            fh1.write(line)

import re    
with open("test1.txt") as fh:
    with open("test2.txt","w") as fh1:
        for line in fh:
            m=re.search(r"\d$",line)
            if m!=None:
                fh1.write(line.upper())    
    
    
    
    
    
    
    