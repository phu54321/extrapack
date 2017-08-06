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
    CreateUnit(1, "Odd Fast Missile", "ol1", P7),
    CreateUnit(1, "Odd Fast Missile", "ol5", P7),
    CreateUnit(1, "Odd Fast Missile", "ol9", P7),
])

Shoot(6, [
    CreateUnit(1, "Odd Fast Missile", "ol2", P7),
    CreateUnit(1, "Odd Fast Missile", "ol6", P7),
    CreateUnit(1, "Odd Fast Missile", "ol10", P7),
])

Shoot(12, [
    CreateUnit(1, "Odd Fast Missile", "ol3", P7),
    CreateUnit(1, "Odd Fast Missile", "ol7", P7),
])

Shoot(18, [
    CreateUnit(1, "Odd Fast Missile", "ol4", P7),
    CreateUnit(1, "Odd Fast Missile", "ol8", P7),
])

Loop(23)


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
