'''
미로 + 반칸미사일
'''

from trggen import *
from .stages_commonlib import *


InitWalls([
    '######## ',
    '       # ',
    ' ##### # ',
    ' #   # # ',
    ' # # # # ',
    ' # #   # ',
    ' # ##### ',
    ' #       ',
    ' ########',
], 'White Flare')

SelectCounter(0)

###########################

Shoot(0, [
    CreateUnit(1, "Odd Fast Missile", "ou1", P7),
    CreateUnit(1, "Odd Fast Missile", "ou3", P7),
    CreateUnit(1, "Odd Fast Missile", "ou5", P7),
    CreateUnit(1, "Odd Fast Missile", "ou7", P7),
    CreateUnit(1, "Odd Fast Missile", "ou9", P7),

    CreateUnit(1, "Odd Fast Missile", "od2", P8),
    CreateUnit(1, "Odd Fast Missile", "od4", P8),
    CreateUnit(1, "Odd Fast Missile", "od6", P8),
    CreateUnit(1, "Odd Fast Missile", "od8", P8),
    CreateUnit(1, "Odd Fast Missile", "od10", P8),
])

Loop(20)
