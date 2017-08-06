'''
TimeLock (Easy)
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
    CreateUnit(1, 'Missile', 'l1', P7),
    CreateUnit(1, 'Missile', 'l3', P7),
    CreateUnit(1, 'Missile', 'l5', P7),
    CreateUnit(1, 'Missile', 'l7', P7),
    CreateUnit(1, 'Missile', 'l9', P7),

    CreateUnit(1, 'Missile', 'r2', P8),
    CreateUnit(1, 'Missile', 'r4', P8),
    CreateUnit(1, 'Missile', 'r6', P8),
    CreateUnit(1, 'Missile', 'r8', P8),
])

Shoot(30, [
    CreateUnit(1, 'Missile', 'u2', P7),
    CreateUnit(1, 'Missile', 'u4', P7),
    CreateUnit(1, 'Missile', 'u6', P7),
    CreateUnit(1, 'Missile', 'u8', P7),

    CreateUnit(1, 'Missile', 'd1', P8),
    CreateUnit(1, 'Missile', 'd3', P8),
    CreateUnit(1, 'Missile', 'd5', P8),
    CreateUnit(1, 'Missile', 'd7', P8),
    CreateUnit(1, 'Missile', 'd9', P8),
])

Loop(60)


SelectCounter(1)

Shoot(0, [
    SetSwitch('LockMissileP7', Set),
    SetSwitch('LockMissileP8', Clear),
])

Shoot(42, [
    SetSwitch('LockMissileP8', Set),
    SetSwitch('LockMissileP7', Clear),
])

Loop(84)
