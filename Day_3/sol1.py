def builds(ar):
    tot=0
    for i in range(len(ar)):
        num=ar[i]<<(len(ar)-i-1)
        tot+=num
    return tot
print(builds([1,1,1]))
gamma= [None]*12
epsilon = [None]*12
CT=1000
onecount=[0]*12

with open('input.txt','r') as f:
    for line in f:
        loc=0
        for ch in line:
            if ch=='1':
                onecount[loc]+=1
            loc+=1
print(onecount)
loc=0
for i in onecount:
    if i>500:
        gamma[loc]=1
        epsilon[loc]=0
    else: 
        gamma[loc]=0
        epsilon[loc]=1
    loc+=1
print(gamma)
print(builds(gamma)*builds(epsilon))
