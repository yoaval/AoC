ct=0
with open('input.txt','r') as f:
    first=int(f.readline())
    second=int(f.readline())
    third=int(f.readline())
    sum=first+second+third
    while True:
        try:
            new=int(f.readline())
        except:
            break
        if new>first:
            ct+=1
        sum+=(new-first)
        first=second
        second=third
        third=new
print(ct)