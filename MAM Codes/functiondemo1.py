def f1(a,b,c=2,*t,**kwarg):
    print(a,b,c)
    print("tuple",t)
    print("dictionary",kwarg)
    
f1(12,23)
f1(11,22,33)
f1(11,22,33,4,5,6,7,1,2)
f1(11,22,33,4,5,6,7,1,2,x=23,y=45,z=67)
