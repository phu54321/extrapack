'''
사이드 디파간격 막쏴
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Heavy Missile", "u1", P7),
    CreateUnit(1, "Heavy Missile", "u2", P7),
    CreateUnit(1, "Heavy Missile", "u3", P7),
    CreateUnit(1, "Heavy Missile", "u4", P7),
    CreateUnit(1, "Heavy Missile", "u5", P7),
    CreateUnit(1, "Heavy Missile", "u6", P7),
    CreateUnit(1, "Heavy Missile", "u7", P7),
    CreateUnit(1, "Heavy Missile", "u8", P7),
    CreateUnit(1, "Heavy Missile", "u9", P7),
])

#######

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Heavy Missile", "l1", P7),
    CreateUnit(1, "Heavy Missile", "l5", P7),
    CreateUnit(1, "Heavy Missile", "l9", P7),
])

Shoot(8, [
    CreateUnit(1, "Heavy Missile", "l2", P7),
    CreateUnit(1, "Heavy Missile", "l6", P7),
])

Shoot(16, [
    CreateUnit(1, "Heavy Missile", "l3", P7),
    CreateUnit(1, "Heavy Missile", "l7", P7),
])

Shoot(24, [
    CreateUnit(1, "Heavy Missile", "l4", P7),
    CreateUnit(1, "Heavy Missile", "l8", P7),
])

Loop(32)


#######


SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Small Slow Missile", "d1", P8),
    CreateUnit(1, "Small Slow Missile", "d2", P8),
    CreateUnit(1, "Small Slow Missile", "d3", P8),
    CreateUnit(1, "Small Slow Missile", "d4", P8),
    CreateUnit(1, "Small Slow Missile", "d5", P8),
    CreateUnit(1, "Small Slow Missile", "d6", P8),
    CreateUnit(1, "Small Slow Missile", "d7", P8),
    CreateUnit(1, "Small Slow Missile", "d8", P8),
    CreateUnit(1, "Small Slow Missile", "d9", P8),
])

Loop(60)
