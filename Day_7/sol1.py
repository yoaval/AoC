import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_7\\input.txt"
with open(PATH,'r') as f:
    ls=[int(i) for i in f.readline().split(',')]
ls=sorted(ls)
md=np.median(ls)
tot=0
for val in ls:
    tot+=np.abs(md-val)
print(md)
print(tot)