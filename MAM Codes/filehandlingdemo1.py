with open("empdata.txt") as fh:
    s=0
    fh.r
    for ln in fh:
        emplst=ln.rstrip("\n").split(",")
        
        s=s+int(emplst[-1])
        

print(f"sum of sal {s}")

empdict={}
with open("empdata.txt") as fh:
    for ln in fh:
        emplst=ln.rstrip("\n").split(",")
        dept=emplst[2]
        #if department key not exists then add it
        if empdict.get(dept)==None:
            empdict[dept]=int(emplst[-1])
        else:
            empdict[dept]=empdict[dept]+int(emplst[-1])
            
for k,v in empdict.items():
    print(f"{k}----->{v}")
            
            
            
            
            
            