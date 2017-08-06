'''
우측으로 몰기 (카피팩 변형)
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '# # # # #',
    '         ',
    ' # # # # ',
    '         ',
    '# # # # #',
    '         ',
    ' # # # # ',
    '         ',
    '# # # # #',
])


#######

SelectCounter(0)

BombPattern(0, 'Protoss Archon', P8, [
    '@#@#@#@#@',
    '         ',
    ' @ @ @ @ ',
    '         ',
    '@#@#@#@#@',
    '         ',
    ' @ @ @ @ ',
    '         ',
    '@#@#@#@#@',
])

BombPattern(16, 'Protoss Archon', P8, [
    '@ @ @ @ @',
    '         ',
    '#@#@#@#@#',
    '         ',
    '@ @ @ @ @',
    '         ',
    '#@#@#@#@#',
    '         ',
    '@ @ @ @ @',
])


Loop(32)

#######

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Missile", "l2", P7),
    CreateUnit(1, "Missile", "l4", P7),
    CreateUnit(1, "Missile", "l6", P7),
    CreateUnit(1, "Missile", "l8", P7),
])

Loop(18)
