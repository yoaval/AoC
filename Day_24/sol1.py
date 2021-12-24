import z3
from z3.z3 import solve
PATH = "C:\\Users\\yoav\\Documents\\AoC\\Day_24\\input.txt"
ins = []
with open(PATH, 'r') as f:
    for line in f:
        ins.append(line.replace('\n', '').split(' '))
s = z3.Optimize()
digits = [z3.BitVec(f'd_{i}', 64) for i in range(14)]
for d in digits:
    s.add(d <= 9)
    s.add(d >= 1)
reg = {
    'x': z3.BitVecVal(0, 64),
    'y': z3.BitVecVal(0, 64),
    'z': z3.BitVecVal(0, 64),
    'w': z3.BitVecVal(0, 64),
}
ct = 0
for i, ex in enumerate(ins):
    if ex[0] == 'inp':
        reg[ex[1]] = digits[ct]
        ct += 1
        continue
    op1 = reg[ex[1]]
    op2 = reg[ex[2]] if ex[2] in ['x', 'y', 'z', 'w'] else int(ex[2])
    if ex[0] == 'add':
        reg[ex[1]] = op1+op2
    elif ex[0] == 'mul':
        reg[ex[1]] = op1*op2
    elif ex[0] == 'div':
        reg[ex[1]] = op1/op2
    elif ex[0] == 'mod':
        reg[ex[1]] = op1 % op2
    elif ex[0] == 'eql':
        reg[ex[1]] = z3.If(op1 == op2, z3.BitVecVal(
            1, 64), z3.BitVecVal(0, 64))
s.add(reg['z'] == 0)
s.push()
s.maximize(sum((10 ** i) * d for i, d in enumerate(digits[::-1])))
print(s.check())
m = s.model()
print(''.join([str(m[d]) for d in digits]))
s.pop()
s.push()
s.minimize(sum((10 ** i) * d for i, d in enumerate(digits[::-1])))
print(s.check())
m = s.model()
print(''.join([str(m[d]) for d in digits]))
s.pop()

