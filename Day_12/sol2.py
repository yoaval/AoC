import numpy as np
SZ=13
ls=[]
id=0
ar=np.zeros((SZ,SZ),np.int8)
dic={}
rdic={}
totp=0
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_12\\input.txt"
def routes(ar):
    global ls
    global id
    global dic
    global rdic
    global totp
    si=dic['start'][0]
    #ei=dic['end'][0]
    ls2=[]
    if ls==[] and totp==0:
        for i in range(id):
            if ar[si,i]==1:
                ls2.append([i])
    elif ls==[] and totp!=0:
        print(totp)
        return
    else:
        for r in ls:
            li=r[-1]
            if rdic[li][0]=='end':
                #print(r)
                totp+=1
                continue
            for i in range(id):
                if ar[li,i]==1 and rdic[i][0]!='start':
                    if rdic[i][1]==True:
                        tmp=r.copy()
                        tmp.append(i)
                        ls2.append(tmp)
                    else:
                        if r.count(i)==2:
                            continue
                        elif r.count(i)==1:
                            full=False
                            for v in r:
                                #bad patch, the better efficency option is to hold another bool per list indicating if it has already visted a cave twice
                                if r.count(v)==2 and rdic[v][1]==False:
                                    full=True
                                    break
                            if full==False:
                                tmp=r.copy()
                                tmp.append(i)
                                ls2.append(tmp)

                        else:
                            tmp=r.copy()
                            tmp.append(i)
                            ls2.append(tmp)
    ls=ls2.copy()
    routes(ar)
            
with open(PATH,'r') as f:
    for line in f:
        t=line.replace('\n','').split('-')
        for s in t:
            big=True
            if 'a'<=s[0]<='z':
                big = False
            if s not in dic:
                dic[s]=(id,big)
                rdic[id]=(s,big)
                id+=1
        ar[dic[t[0]][0],dic[t[1]][0]]=1
        ar[dic[t[1]][0],dic[t[0]][0]]=1

routes(ar)
print(ar[:id,:id])
print('-------')
print(dic)