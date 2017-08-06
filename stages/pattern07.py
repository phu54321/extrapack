'''
상하좌우 계단
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

shootf = lambda i: [
    CreateUnit(1, 'Fast Missile', 'u%d' % i, P7),
    CreateUnit(1, 'Fast Missile', 'l%d' % (10-i), P7),
    CreateUnit(1, 'Fast Missile', 'd%d' % (10-i), P8),
    CreateUnit(1, 'Fast Missile', 'r%d' % i, P8),
]

Shoot(0, shootf(1))
Shoot(9, shootf(2))
Shoot(18, shootf(3))
Shoot(27, shootf(4))
Shoot(36, shootf(5))
Shoot(45, shootf(6))
Shoot(54, shootf(7))
Shoot(63, shootf(8))
Shoot(72, shootf(9))

Loop(81)
