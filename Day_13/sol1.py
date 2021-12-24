import numpy as np
# SW=11
# SH=15
SW=1311
SH=895
ar=np.zeros((SH,SW),np.int8)
cuts=[]
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_13\\input.txt"
def ycut(index,ar):
    idxs=np.where(ar==1)
    pc=len(idxs[0])
    for val in range(pc):
        if idxs[0][val]>index:
            ar[2*index-idxs[0][val],idxs[1][val]]=1
    return ar[:index,:]
def xcut(index,ar):
    idxs=np.where(ar==1)
    pc=len(idxs[0])
    for val in range(pc):
        if idxs[1][val]>index:
            ar[idxs[0][val],2*index-idxs[1][val]]=1
    return ar[:,:index]
with open(PATH,'r') as f:
    for line in f:
        if line[0]!='f':
            star=[int(x) for x in line.split(',')]
            ar[star[1],star[0]]+=1
        else:
            if line.find('x')!=-1:
                cuts.append((int(line.split('=')[1].replace('\n','')),'x'))
            else:
                cuts.append((int(line.split('=')[1].replace('\n','')),'y'))
# print(cuts)
# print('---------')
for val in cuts:
    if val[1]=='y':
        ar=ycut(val[0],ar)
        print(len(np.where(ar==1)[0]))
    else:
        ar=xcut(val[0],ar)
        print(len(np.where(ar==1)[0]))
print(ar)


