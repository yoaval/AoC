import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_5\\input.txt"
SIZE=1000
ar=np.zeros((SIZE,SIZE),np.int8)
with open(PATH,'r') as f:
    for line in f:
        pts=[int(i) for i in line.replace('\n','').split(' ')]
        if pts[0]== pts[2]: #x1=x2
            for i in range(np.min(pts[1::2]),np.max(pts[1::2])+1):
                ar[i,pts[0]]+=1
        elif pts[1]== pts[3]:
            for i in range(np.min(pts[0::2]),np.max(pts[0::2])+1):
                ar[pts[1],i]+=1
        else:
            xadd=-1 if pts[0]>pts[2] else 1
            yadd=-1 if pts[1]>pts[3] else 1
            cnt=0
            for i in range(pts[0],pts[2]+xadd,xadd):
                ar[pts[1]+yadd*cnt,pts[0]+xadd*cnt]+=1
                cnt+=1
print(len(np.where(ar>1)[0]))
print(ar)