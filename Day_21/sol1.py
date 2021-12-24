DICE=1
RC=0
def rollsum():
    global DICE,RC
    RC+=3
    Ds=DICE
    DICE = DICE+1 if DICE!=100 else 1
    Ds+=DICE
    DICE = DICE+1 if DICE!=100 else 1
    Ds+=DICE
    DICE = DICE+1 if DICE!=100 else 1
    return Ds
p1l=5
p2l=8
p1s=0
p2s=0

while p1s<1000 and p2s<1000:
    rol=rollsum()
    rol%=10
    p1l+=rol
    p1l=p1l if p1l<=10 else p1l-10
    p1s+=p1l
    if p1s>=1000:
        break
    rol=rollsum()
    rol%=10
    p2l+=rol
    p2l=p2l if p2l<=10 else p2l-10
    p2s+=p2l
print(RC*min(p1s,p2s))
print(RC)
print(p1s)
print(p2s)
