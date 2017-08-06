from trggen import *
from .stages_commonlib import *


def bitsum(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + bitsum(n >> 1)


InitNormalMissileMove()

SelectCounter(0)

dt = 3
t = 0

for i in range(72):
    position = 2 * i % 9 + 1
    missileType = ['Heavy Missile', 'Missile'][bitsum(i) & 1]
    Shoot(t, CreateUnit(1, missileType, 'u%d' % position, P7))
    t += dt

Loop(t)
