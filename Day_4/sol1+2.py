import numpy as np
import shlex
def play(ar,num):
    ar[np.where(ar==num)]=-1

def check(ar,num):
    bingos=[]
    rindex=np.where((ar==(-1,-1,-1,-1,-1)).all(axis=2))[0]
    rows=ar[rindex]
    cindex=np.where((ar.transpose(0,2,1)==(-1,-1,-1,-1,-1)).all(axis=2))[0]
    cols=ar[cindex]
    if rows.shape!=(0,5,5):
        # print(rows)
        # print('--------')
        # print(num)
        for array in rows:
            bingos.append((np.sum(array[np.where(array!=-1)])*num,array))
        ar[rindex]=np.full((5,5),-2)
    if cols.shape!=(0,5,5):
        # print(cols)
        # print('--------')
        # print(num)
        for array in cols:
            bingos.append((np.sum(array[np.where(array!=-1)])*num,array))
        ar[cindex]=np.full((5,5),-2)
    return bingos
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_4\\input.txt"
ar=np.zeros((100,5,5),np.int8)
with open(PATH,'r') as f:
    order=[int(i) for i in f.readline().replace('\n','').split(',')]
    f.readline()
    index=0
    row=0
    for line in f:
        if line=='\n':
            index+=1
            row=0
            continue
        ar[index,row,:]=[int(i) for i in shlex.split(line.replace('\n',''))]
        row+=1
for num in order:
    play(ar,num)
    res=check(ar,num)
    if res!=[]:
        print(res[0][0])

# print(order[5])
# print(ar[2])