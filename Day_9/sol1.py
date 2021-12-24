import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_9\\input.txt"
SZ=100 + 2
ar=np.full((SZ,SZ),11)
with open(PATH,'r') as f:
    ct=1
    for line in f:
        ar[ct,1:-1]=[int(x) for x in list(line.replace('\n',''))]
        ct+=1
tot=0
for x in range(1,SZ-1):
    for y in range(1,SZ-1):
        if ar[x,y]<ar[x+1,y] and ar[x,y]<ar[x-1,y] and ar[x,y]<ar[x,y+1] and ar[x,y]<ar[x,y-1]:
            tot+=ar[x,y]+1
print(tot)