'''
러커폭탄 + 퀸
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Missile", "u2", P7),
    CreateUnit(1, "Missile", "u4", P7),
    CreateUnit(1, "Missile", "u6", P7),
    CreateUnit(1, "Missile", "u8", P7),
])

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Missile", "u1", P7),
    CreateUnit(1, "Missile", "u3", P7),
    CreateUnit(1, "Missile", "u5", P7),
    CreateUnit(1, "Missile", "u7", P7),
    CreateUnit(1, "Missile", "u9", P7),
])

Shoot(12, [
    CreateUnit(1, "Missile", "u2", P7),
    CreateUnit(1, "Missile", "u4", P7),
    CreateUnit(1, "Missile", "u6", P7),
    CreateUnit(1, "Missile", "u8", P7),
])

Loop(24)


SelectCounter(1)

BombPattern(0, 'Flare', P8, [
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
])


BombPattern(36, 'Flare', P8, [
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
    ' # # # # ',
])

Loop(72)
