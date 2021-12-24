from __future__ import annotations
from typing import List


class cube:
    def __init__(self, x1, x2, y1, y2, z1, z2, state=True) -> None:
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)
        self.z1 = min(z1, z2)
        self.z2 = max(z1, z2)
        self.state = state
        self.vol = ((x2+1-x1)*(y2+1-y1)*(z2+1-z1))
    def intersection(self, c2: cube) -> cube:
        inter = False
        if (self.x2 >= c2.x1):
            if (self.x1 <= c2.x2):
                if (self.y2 >= c2.y1):
                    if (self.y1 <= c2.y2):
                        if (self.z2 >= c2.z1):
                            if (self.z1 <= c2.z2):
                                inter = True
        if inter == False:
            return None
        else:
            nc = cube(max(c2.x1, self.x1), min(c2.x2, self.x2), max(c2.y1, self.y1), min(c2.y2, self.y2), max(c2.z1, self.z1), min(c2.z2, self.z2))
            if self.state == True and c2.state == True:
                inter = False
                nc.state = inter
                return nc
            elif self.state == True and c2.state == False:
                inter = True
                nc.state = inter
                return nc
            elif self.state == False and c2.state == True:
                inter = False
                nc.state = inter
                return nc
            elif self.state == False and c2.state == False:
                inter = True
                nc.state = inter
                return nc
    def volume(self):
        return self.vol if self.state==True else -self.vol

PATH = "C:\\Users\\yoav\\Documents\\AoC\\Day_22\\input.txt"
instructions: list[cube] = []
with open(PATH, 'r') as f:
    for line in f:
        # on x=-27..27,y=-41..4,z=-9..38
        l = line.strip('\n')
        state = True if l[1] == 'n' else False
        # x=-27..27,y=-41..4,z=-9..38
        # -27..27,-41..4,-9..38
        x1, x2, y1, y2, z1, z2 = map(int,l.split(' ')[1].replace('x=', '').replace(
            'y=', '').replace('z=', '').replace('..', ',').split(','))
        instructions.append(cube(x1, x2, y1, y2, z1, z2, state))
currcubes: list[cube] = []
for ins in instructions:
    l = len(currcubes)
    if ins.state == True:
        currcubes.append(ins)
    for i in range(l):
        c2 = ins.intersection(currcubes[i])
        if c2 is not None:
            currcubes.append(c2)
tot=0
for c in currcubes:
    tot+=c.volume()
print(tot)

