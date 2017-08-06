'''
무궁화꽃
'''

from trggen import *
from .stages_commonlib import *


InitNormalMissileMove()


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Missile', 'd1', P8),
    CreateUnit(1, 'Missile', 'd3', P8),
    CreateUnit(1, 'Missile', 'd5', P8),
    CreateUnit(1, 'Missile', 'd7', P8),
    CreateUnit(1, 'Missile', 'd9', P8),
])

Shoot(24, [
    CreateUnit(1, 'Missile', 'd2', P8),
    CreateUnit(1, 'Missile', 'd4', P8),
    CreateUnit(1, 'Missile', 'd6', P8),
    CreateUnit(1, 'Missile', 'd8', P8),
])

Loop(48)


SelectCounter(1)

Shoot(0, [
    SetSwitch('LockDrone', Set)
])

Shoot(32, [
    SetSwitch('LockDrone', Clear)
])

Loop(60)
