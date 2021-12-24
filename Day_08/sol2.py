PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_8\\input.txt"
def l2d(fp):
    dic={}
    lens=set([2,3,4,7])
    for s in fp:
        if len(s)==2:
            dic[1]=s
        elif len(s)==3:
            dic[7]=s
        elif len(s)==4:
            dic[4]=s
        elif len(s)==7:
            dic[8]=s
    for s in fp:
        if len(s) not in lens:
            if len(s)==6:
                if s.intersection(dic[4])==dic[4]:
                    dic[9]=s
                elif s.intersection(dic[1])!=dic[1]:
                    dic[6]=s
                else:
                    dic[0]=s
            if len(s)==5:
                if len(s.intersection(dic[4]))==2:
                    dic[2]=s
                elif len(s.intersection(dic[4]))==3 and s.intersection(dic[1])==dic[1] :
                    dic[3]=s
                else:
                    dic[5]=s
    return dic

with open(PATH,'r') as f:
    tot=0
    for line in f:
        fp,sp=line.replace('\n','').split('|')
        fp=fp[:-1].split(' ')
        sp=sp[1:].split(' ')
        fp=[set(x) for x in fp]
        sp=[set(x) for x in sp]
        dic=l2d(fp)
        num=0
        mult=1000
        for s in sp:
            for key,value in dic.items():
                if s==value:
                    num+=mult*key
                    mult/=10
                    break
        tot+=num
print(tot)