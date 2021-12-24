ct=0
with open('input.txt','r') as f:
    first=int(f.readline())
    while True:
        try:
            second=int(f.readline())
        except:
            break
        if second>first:
            ct+=1
        first=second
print(ct)