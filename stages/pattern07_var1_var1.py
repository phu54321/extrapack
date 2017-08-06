'''
위에서 2개씩 날라오기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

time = 0
dt = 15


def shootf(i):
    return [
        CreateUnit(1, 'Fast Missile', 'u%d' % i, P7),
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
