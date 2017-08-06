'''
파일런 + 울트라같은사이드스테이지미사일
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

#######


def CreateBlock(x, y):
    return [
        MoveMainloc(x, y),
        CreateUnit(1, "NarrowBlock", "blockchamber", P7),
        MoveUnit(1, "NarrowBlock", P7, "blockchamber", 'xymain'),
        RemoveUnitAt(All, "NarrowBlock", "blockchamber", P7),
    ]

SelectCounter(0)

for i in range(1, 10):
    Shoot(4*i, [
        CreateBlock(i, 1),
        CreateBlock(i, 2),
        CreateBlock(i, 3),
        CreateBlock(i, 4),
        CreateBlock(i, 5),
        CreateBlock(i, 6),
        CreateBlock(i, 7),
        CreateBlock(i, 8),
        CreateBlock(i, 9),
    ])

for i in range(1, 10):
    Shoot(40 + 4*i, [
        MoveMainloc(i, 1), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 2), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 3), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 4), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 5), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 6), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 7), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 8), KillUnitAt(All, "NarrowBlock", "xymain", P7),
        MoveMainloc(i, 9), KillUnitAt(All, "NarrowBlock", "xymain", P7),
    ])

Loop(86)

#######

SelectCounter(1)
for j in range(1, 10):
    Shoot((j - 1) * 4, [
        CreateUnit(1, "Fast Missile", "r%d" % j, P8),
    ])

Loop(50)
