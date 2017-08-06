'''
사이드 반칸무빙 - 역방향
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    ' ########',
    ' #       ',
    ' #     # ',
    ' #     # ',
    ' #     # ',
    ' #     # ',
    ' #     # ',
    '       # ',
    '######## ',
])

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Odd Fast Missile", "ol1", P7),
    CreateUnit(1, "Fast Missile", "l2", P7),
    CreateUnit(1, "Odd Fast Missile", "ol4", P7),
    CreateUnit(1, "Fast Missile", "l5", P7),
    CreateUnit(1, "Odd Fast Missile", "ol7", P7),
    CreateUnit(1, "Fast Missile", "l8", P7),
    CreateUnit(1, "Odd Fast Missile", "ol10", P7),
])

Shoot(10, [
    CreateUnit(1, "Odd Fast Missile", "ol2", P7),
    CreateUnit(1, "Fast Missile", "l3", P7),
    CreateUnit(1, "Odd Fast Missile", "ol5", P7),
    CreateUnit(1, "Fast Missile", "l6", P7),
    CreateUnit(1, "Odd Fast Missile", "ol8", P7),
    CreateUnit(1, "Fast Missile", "l9", P7),
])

Shoot(20, [
    CreateUnit(1, "Fast Missile", "l1", P7),
    CreateUnit(1, "Odd Fast Missile", "ol3", P7),
    CreateUnit(1, "Fast Missile", "l4", P7),
    CreateUnit(1, "Odd Fast Missile", "ol6", P7),
    CreateUnit(1, "Fast Missile", "l7", P7),
    CreateUnit(1, "Odd Fast Missile", "ol9", P7),
])

Loop(30)
