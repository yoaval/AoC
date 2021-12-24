import numpy as np
WIN=21
dic={}
p1l=5
p2l=8
def caching(p1l,p2l,p1s,p2s,turn):
    global dic
    if (p1l,p2l,p1s,p2s,turn) in dic:
        return dic[(p1l,p2l,p1s,p2s,turn)]
    elif p1s>=WIN:
        tmp=np.zeros(2)
        tmp[0]=1
        dic[(p1l,p2l,p1s,p2s,turn)]=tmp
        return dic[(p1l,p2l,p1s,p2s,turn)]
    elif p2s>=WIN:
        tmp=np.zeros(2)
        tmp[1]=1
        dic[(p1l,p2l,p1s,p2s,turn)]=tmp
        return dic[(p1l,p2l,p1s,p2s,turn)]
    elif turn:
        newpls=[0,0,0,0,0,0,0]
        for i in range(len(newpls)):
            newpls[i]=p1l+3+i if p1l<=10-(3+i) else p1l-10+(3+i)
        newpps=[0,0,0,0,0,0,0]
        for i in range(len(newpps)):
            newpps[i]=p1s+newpls[i]
        dic[(p1l,p2l,p1s,p2s,turn)]=1*caching(newpls[0],p2l,newpps[0],p2s,False) + 3*caching(newpls[1],p2l,newpps[1],p2s,False) +6*caching(newpls[2],p2l,newpps[2],p2s,False) + 7*caching(newpls[3],p2l,newpps[3],p2s,False) + 6*caching(newpls[4],p2l,newpps[4],p2s,False) +3*caching(newpls[5],p2l,newpps[5],p2s,False) + 1*caching(newpls[6],p2l,newpps[6],p2s,False)
        return dic[(p1l,p2l,p1s,p2s,turn)]
    else:
        #not turn
        newpls=[0,0,0,0,0,0,0]
        for i in range(len(newpls)):
            newpls[i]=p2l+3+i if p2l<=10-(3+i) else p2l-10+(3+i)
        newpps=[0,0,0,0,0,0,0]
        for i in range(len(newpps)):
            newpps[i]=p2s+newpls[i]
        dic[(p1l,p2l,p1s,p2s,turn)]=1*caching(p1l,newpls[0],p1s,newpps[0],True) + 3*caching(p1l,newpls[1],p1s,newpps[1],True) +6*caching(p1l,newpls[2],p1s,newpps[2],True) + 7*caching(p1l,newpls[3],p1s,newpps[3],True) + 6*caching(p1l,newpls[4],p1s,newpps[4],True) +3*caching(p1l,newpls[5],p1s,newpps[5],True) + 1*caching(p1l,newpls[6],p1s,newpps[6],True)
        return dic[(p1l,p2l,p1s,p2s,turn)]
res=caching(p1l,p2l,0,0,True)
print(f'{res[0]:.0f},{res[1]:.0f}')


