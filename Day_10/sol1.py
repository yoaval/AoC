PATH="C:\\Users\\yoav\\Documents\\AoC\\Day_10\\input.txt"
ls=[]
openers=set(['[','{','<','('])
points={
    ']':57,
    '}':1197,
    '>':25137,
    ')':3
}
tot=0
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
                tot+=points[c]
                break
print(tot)