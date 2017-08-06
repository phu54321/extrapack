'''
미로 + 반칸미사일 2
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    ' ########',
    ' #       ',
    ' # ##### ',
    ' # #   # ',
    ' # # # # ',
    ' #   # # ',
    ' ##### # ',
    '       # ',
    '######## ',
], unit='Flare', player=P7)

looptm = 23
dt = 6
delta = 15

SelectCounter(0)

Shoot((delta + dt * 0) % looptm, CreateUnit(1, "Odd Fast Missile", "ou1", P7))
Shoot((delta + dt * 1) % looptm, CreateUnit(1, "Odd Fast Missile", "od2", P8))
Shoot((delta + dt * 2) % looptm, CreateUnit(1, "Odd Fast Missile", "ou3", P7))
Shoot((delta + dt * 3) % looptm, CreateUnit(1, "Odd Fast Missile", "ou5", P7))
Shoot((delta + dt * 4) % looptm, CreateUnit(1, "Odd Fast Missile", "od4", P8))
Shoot((delta + dt * 5) % looptm, CreateUnit(1, "Odd Fast Missile", "od6", P8))
Shoot((delta + dt * 6) % looptm, CreateUnit(1, "Odd Fast Missile", "ou7", P7))
Shoot((delta + dt * 7) % looptm, CreateUnit(1, "Odd Fast Missile", "ou9", P7))
Shoot((delta + dt * 8) % looptm, CreateUnit(1, "Odd Fast Missile", "od8", P8))
Shoot((delta + dt * 9) % looptm, CreateUnit(1, "Odd Fast Missile", "od10", P8))

Loop(looptm)
