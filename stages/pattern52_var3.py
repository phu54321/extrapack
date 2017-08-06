from trggen import *
from .stages_commonlib import *
import math

InitNormalMissileMove()

SelectCounter(0)

dt = 4
ivspeed = 10

for i in range(ivspeed * 9):
    row = math.floor(0.5 + i * i / ivspeed) % 9
    Shoot(i * dt, [
        CreateUnit(1, 'Fast Missile', 'l%d' % (row + 1), P7)
    ])

Loop(dt * ivspeed * 9)
