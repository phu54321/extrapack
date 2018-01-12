'''
사이드 반칸무빙
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
], delay=12)

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Odd Fast Missile", "ou1", P7),
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Odd Fast Missile", "ou4", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Odd Fast Missile", "ou7", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
    CreateUnit(1, "Odd Fast Missile", "ou10", P7),
])

Shoot(10, [
    CreateUnit(1, "Odd Fast Missile", "ou2", P7),
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Odd Fast Missile", "ou5", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Odd Fast Missile", "ou8", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
])

Shoot(20, [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Odd Fast Missile", "ou3", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Odd Fast Missile", "ou6", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
    CreateUnit(1, "Odd Fast Missile", "ou9", P7),
])

Loop(30)
