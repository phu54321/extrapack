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
], 6)


# -------


SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Missile', 'l1', P7),
    CreateUnit(1, 'Missile', 'r2', P8),
    CreateUnit(1, 'Missile', 'l3', P7),
    CreateUnit(1, 'Missile', 'r4', P8),
    CreateUnit(1, 'Missile', 'l5', P7),
    CreateUnit(1, 'Missile', 'r6', P8),
    CreateUnit(1, 'Missile', 'l7', P7),
    CreateUnit(1, 'Missile', 'r8', P8),
    CreateUnit(1, 'Missile', 'l9', P7),
])
Loop(24)
