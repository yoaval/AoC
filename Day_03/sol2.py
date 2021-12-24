def builds(ar):
    tot=0
    for i in range(len(ar)):
        num=int(ar[i])<<(len(ar)-i-1)
        tot+=num
    return tot
def onecount(ar):
    arcount=[0]*NUMLEN
    for line in ar:
        loc=0
        for ch in line:
            if ch=='1':
                arcount[loc]+=1
            loc+=1
    return arcount
def filter_o(ar,oncnt,count,co2=False):
    newar=[]
    if oncnt[count]>=len(ar)/2:
        ft='1'
    else:
        ft='0'
    if co2:
        if ft=='1':
            ft='0'
        else:
            ft='1'
    for val in ar:
        if val[count]==ft:
            newar.append(val)
    return newar


CT=1000
NUMLEN=12
# CT=12
# NUMLEN=5
all=[]
PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_3\\input.txt"
with open(PATH,'r') as f:
    for line in f:
        all.append(line.replace('\n',''))

newarr=all.copy()
i=0
while len(newarr)>1:
    onecnt=onecount(newarr)
    newarr=filter_o(newarr,onecnt,i)
    i+=1
o2=builds(newarr[0])

newarr=all.copy()
i=0
while len(newarr)>1:
    onecnt=onecount(newarr)
    newarr=filter_o(newarr,onecnt,i,co2=True)
    i+=1
co2=builds(newarr[0])
print(o2*co2)
