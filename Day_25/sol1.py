import numpy as np
from numpy.core.numeric import array_equal
PATH = "C:\\Users\\yoav\\Documents\\AoC\\Day_25\\input.txt"
H=137
W=139
# W=10
# H=9
ar=np.zeros((H,W),np.int8)
dic={
    '.':0,
    '>':1,    
    'v':2,    

}
rdic={
    0 :'. ',
    1 :'> ',    
    2 :'v '    

}
def mover(l,W,H):
    global ar

    #explaining those lines - we look on all coulmns and for each coulmn we want to look at every pair of adjacent cordinates
    # than we want to look at when this is equal to our value and than a 0
    tmp1=(ar[:,np.arange(W-1)[:,None]+np.arange(2)]==[l,0]).all(2)
    tmp2=(ar[:,0::W-1]==[0,l]).all(1)
    ar[:,:-1][tmp1]=0
    ar[:,1:][tmp1]=l
    ar[tmp2,0::W-1]=[l,0]
def moved():
    global ar
    ar=ar.T
    mover(2,H,W)
    ar=ar.T
def step():
    mover(1,W,H)
    moved()
def printar(ar):
    for i in range(H):
        for j in range(W):
            print(f'{rdic[ar[i,j]]}',end='')
        print('')
    print('------------------------------')


with open(PATH,'r') as f:
    for i,line in enumerate(f):
        ar[i,:]=[dic[x] for x in line.strip()]
steps=0
while True:
    par=ar.copy()
    step()
    steps+=1
    if array_equal(par,ar):
        print(steps)
        break

