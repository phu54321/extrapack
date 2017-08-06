'''
간단한 중간해처리
'''

from trggen import *
from .stages_commonlib import *


def CreateBlock(loc):
    return [
        CreateUnit(1, "Protoss Observer", loc, P7),
        KillUnitAt(All, "Protoss Observer", loc, P7),
        CreateUnit(1, "NarrowBlock", "blockchamber", P7),
        MoveUnit(1, "NarrowBlock", P7, "blockchamber", loc),
        RemoveUnitAt(All, "NarrowBlock", "blockchamber", P7),
    ]


InitNormalMissileMove()

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
])

for i in range(1, 10):
    Shoot(i * 5, [
        CreateUnit(1, "Fast Missile", "l%d" % i, P7),
        CreateUnit(1, "Fast Missile", "r%d" % i, P8),
    ])

for i in range(1, 10):
    Shoot(i * 3, [
        MoveMainloc(1, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(2, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(3, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(4, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(6, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(7, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(8, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
        MoveMainloc(9, i), KillUnitAt(All, "NarrowBlock", 'xymain', P7),
    ])


for i in range(1, 10):
    Shoot(60 + i * 3, [
        MoveMainloc(1, 10 - i), CreateBlock('xymain'),
        MoveMainloc(2, 10 - i), CreateBlock('xymain'),
        MoveMainloc(3, 10 - i), CreateBlock('xymain'),
        MoveMainloc(4, 10 - i), CreateBlock('xymain'),
        MoveMainloc(6, 10 - i), CreateBlock('xymain'),
        MoveMainloc(7, 10 - i), CreateBlock('xymain'),
        MoveMainloc(8, 10 - i), CreateBlock('xymain'),
        MoveMainloc(9, 10 - i), CreateBlock('xymain'),
    ])

Loop(90)
