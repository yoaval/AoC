import numpy as np
flashes=0
def flash(ar):
    global flashes
    DX=[-1,-1,0,1,1,1,0,-1]
    DY=[0,1,1,1,0,-1,-1,-1]
    while True:
        toflash=np.where(ar>9)

        s=ar[toflash].shape
        if s==(0,):
            break
        idx = len(toflash[0])
        for i in range(idx):
            bidx,bidy=toflash[0][i],toflash[1][i]
            ar[bidx,bidy]=-100
            flashes+=1
            for ii in range(8):
                bidx2=bidx+DX[ii]
                bidy2=bidy+DY[ii]
                if 0<=bidx2<SZ and 0<=bidy2<SZ:
                    ar[bidx2,bidy2]+=1
    return ar

def afterflash(ar):
    ar[np.where(ar<0)]=0
    return ar
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_11\\input.txt"
SZ=10
ar=np.zeros((SZ,SZ),np.int8)
cnt=0
DAYS=10000
with open(PATH,'r') as f:
    for line in f:
        ar[cnt,:]=[int(c) for c in line.replace('\n','') ]
        cnt+=1
for i in range(DAYS):
    ar+=1
    fb=flashes
    ar=afterflash(flash(ar))
    fa=flashes
    if (fa-fb)==100:
        print(i+1)
        break
    # print(ar)
    # print('-------------')
print(flashes)

