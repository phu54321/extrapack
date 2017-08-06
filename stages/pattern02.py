'''
44벽 + 거미줄. 원클가능.
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '# # # # #',
    '         ',
    '# # # # #',
    '         ',
    '# # # # #',
    '         ',
    '# # # # #',
    '         ',
    '# # # # #',
])


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Missile", "l2", P7),
    CreateUnit(1, "Missile", "r4", P8),
    CreateUnit(1, "Missile", "l6", P7),
    CreateUnit(1, "Missile", "r8", P8),
    CreateUnit(1, "Missile", "d2", P8),
    CreateUnit(1, "Missile", "u4", P7),
    CreateUnit(1, "Missile", "d6", P8),
    CreateUnit(1, "Missile", "u8", P7),
])

Shoot(23, [
    SetDeaths(P8, SetTo, -1, "@PatternSubCounter1"),
])
