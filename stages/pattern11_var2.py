'''
파티퀸 격자
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

uo = [
    CreateUnit(1, "Fast Missile", "d1", P8),
    CreateUnit(1, "Missile", "d3", P8),
    CreateUnit(1, "Fast Missile", "d5", P8),
    CreateUnit(1, "Missile", "d7", P8),
    CreateUnit(1, "Fast Missile", "d9", P8),
]

ue = [
    CreateUnit(1, "Fast Missile", "d2", P8),
    CreateUnit(1, "Missile", "d4", P8),
    CreateUnit(1, "Fast Missile", "d6", P8),
    CreateUnit(1, "Missile", "d8", P8),
]

ro = [
    CreateUnit(1, "Fast Missile", "l1", P7),
    CreateUnit(1, "Missile", "l3", P7),
    CreateUnit(1, "Fast Missile", "l5", P7),
    CreateUnit(1, "Missile", "l7", P7),
    CreateUnit(1, "Fast Missile", "l9", P7),
]

re = [
    CreateUnit(1, "Fast Missile", "l2", P7),
    CreateUnit(1, "Missile", "l4", P7),
    CreateUnit(1, "Fast Missile", "l6", P7),
    CreateUnit(1, "Missile", "l8", P7),
]

dt = 12

Shoot(dt * 0, [uo, ro])
Shoot(dt * 1, [uo, ro])
Shoot(dt * 3, [uo, re])
Shoot(dt * 4, [uo, re])
Shoot(dt * 6, [ue, re])
Shoot(dt * 7, [ue, re])
Shoot(dt * 9, [ue, ro])
Shoot(dt * 10, [ue, ro])

Loop(dt * 12)
