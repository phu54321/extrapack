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

Shoot(12, [
    CreateUnit(1, "Odd Fast Missile", "or2", P8),
    CreateUnit(1, "Fast Missile", "r3", P8),
    CreateUnit(1, "Odd Fast Missile", "or5", P8),
    CreateUnit(1, "Fast Missile", "r6", P8),
    CreateUnit(1, "Odd Fast Missile", "or8", P8),
    CreateUnit(1, "Fast Missile", "r9", P8),
])

Shoot(24, [
    CreateUnit(1, "Fast Missile", "r1", P8),
    CreateUnit(1, "Odd Fast Missile", "or3", P8),
    CreateUnit(1, "Fast Missile", "r4", P8),
    CreateUnit(1, "Odd Fast Missile", "or6", P8),
    CreateUnit(1, "Fast Missile", "r7", P8),
    CreateUnit(1, "Odd Fast Missile", "or9", P8),
])

Loop(36)
