'''
Timelock 2
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Heavy Missile', 'u9', P7),
], 12)


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'u1', P7),
    CreateUnit(1, 'Fast Missile', 'u4', P7),
    CreateUnit(1, 'Fast Missile', 'u7', P7)
])

Shoot(18, [
    CreateUnit(1, 'Fast Missile', 'u2', P7),
    CreateUnit(1, 'Fast Missile', 'u5', P7),
    CreateUnit(1, 'Fast Missile', 'u8', P7)
])

Shoot(36, [
    CreateUnit(1, 'Fast Missile', 'u3', P7),
    CreateUnit(1, 'Fast Missile', 'u6', P7),
    CreateUnit(1, 'Fast Missile', 'u9', P7)
])

Loop(54)


####

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, 'Missile', 'r1', P8),
    CreateUnit(1, 'Missile', 'r4', P8),
    CreateUnit(1, 'Missile', 'r7', P8)
])

Shoot(24, [
    CreateUnit(1, 'Missile', 'r2', P8),
    CreateUnit(1, 'Missile', 'r5', P8),
    CreateUnit(1, 'Missile', 'r8', P8)
])

Shoot(48, [
    CreateUnit(1, 'Missile', 'r3', P8),
    CreateUnit(1, 'Missile', 'r6', P8),
    CreateUnit(1, 'Missile', 'r9', P8)
])

Loop(72)

####


SelectCounter(2)

Shoot(0, [
    SetSwitch('LockMissileP7', Set),
    SetSwitch('LockMissileP8', Clear),
])

Shoot(31, [
    SetSwitch('LockMissileP7', Clear),
    SetSwitch('LockMissileP8', Set),
])

Loop(62)
