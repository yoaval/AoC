PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_16\\input.txt"
input='target area: x=117..164, y=-140..-89'
#real
minX=117
maxX=164
minY=-140
maxY=-89
startX=0
startY=0
#test
# minX=20
# maxX=30
# minY=-10
# maxY=-5
# startX=0
# startY=0
def minhelper(n):
    if n==-1:
        return 1000
    return n
def posX():
    l=[]#(val,min step,max step)
    currx=0
    for x in range (1,maxX+1):
        pos=0
        steps=set()
        currx=x
        step=0
        while currx>0:
            pos+=currx
            currx-=1
            step+=1
            if minX<=pos<=maxX:
                steps.add(step)
                if currx==0:
                    steps.add(-1)
        if len(steps)>0:
            l.append((x,steps))
    return l
def posY():
    l=[]#(val,min step,max step)
    curry=0
    for y in range (minY,abs(minY)):
        pos=0
        steps=set()
        curry=y
        step=0
        while pos>=minY:
            pos+=curry
            curry-=1
            step+=1
            if minY<=pos<=maxY:
                steps.add(step)
        if len(steps)>0:
            l.append((y,steps))
    return l

X=posX()
Y=posY()
# print(X)
# print('-------------')
# print(Y)
# print('-------------')

Yi=len(Y)-1
Xi=0
poss=[]
maxys=-1
while Yi>=0:
    Xi=0
    for Xi in range(len(X)):
        if -1 in X[Xi][1]:
            if max(Y[Yi][1])>=min(X[Xi][1],key=minhelper):
                poss.append((X[Xi][0],Y[Yi][0]))   
                if Y[Yi][0]>maxys:
                    maxys=Y[Yi][0]
        else:
            inter=X[Xi][1].intersection(Y[Yi][1])
            if len(inter)>0:
                poss.append((X[Xi][0],Y[Yi][0]))
                if Y[Yi][0]>maxys:
                    maxys=Y[Yi][0]
    Yi-=1
print(len(poss))
print((maxys+1)*(maxys)//2)


