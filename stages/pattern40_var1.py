'''
무궁화꽃 (역방향)
'''

from trggen import *
from .stages_commonlib import *


InitNormalMissileMove()


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Missile', 'u1', P7),
    CreateUnit(1, 'Missile', 'u3', P7),
    CreateUnit(1, 'Missile', 'u5', P7),
    CreateUnit(1, 'Missile', 'u7', P7),
    CreateUnit(1, 'Missile', 'u9', P7),
])

Shoot(27, [
    CreateUnit(1, 'Missile', 'u2', P7),
    CreateUnit(1, 'Missile', 'u4', P7),
    CreateUnit(1, 'Missile', 'u6', P7),
    CreateUnit(1, 'Missile', 'u8', P7),
])

Loop(54)


SelectCounter(1)

Shoot(0, [
    SetSwitch('LockDrone', Set)
])

Shoot(36, [
    SetSwitch('LockDrone', Clear)
])

Loop(72)
