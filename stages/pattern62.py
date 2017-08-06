'''
발키리 피하기 다른패턴
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
], 6)


# -------


SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Heavy Missile', 'l1', P7),
    CreateUnit(1, 'Heavy Missile', 'l6', P7),
])

Shoot(18, [
    CreateUnit(1, 'Heavy Missile', 'l2', P7),
    CreateUnit(1, 'Heavy Missile', 'l7', P7),
])

Shoot(36, [
    CreateUnit(1, 'Heavy Missile', 'l3', P7),
    CreateUnit(1, 'Heavy Missile', 'l8', P7),
])

Shoot(54, [
    CreateUnit(1, 'Heavy Missile', 'l4', P7),
    CreateUnit(1, 'Heavy Missile', 'l9', P7),
])

Shoot(72, [
    CreateUnit(1, 'Heavy Missile', 'l5', P7),
])

Loop(90)

# -------

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'u1', P7),
    CreateUnit(1, 'Fast Missile', 'u2', P7),
    CreateUnit(1, 'Fast Missile', 'u3', P7),
    CreateUnit(1, 'Fast Missile', 'u4', P7),
    CreateUnit(1, 'Fast Missile', 'u5', P7),
    CreateUnit(1, 'Fast Missile', 'u6', P7),
    CreateUnit(1, 'Fast Missile', 'u7', P7),
    CreateUnit(1, 'Fast Missile', 'u8', P7),
    CreateUnit(1, 'Fast Missile', 'u9', P7),
])

Loop(60)
