'''
파티퀸 격자
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

uo = [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
]

ue = [
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
]

ro = [
    CreateUnit(1, "Fast Missile", "r1", P8),
    CreateUnit(1, "Fast Missile", "r3", P8),
    CreateUnit(1, "Fast Missile", "r5", P8),
    CreateUnit(1, "Fast Missile", "r7", P8),
    CreateUnit(1, "Fast Missile", "r9", P8),
]

re = [
    CreateUnit(1, "Fast Missile", "r2", P8),
    CreateUnit(1, "Fast Missile", "r4", P8),
    CreateUnit(1, "Fast Missile", "r6", P8),
    CreateUnit(1, "Fast Missile", "r8", P8),
]


Shoot(0, [uo, ro])
Shoot(12, [uo, ro])
Shoot(24, [uo, re])
Shoot(36, [uo, re])
Shoot(48, [ue, re])
Shoot(60, [ue, re])
Shoot(72, [ue, ro])
Shoot(84, [ue, ro])

Loop(96)
