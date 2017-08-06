# 위 & 오른쪽 반칸미사일

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Odd Fast Missile", "or1", P8),
    CreateUnit(1, "Fast Missile", "r2", P8),
    CreateUnit(1, "Odd Fast Missile", "or4", P8),
    CreateUnit(1, "Fast Missile", "r5", P8),
    CreateUnit(1, "Odd Fast Missile", "or7", P8),
    CreateUnit(1, "Fast Missile", "r8", P8),
    CreateUnit(1, "Odd Fast Missile", "or10", P8),
])

Shoot(24, [
    CreateUnit(1, "Odd Fast Missile", "or2", P8),
    CreateUnit(1, "Fast Missile", "r3", P8),
    CreateUnit(1, "Odd Fast Missile", "or5", P8),
    CreateUnit(1, "Fast Missile", "r6", P8),
    CreateUnit(1, "Odd Fast Missile", "or8", P8),
    CreateUnit(1, "Fast Missile", "r9", P8),
])

Shoot(48, [
    CreateUnit(1, "Fast Missile", "r1", P8),
    CreateUnit(1, "Odd Fast Missile", "or3", P8),
    CreateUnit(1, "Fast Missile", "r4", P8),
    CreateUnit(1, "Odd Fast Missile", "or6", P8),
    CreateUnit(1, "Fast Missile", "r7", P8),
    CreateUnit(1, "Odd Fast Missile", "or9", P8),
])


Shoot(0, [
    CreateUnit(1, "Odd Fast Missile", "ou1", P7),
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Odd Fast Missile", "ou4", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Odd Fast Missile", "ou7", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
    CreateUnit(1, "Odd Fast Missile", "ou10", P7),
])

Shoot(24, [
    CreateUnit(1, "Odd Fast Missile", "ou2", P7),
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Odd Fast Missile", "ou5", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Odd Fast Missile", "ou8", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
])

Shoot(48, [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Odd Fast Missile", "ou3", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Odd Fast Missile", "ou6", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
    CreateUnit(1, "Odd Fast Missile", "ou9", P7),
])


Loop(72)
