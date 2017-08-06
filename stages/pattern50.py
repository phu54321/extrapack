from trggen import *
from .stages_commonlib import *


def sact(l):
    return [
        CreateUnit(1, 'Small Slow Heavy Missile', 'u%d' % i, P7)
        for i in l
    ]

InitNormalMissileMove([
    sact([1, 2, 3, 4, 5, 6, 7, 8, 9])
], 12)


# 가디언
SelectCounter(0)
Shoot(0 * 30, sact([1, 2, 3, 4, 6, 7, 8, 9]))
Shoot(1 * 30, sact([1, 2, 3, 5, 6, 7, 8, 9]))
Shoot(2 * 30, sact([1, 2, 4, 5, 6, 7, 8, 9]))
Shoot(3 * 30, sact([1, 2, 3, 5, 6, 7, 8, 9]))
Shoot(4 * 30, sact([1, 2, 3, 4, 6, 7, 8, 9]))
Shoot(5 * 30, sact([1, 2, 3, 4, 5, 7, 8, 9]))
Shoot(6 * 30, sact([1, 2, 3, 4, 5, 6, 8, 9]))
Shoot(7 * 30, sact([1, 2, 3, 4, 5, 7, 8, 9]))
Loop(8 * 30)

# 세로미사일
SelectCounter(1)
Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'l1', P7),
    CreateUnit(1, 'Fast Missile', 'l3', P7),
    CreateUnit(1, 'Fast Missile', 'l5', P7),
    CreateUnit(1, 'Fast Missile', 'l7', P7),
    CreateUnit(1, 'Fast Missile', 'l9', P7),
])

Shoot(17, [
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
])

Loop(34)
