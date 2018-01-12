'''
상하좌우 겹치기 - 가디언 버젼
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Small Slow Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u9', P7),
], 12)

#######

u = 'Big Slow Missile'


def uact(i):
    if 1 <= i <= 9:
        if i % 2 == 0:
            return [
                CreateUnit(1, u, 'u%d' % i, P7),
                Order(u, P7, 'u%d' % i, Move, 'd%d' % i)
            ]
        else:
            return [
                CreateUnit(1, u, 'u%d' % i, P8),
                Order(u, P8, 'u%d' % i, Move, 'd%d' % i)
            ]
    else:
        return []


def ract(i):
    if 1 <= i <= 9:
        if i % 2 == 0:
            return [
                CreateUnit(1, u, 'r%d' % i, P8),
                Order(u, P8, 'r%d' % i, Move, 'l%d' % i)
            ]
        else:
            return [
                CreateUnit(1, u, 'r%d' % i, P7),
                Order(u, P7, 'r%d' % i, Move, 'l%d' % i)
            ]
    else:
        return []


dt = 15

SelectCounter(0)


#######


rowtb = [
    4, 2, 3, 1
]

for i in range(len(rowtb)):
    Shoot(i * dt, [
        uact(rowtb[i] - 1),
        uact(rowtb[i] + 3),
        uact(rowtb[i] + 7),
        uact(rowtb[i] + 11),
    ])


#######


rowtb = [
    2, 3, 1, 4
]

for i in range(len(rowtb)):
    Shoot(i * dt, [
        ract(rowtb[i] - 1),
        ract(rowtb[i] + 3),
        ract(rowtb[i] + 7),
        ract(rowtb[i] + 11),
    ])


#######


Loop(dt * len(rowtb))

AlwaysShoot([
    KillUnitAt(All, u, 'd', AllPlayers),
    KillUnitAt(All, u, 'l', AllPlayers)
])
