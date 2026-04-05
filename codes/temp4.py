x = 100
cnt = 0
def myf1():
    
    global cnt

    x = 23
    print("in myf1",x)
    # x= 200
    cnt+=1
    def myf2(): 
        global x
        # nonlocal x
        x=35
        print('in myf2',x)
        print('count: ' ,cnt)
    myf2()
    print('in myf1 after calling myf2', x)
    
    
    
print(x)
myf1()
# print(x)
# print(cnt)
print('in global scope  myf1', x)

#------------------------------------------#

def f1(a,b,c=0,*t,**kwarg):
    print(a,b,c)
    print('tuple', t)
    print('dict', kwarg)
    print()
    
f1(1,2)
f1(1,2,3)
f1(1,2,3,4,5,6)
f1(1,2,3,4,5,6,x=7,y=8,z=9)