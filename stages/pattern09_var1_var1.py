from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Fast Missile", "l1", P7),
    CreateUnit(1, "Fast Missile", "l3", P7),
    CreateUnit(1, "Fast Missile", "l5", P7),
    CreateUnit(1, "Fast Missile", "l7", P7),
    CreateUnit(1, "Fast Missile", "l9", P7),
])

Shoot(12, [
    CreateUnit(1, "Fast Missile", "l2", P7),
    CreateUnit(1, "Fast Missile", "l4", P7),
    CreateUnit(1, "Fast Missile", "l6", P7),
    CreateUnit(1, "Fast Missile", "l8", P7),
])

Loop(24)
