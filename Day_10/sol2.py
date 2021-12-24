PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_10\\input.txt"
ls=[]
openers=set(['[','{','<','('])
points={
    ']':2,
    '}':3,
    '>':4,
    ')':1
}
match={
    '[':']',
    '{':'}',
    '<':'>',
    '(':')'
}
tot=[]
wrong=False
with open(PATH,'r') as f:
    for line in f:
        l=line.replace('\n','')
        ls=[]
        for c in l:
            if c in openers:
                ls.append(c)
            elif 0<ord(c)-ord(ls[-1])<3:
                ls.pop()
            else:
                wrong=True
                break
        if wrong:
            wrong=False
            continue
        sbt=0
        if ls!=[]:
            for c in reversed(ls):
                sbt*=5
                sbt+=points[match[c]]
            tot.append(sbt)
tot=sorted(tot)
print(tot[len(tot)//2])
print(len(tot))