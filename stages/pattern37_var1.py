'''
상하좌우 겹치기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

#######

su = 'Small Missile'
uact = lambda i: CreateUnit(1, su, 'su%d' % i, P7) if 1 <= i <= 18 else []
ract = lambda i: CreateUnit(1, su, 'sr%d' % i, P8) if 1 <= i <= 18 else []


dt = 6

SelectCounter(0)


#######


rowtb = [
    0, 1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 1,
    0, -1, -2, -3, -4, -5, -5, -5, -4, -3, -2, -1
]

for i in range(len(rowtb)):
    Shoot(i * dt, [
        uact(rowtb[i] - 2),
        uact(rowtb[i] + 5),
        uact(rowtb[i] + 12),
        uact(rowtb[i] + 19),
    ])


#######


rowtb = [
    -5, -4, -3, -2, -1, 0, 1, 2, 3, 4,
    5, 5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -5
]

for i in range(len(rowtb)):
    Shoot(i * dt, [
        ract(rowtb[i] - 2),
        ract(rowtb[i] + 5),
        ract(rowtb[i] + 12),
        ract(rowtb[i] + 19),
    ])


#######


Loop(dt * len(rowtb))
