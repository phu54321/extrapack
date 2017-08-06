'''
7패턴 변형 - 사방에서 무한S자
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

time = 0
dt = 12

def shootf(i):
    return [
        CreateUnit(1, 'Fast Missile', 'u%d' % i, P7),
        CreateUnit(1, 'Fast Missile', 'l%d' % (10 - i), P7),
        CreateUnit(1, 'Fast Missile', 'd%d' % (10 - i), P8),
        CreateUnit(1, 'Fast Missile', 'r%d' % i, P8),
    ]

Shoot(time, shootf(1) + shootf(2))
time += dt
Shoot(time, shootf(3) + shootf(4))
time += dt
Shoot(time, shootf(5) + shootf(6))
time += dt
Shoot(time, shootf(7) + shootf(8))
time += dt
Shoot(time, shootf(9) + shootf(8))
time += dt
Shoot(time, shootf(7) + shootf(6))
time += dt
Shoot(time, shootf(5) + shootf(4))
time += dt
Shoot(time, shootf(3) + shootf(2))
time += dt
Loop(time)
