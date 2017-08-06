from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
tm = 0

SelectCounter(0)
for j in range(8, -1, -1):
    Shoot(6 * tm, [
        CreateUnit(1, 'Heavy Missile', 'l%d' % (j + 1), P7),
        CreateUnit(1, 'Heavy Missile', 'r%d' % (9 - j), P8),
    ])
    tm += 1

for j in range(9):
    Shoot(6 * tm, [
        CreateUnit(1, 'Heavy Missile', 'u%d' % (j + 1), P7),
        CreateUnit(1, 'Heavy Missile', 'd%d' % (9 - j), P8),
    ])
    tm += 1

Loop(6 * tm)
