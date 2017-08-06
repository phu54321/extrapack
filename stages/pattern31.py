'''
느린 미사일 폭풍
'''

from trggen import *
from .stages_commonlib import *

# Some special init

InitNormalMissileMove([
    MoveMainloc(1, 1), CreateUnit(1, 'Block', 'xymain', P7),
    MoveMainloc(1, 9), CreateUnit(1, 'Block', 'xymain', P7),
    MoveMainloc(9, 1), CreateUnit(1, 'Block', 'xymain', P7),
    MoveMainloc(9, 9), CreateUnit(1, 'Block', 'xymain', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u1', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u2', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u3', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u4', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u5', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u6', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u7', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u8', P7),
    CreateUnit(1, "Small Slow Heavy Missile", 'u9', P7),
], 12)

#######

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Big Slow Missile", 'u1', P7),
    CreateUnit(1, "Big Slow Missile", 'u3', P7),
    CreateUnit(1, "Big Slow Missile", 'u5', P7),
    CreateUnit(1, "Big Slow Missile", 'u7', P7),
    CreateUnit(1, "Big Slow Missile", 'u9', P7),
    Order("Big Slow Missile", P7, 'u1', Move, 'd1'),
    Order("Big Slow Missile", P7, 'u3', Move, 'd3'),
    Order("Big Slow Missile", P7, 'u5', Move, 'd5'),
    Order("Big Slow Missile", P7, 'u7', Move, 'd7'),
    Order("Big Slow Missile", P7, 'u9', Move, 'd9'),
])

Shoot(48, [
    CreateUnit(1, "Big Slow Missile", 'u2', P7),
    CreateUnit(1, "Big Slow Missile", 'u4', P7),
    CreateUnit(1, "Big Slow Missile", 'u6', P7),
    CreateUnit(1, "Big Slow Missile", 'u8', P7),
    Order("Big Slow Missile", P7, 'u2', Move, 'd2'),
    Order("Big Slow Missile", P7, 'u4', Move, 'd4'),
    Order("Big Slow Missile", P7, 'u6', Move, 'd6'),
    Order("Big Slow Missile", P7, 'u8', Move, 'd8'),
])

Loop(96)

AlwaysShoot(KillUnitAt(All, "Big Slow Missile", 'd', P7))


#######


SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Missile", 'l1', P7),
    CreateUnit(1, "Missile", 'r2', P8),
    CreateUnit(1, "Missile", 'r8', P8),
    CreateUnit(1, "Missile", 'l9', P7),
])

Loop(15)


#######


SelectCounter(2)

Shoot(0, [
    CreateUnit(1, "Missile", 'l4', P7),
    CreateUnit(1, "Missile", 'r5', P8),
    CreateUnit(1, "Missile", 'l6', P7),
])

Loop(20)
