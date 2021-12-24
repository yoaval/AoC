import numpy as np
import queue
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_15\\input.txt"
#SZ=10*5
SZ=100*5
DX=[-1,0,1,0]
DY=[0,1,0,-1]
ar=np.zeros((SZ,SZ),np.int16)
def djk():
    global ar,DX,DY
    removed=set()
    q=queue.PriorityQueue()
    dist={}
    mind=(0,0)
    dist[mind]=0
    prev={}
    for i in range(SZ):
        for j in range(SZ):
            if i!=0 or j!=0:
                prev[(i,j)]=None
                dist[(i,j)]=10001
            q.put((10001,(i,j)))
    while q.empty()==False:
        u=q.get()
        if u in removed:
            continue
        y=u[1][0]
        x=u[1][1]
        for i in range(4):
            yy=y+DY[i]
            xx=x+DX[i]
            if 0<=xx<SZ and 0<=yy<SZ:
                alt=dist[u[1]]+ar[u[1][0],u[1][1]]
                if alt<dist[(yy,xx)]:
                    removed.add((dist[(yy,xx)],(yy,xx)))
                    dist[(yy,xx)]=alt
                    prev[(yy,xx)]=u[1]
                    q.put((alt,(yy,xx)))
    return dist,prev



with open(PATH,'r') as f:
    i=0
    for line in f:
        ar[i,:SZ//5]=[int(x) for x in line.replace('\n','')]
        i+=1
for i in range(5):
    for j in range(5):
        if i==0 and j==0:
            continue
        nar=ar[:SZ//5,:SZ//5].copy()
        nar+=(i+j)
        nar[nar>=10]+=1
        nar%=10
        ar[(SZ//5)*i:(SZ//5)*(i+1),(SZ//5)*j:(SZ//5)*(j+1)]=nar.copy()
dist,prev=djk()
loc=(SZ-1,SZ-1)
tot=0
while loc!=(0,0):
    #print(f'{loc}:{ar[loc]}')
    tot+=ar[loc]
    loc=prev[loc]
print(tot)

