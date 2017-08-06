'''
간단한 대각무빙
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '#######  ',
    '######   ',
    '#####   #',
    '####   ##',
    '###   ###',
    '##   ####',
    '#   #####',
    '   ######',
    '  #######',
])

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Diagonal Missile RL", "ur4", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur6", P7),
])

Shoot(12, [
    CreateUnit(1, "Diagonal Missile RL", "ur5", P7),
])

Loop(24)
