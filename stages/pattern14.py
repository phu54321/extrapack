'''
반칸 퀸
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Small Missile", "su1", P7),
    CreateUnit(1, "Small Missile", "su3", P7),
    CreateUnit(1, "Small Missile", "su5", P7),
    CreateUnit(1, "Small Missile", "su7", P7),
    CreateUnit(1, "Small Missile", "su9", P7),
    CreateUnit(1, "Small Missile", "su11", P7),
    CreateUnit(1, "Small Missile", "su13", P7),
    CreateUnit(1, "Small Missile", "su15", P7),
    CreateUnit(1, "Small Missile", "su17", P7),
])

Shoot(12, [
    CreateUnit(1, "Small Missile", "su2", P7),
    CreateUnit(1, "Small Missile", "su4", P7),
    CreateUnit(1, "Small Missile", "su6", P7),
    CreateUnit(1, "Small Missile", "su8", P7),
    CreateUnit(1, "Small Missile", "su10", P7),
    CreateUnit(1, "Small Missile", "su12", P7),
    CreateUnit(1, "Small Missile", "su14", P7),
    CreateUnit(1, "Small Missile", "su16", P7),
    CreateUnit(1, "Small Missile", "su18", P7),
])

Loop(24)
