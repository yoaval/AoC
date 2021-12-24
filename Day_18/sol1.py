import ast
from typing import Any, List, Union
from copy import deepcopy
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_18\\input.txt"
l=[]
def add(l1,l2):
    return [l1,l2]
def parse(l):
    while True:    
        ct=0
    #first pass looks for explode
        while True:
            i2expl=explode(l,[])
            if i2expl:
                ct+=1
                vals=fetchobj(l,i2expl)
                propleft(l,i2expl,vals[0])# type: ignore
                propright(l,i2expl,vals[1])# type: ignore
                zeroout(l,i2expl)
            if i2expl==None:
                break
        # second pass looks for split
        b=split(l)
        if ct==0 and b!=True:
            return l
def split(l):
     for val in range(2):
        try:
            if l[val]>=10:
                l[val]=[l[val]//2,l[val]//2 if l[val]%2==0 else l[val]//2 + 1]
                return True
            elif l[val]<10:
                continue
        except:
            b=split(l[val])
            if b:
                return True
def fetchobj(l:list,index_list:list):
    t=l
    for i in index_list:
        try:
            t=t[i]
        except:
            return None
    return t
def addobj(l:list,index_list:list,val:int):
    t=l
    for i in index_list[:-1]:
        t=t[i]
    t[index_list[-1]]+=val # type: ignore
def propleft(l:list,index_list:list,val:int) :
    idlistcopy=index_list.copy()
    idlistcopy.append(1)
    for i in range(len(idlistcopy)-2,-1,-1):
        if idlistcopy[i]==1:
            idlistcopy[i]=0
            for j in range(i+1,len(idlistcopy)):
                idlistcopy[j]=1
            for k in range(i,len(idlistcopy)):
                obj = fetchobj(l,idlistcopy[:k+1])
                if type(obj)==int:
                    addobj(l,idlistcopy[:k+1],val)  # type: ignore
                    return
def propright(l:list,index_list:list,val:int) :
    idlistcopy=index_list.copy()
    idlistcopy.append(0)
    for i in range(len(idlistcopy)-2,-1,-1):
        if idlistcopy[i]==0:
            idlistcopy[i]=1
            for j in range(i+1,len(idlistcopy)):
                idlistcopy[j]=0
            for k in range(i,len(idlistcopy)):
                obj = fetchobj(l,idlistcopy[:k+1])
                if type(obj)==int:
                    addobj(l,idlistcopy[:k+1],val)  # type: ignore
                    return
def zeroout(l:list,index_list:list):
    t=l
    for i in index_list[:-1]:
        t=t[i]
    t[index_list[-1]]=0
def explode(l,index_list:list):
    if len(index_list)!=4:
        for val in range(2):
            try:
                if type(l[val]) is list:
                    index_list.append(val)
                    v=explode(l[val],index_list)
                    if v==None:
                        index_list.pop()
                    else: 
                        return v
            except:
                continue
    else:
        if type(l) is list:
           return index_list
        else:
            return None        
    return None
def calmag(l:Any)->int:
    if type(l) is list:
        return 3*calmag(l[0])+2*calmag(l[1])
    else:
        return l

with open(PATH,'r') as f:
    for line in f:
        l.append(ast.literal_eval(line.replace('\n','')))
res=l[0]
cop=deepcopy(l)
for i in range(1,len(l)):
    res=add(res,l[i])
    res=parse(res)
    #print(res)
print(calmag(res))
magmax=0
for i in cop:
    for j in cop:
        if i==j:
            continue
        mag=calmag(parse(add(deepcopy(i),deepcopy(j))))
        magmax=mag if mag>magmax else magmax
print(magmax)
