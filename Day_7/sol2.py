import numpy as np
def cost(ls,loc):
    tot=0
    for val in ls:
        tot+=(np.abs(val-loc)+1)*np.abs(val-loc)/2
    return tot
def bins(ls,mn,mx,mnv=None,mxv=None):
    pass
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_7\\input.txt"
with open(PATH,'r') as f:
    ls=[int(i) for i in f.readline().split(',')]
ls=sorted(ls)
mn=np.min(ls)
mx=np.max(ls)
tmp=0
min=9999999999
for val in range(mn,mx):
    tmp=cost(ls,val)
    if tmp<min:
        min=tmp
        print(min)
