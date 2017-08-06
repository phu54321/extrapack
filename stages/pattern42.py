'''
TimeLock (Easy)
'''

from trggen import *
from .stages_commonlib import *


InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Heavy Missile', 'u9', P7),
], 12)


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'l1', P7),
    CreateUnit(1, 'Fast Missile', 'l3', P7),
    CreateUnit(1, 'Fast Missile', 'l5', P7),
    CreateUnit(1, 'Fast Missile', 'l7', P7),
    CreateUnit(1, 'Fast Missile', 'l9', P7),
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
])

Loop(24)


SelectCounter(1)

bodd = ['# # # # #']
beven = [' # # # # ']
bsp = ['         ']

time = 0
dt = 2

bb = beven
for i in range(9):
    BombPattern(time, 'Zerg Overlord', P7, bsp * i + bb + bsp * (8 - i))
    bb = beven if bb == bodd else bodd
    time += dt

time = 32
bb = bodd
for i in range(9):
    BombPattern(time, 'Zerg Overlord', P7, bsp * (8 - i) + bb + bsp * i)
    bb = beven if bb == bodd else bodd
    time += dt

Loop(65)
