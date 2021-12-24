forw=0
dept=0
with open('input.txt','r') as f:
    for line in f:
        s=line.split(' ')
        if s[0]=='forward':
            forw+=int(s[1])
        elif s[0]=='down':
            dept+=int(s[1])
        else:
            dept-=int(s[1])
print(forw*dept)
