'''
위아래 왔다갔다
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

####

rowtb = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1]
for i in range(len(rowtb)):
    Shoot(i * 4, [
        [
            CreateUnit(1, "Small Missile", "sl%d" % j, P7)
            for j in range(1, 19) if (j - 1) % 6 == rowtb[i]
        ],
    ])

Loop(4 * len(rowtb))
