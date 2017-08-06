'''
좌우로 왔다갔다
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()


#######


def upact(i):
    if 1 <= i <= 18:
        return CreateUnit(1, 'Small Missile', 'su%d' % i, P7)
    else:
        return []


SelectCounter(0)
rowtb = [0, 1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3, -4, -3, -2, -1]
for i in range(len(rowtb)):
    Shoot(i * 3, [
        upact(rowtb[i] - 3),
        upact(rowtb[i] + 2),
        upact(rowtb[i] + 7),
        upact(rowtb[i] + 12),
        upact(rowtb[i] + 17),
        upact(rowtb[i] + 22),
    ])
Loop(3 * len(rowtb))


#######
'''
SelectCounter(1)
Shoot(0, [
    CreateUnit(1, 'Small Slow Heavy Missile', 'd1', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd2', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd3', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd4', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd5', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd6', P8),
    CreateUnit(1, 'Small Slow Heavy Missile', 'd7', P8),
])

Loop(48)
'''
