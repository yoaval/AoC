import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_9\\input.txt"
SZ=100 + 2
ar=np.full((SZ,SZ),11)
vis=set()
def areasize(x,y):
    global vis
    if ar[x,y]==11 or ar[x,y]==9:
        return
    elif (x,y) in vis:
        return 
    else: 
        #(x,y) not in vis:
        vis.add((x,y))
        areasize(x+1,y)
        areasize(x-1,y)
        areasize(x,y+1)
        areasize(x,y-1)


with open(PATH,'r') as f:
    ct=1
    for line in f:
        ar[ct,1:-1]=[int(x) for x in list(line.replace('\n',''))]
        ct+=1
tot=0
sizes=[]
for x in range(1,SZ-1):
    for y in range(1,SZ-1):
        if ar[x,y]<ar[x+1,y] and ar[x,y]<ar[x-1,y] and ar[x,y]<ar[x,y+1] and ar[x,y]<ar[x,y-1]:
            #found a low
            areasize(x,y)
            sizes.append(len(vis))
            vis=set()
print(sorted(sizes)[-3:])