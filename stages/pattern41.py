'''
이상한 세로미사일
'''

from trggen import *
from .stages_commonlib import *


def cm(s, d):
    sloc = 'u%d' % s
    dloc = 'd%d' % d
    return [
        CreateUnit(1, 'Fast Missile', sloc, P7),
        Order('Fast Missile', P7, sloc, Move, dloc),
    ]


InitWalls([
    '#       #',
    '#       #',
    '#       #',
    '#       #',
    '#       #',
    '#       #',
    '#       #',
    '#       #',
    '#       #',
], additionalactions=[
    SetSwitch("NormalMissileMove", Clear)
])
SelectCounter(0)
AlwaysShoot(KillUnitAt(All, 'Fast Missile', 'd', P7))
Shoot(0, [cm(1, 2), cm(3, 4), cm(5, 6), cm(7, 8)])
Shoot(9, [cm(2, 3), cm(4, 5), cm(6, 7), cm(8, 9)])
Shoot(18, [cm(3, 2), cm(5, 4), cm(7, 6), cm(9, 8)])
Shoot(27, [cm(2, 1), cm(4, 3), cm(6, 5), cm(8, 7)])
Loop(36)
