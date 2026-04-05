# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:40:25 2026

@author: anilk
"""

s="This is string"
print(" s[::-1] reverse order",s[::-1])
print(" s[3:8] 3 to 7 characters",s[3:8])
print(" s[::2] alternate characters even index",s[::2])
print(" s[1::2] alternate characters odd index",s[1::2])


#find 
s="this is my cat, where is your cat, the cat is cute"
pos=s.find("cat")   #11
print(pos)

pos=s.find("cat",pos+1)   #12
print(pos)




#rfind
pos=s.rfind("cat")   #11
print(pos)

pos=s.rfind("cat",0,pos-1)   #12
print(pos)


#index
pos=s.index("cat")   #11
print(pos)

pos=s.index("cat",pos+1)   #12
print(pos)



s="xxxaaaab bbyyThis is testing bb aabbxx"
print(s.strip("xab y"))
print(s.rstrip("xab y"))
print(s.lstrip("xab y"))

s="There is a rain in SPAIN,and in plain"
print(s.replace("ain","xxxxxxx",count=1))


s="thisischeck"
print(s.isalpha())
print(s.isalnum())


