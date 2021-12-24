PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_16\\input.txt"
pvt=0
def doop(pl,pt):
    if pt==0:
        return sum(pl)
    elif pt==1:
        res=1
        for v in pl:
            res*=v
        return res
    elif pt==2:
        return min(pl)
    elif pt==3:
        return max(pl)
    elif pt==5:
        if pl[0]>pl[1]:
            return 1
        else:
            return 0    
    elif pt==6:
        if pl[0]<pl[1]:
            return 1
        else:
            return 0
    elif pt==7:
        if pl[0]==pl[1]:
            return 1
        else:
            return 0
def parser(s,pos):
    while pos<len(s)-11:
        next=parsepacket(s,pos)
        pos+=next[0]
    print(next[1])
def parsepacket(s,pos):    
    global pvt
    pv=int(s[pos:pos+3],2)
    pt=int(s[pos+3:pos+6],2)
    pvt+=pv
    if pt==4:
        #literal
        num=''
        i=pos+6
        while True:
            n=s[i:i+5]
            b=int(n[0])
            rest=n[1:]
            i+=5
            num+=rest
            if b==0:
                break
        num=int(num,2)
        #i+=4-((i-pos)%4)
        print(f'numpacket: type - {pt}, version - {pv}, number - {num}')
        return (i,num)
    else:
        ltid=int(s[pos+6])
        if ltid==1:
            #number of sub packets
            nsp=int(s[pos+7:pos+18],2)
            i=pos+18
            print(f'opepacket: type - {pt}, version - {pv}, lengthtype - {ltid}, length - {nsp}')
            pl=[]
            for _ in range(nsp):
                i,j=parsepacket(s,i)
                pl.append(j)
            res=doop(pl,pt)
            return (i,res)
        else:
            #length in bits
            tli=int(s[pos+7:pos+22],2)
            i=pos+22
            print(f'opepacket: type - {pt}, version - {pv}, lengthtype - {ltid}, length - {tli}')
            pl=[]
            while i<pos+22+tli:
                i,j=parsepacket(s,i)
                pl.append(j)
            res=doop(pl,pt)
            return (i,res)

with open(PATH,'r') as f:
    s=f.readline()
bs=''
for c in s:
    tmp=bin(int(c,16))[2:]
    while len(tmp)<4:
        tmp='0'+tmp
    bs+=tmp
#print(bs)
print(parsepacket(bs,0)[1])
print(pvt)