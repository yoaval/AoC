import numpy as np
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_20\\input.txt"
index_string : str = ''
steps=51
SZ=100
Shape=(SZ+2*steps,SZ+2*steps)
ar: np.ndarray=np.zeros(Shape,np.int8)
ct=steps
def step(ar:np.ndarray,bound) ->np.ndarray:
    global index_string
    new_ar=np.zeros_like(ar)
    for i in range(bound,ar.shape[0]-bound+1):
        for j in range(bound,ar.shape[0]-bound+1):
            square : np.ndarray=ar[i-1:i+2,j-1:j+2]
            flat=square.flatten()
            num=0
            pow=2**8
            for val in flat:
                num+=val*pow
                pow//=2
            new_ar[i,j]=int(index_string[num])
    return new_ar
def outofbound(ar,bound,val):
    ar[:bound,:]=val
    ar[-bound:,:]=val
    ar[:,:bound]=val
    ar[:,-bound:]=val
def printar(ar):
    for i in range(len(ar)):
        for j in range(len(ar)):
            print('. ',end='') if ar[i,j]==0 else print('# ',end='')
        print()

with open(PATH,'r') as f:
    index_string=f.readline().replace('.','0').replace('#','1').replace('\n','')
    for line in f:
        ar[ct,steps:-steps]=[int(x) for x in line.replace('.','0').replace('#','1').replace('\n','')]
        ct+=1
printar(ar)
print('---------------------')
bound=50
val=1
for _ in range(50):
    ar=step(ar,bound)
    outofbound(ar,bound,val)
    bound-=1
    if val==0:
        val=1
    else:
        val=0
    #printar(ar)
    print('---------------------')
print(np.count_nonzero(ar==1))