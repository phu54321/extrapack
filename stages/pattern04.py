'''
오른쪽으로 몰아가기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
])

Shoot(8, [
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
])

Shoot(16, [
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
])

Loop(24)
