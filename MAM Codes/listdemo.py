# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 09:12:30 2026

@author: anilk
"""

lst=[12,13,1,3,4,6]
num=13
print(num in lst)
#add 34 at the end
lst.append(34)
print(lst)

#add list as single value at the end
lst.append([10,20,30])

#find length of the list
print(len(lst))

#add 3 values at the end
lst.extend([10,20,30])
print(len(lst))

#add 3 values at the end
lst.extend((2,3,4))

#add one string at the end
lst.append('test')
print(lst)
#add 4 characters at the end
lst.extend('test')
print(lst)

lst.insert(2,100)
print(lst)

#to delete from the end
lst.pop()
print(lst)

#to delete from 3 rd index position
lst.pop(3)
print(lst)

#to delete by value if found otherwise throw exception
lst.remove(100)
print(lst)

#to count occurences of a number
lst.count(10)

# to create a shallow copy
lst1=lst.copy()

#reverse the list
lst.reverse()
print(lst)  #reversed list
print(lst1) #original list


#to sort the list
lst.sort() #sort in ascending order
print(lst)

lst.sort(reverse=True)
print(lst)


























