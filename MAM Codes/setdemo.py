# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 17:27:03 2026

@author: anilk
"""

setA={1,2,3,4,5}
setB={4,5,11,12}
print(setA,setB)

#all values of setA and setA and common values
print(setA.union(setB),setA|setB)

#give only common values
print(setA.intersection(setB),setA&setB)

#give all values only in setA
print(setA.difference(setB),setA-setB)

#give all values only in setA and only in setB
print(setA.symmetric_difference(setB),setA^setB)


#give all values only in setA, but also overwrite values in setA
#setA.difference_update(setB)
setA=setA-setB
print(setA)

#give all values only in setA and only in setB, 
#but also modify set
setA.symmetric_difference_update(setB)
setA=setA^setB
print(setA)

setA.add(100)
setA.update([12,13,24,100])
print(setA)

setA.remove(100)
print(setA)

val=setA.pop()
print(val,setA)

setA.remove(100)

setA.discard(100)

setA={34,23,11,"sdsd"}
fsetA=frozenset(setA)




