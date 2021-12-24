import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_6\\input.txt"
def day(fisharr):
    new=fisharr[0]
    for i in range(len(fisharr)-1):
        fisharr[i]=fisharr[i+1]
    fisharr[len(fisharr)-1]=new
    fisharr[6]+=new
    return fisharr
with open(PATH,'r') as f:
    l=[int(i) for i in f.readline().replace('\n','').split(',')]
fisharr=[0 for i in range(9)]
for i in l:
    fisharr[i]+=1
for i in range(256):
    fisharr=day(fisharr)
print(sum(fisharr))
