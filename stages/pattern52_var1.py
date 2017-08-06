from trggen import *
from .stages_commonlib import *
import math

InitNormalMissileMove()


dt = 3
ivspeed = 11
SelectCounter(0)
for i in range(ivspeed * 9):
    row = math.floor(0.5 + i * i / ivspeed) % 9
    Shoot(i * dt, [
        CreateUnit(1, 'Heavy Missile', 'l%d' % (row + 1), P7)
    ])

Loop(dt * ivspeed * 9)


SelectCounter(1)

dt = 3
ivspeed = 7
SelectCounter(1)
for i in range(ivspeed * 9):
    row = math.floor(0.5 + i * i / ivspeed) % 9
    Shoot(i * dt, [
        CreateUnit(1, 'Heavy Missile', 'r%d' % (9 - row), P8)
    ])

Loop(dt * ivspeed * 9)
