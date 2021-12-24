PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_14\\input.txt"
dic={}
counts={}
st=''
def step():
    global dic,counts
    tmp={}
    for key in counts.keys():
        if counts[key]==0:
            continue
        else:
            for val in dic[key]:
                try:
                    tmp[val]+=counts[key]
                except:
                    tmp[val]=counts[key]
    counts=tmp.copy()
def countl():
    global counts,st
    ct={}
    for c in st:
        ct[c]=0
    ct['H']=0
    for val in counts.keys():
        for c in val:
            ct[c]+=counts[val]
    ct[st[0]]+=1
    ct[st[len(st)-1]]+=1
    for key in ct.keys():
        ct[key]/=2
    return ct
            

with open(PATH,'r') as f:
    st=f.readline().replace('\n','')
    for line in f:
        tmp=line.replace('\n','').split('->')
        dic[tmp[0]]=[tmp[0][0]+tmp[1],tmp[1]+tmp[0][1]]
for key in dic.keys():
    counts[key]=0
for i in range(len(st)-1):
    counts[st[i:i+2]]+=1
for _ in range(40):
    step()
ct=countl()
vals=ct.values()
print(max(vals)-min(vals))

        