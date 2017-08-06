'''
폭탄 + 퀸
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

# Bombing

SelectCounter(0)
o = '#########'
x = '         '

BombPattern(0, 'Protoss Dark Archon', P8, [x, x, o, o, x, x, o, o, x])
BombPattern(24, 'Protoss Dark Archon', P8, [x, o, o, x, x, o, o, x, x])
BombPattern(48, 'Protoss Dark Archon', P8, [o, o, x, x, o, o, x, x, o])
BombPattern(72, 'Protoss Dark Archon', P8, [o, x, x, o, o, x, x, o, o])
Loop(96)


# Missile

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Fast Missile", 'u1', P7),
    CreateUnit(1, "Fast Missile", 'u3', P7),
    CreateUnit(1, "Fast Missile", 'u5', P7),
    CreateUnit(1, "Fast Missile", 'u7', P7),
    CreateUnit(1, "Fast Missile", 'u9', P7),
])

Shoot(10, [
    CreateUnit(1, "Fast Missile", 'u2', P7),
    CreateUnit(1, "Fast Missile", 'u4', P7),
    CreateUnit(1, "Fast Missile", 'u6', P7),
    CreateUnit(1, "Fast Missile", 'u8', P7),
])

Loop(20)
