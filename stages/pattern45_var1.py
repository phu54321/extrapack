'''
대각선 미사일
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
])


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Diagonal Missile LR', 'ul1', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul3', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul5', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul7', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul9', P7),
])

Loop(18)
