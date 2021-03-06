# 역방향

from trggen import *
from .stages_commonlib import *

InitNone([
    CreateUnit(1, 'Small Slow Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u9', P7),
    Order('Small Slow Heavy Missile', P7, 'u1', Move, 'd1'),
    Order('Small Slow Heavy Missile', P7, 'u2', Move, 'd2'),
    Order('Small Slow Heavy Missile', P7, 'u3', Move, 'd3'),
    Order('Small Slow Heavy Missile', P7, 'u4', Move, 'd4'),
    Order('Small Slow Heavy Missile', P7, 'u5', Move, 'd5'),
    Order('Small Slow Heavy Missile', P7, 'u6', Move, 'd6'),
    Order('Small Slow Heavy Missile', P7, 'u7', Move, 'd7'),
    Order('Small Slow Heavy Missile', P7, 'u8', Move, 'd8'),
    Order('Small Slow Heavy Missile', P7, 'u9', Move, 'd9'),
])

AlwaysShoot([
    [
        [MoveYRow(i), Order('Heavy Missile', P7, 'yall', Move, 'r%d' % i)]
        for i in range(1, 10)
    ],
    KillUnitAt(All, 'Heavy Missile', 'r', P7),
    KillUnitAt(All, 'Small Slow Heavy Missile', 'd', P7),
    MoveUnit(All, 'Heavy Missile', P8, 'Anywhere', 'minimapping'),
])

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Heavy Missile', 'l1', P8),
    CreateUnit(1, 'Heavy Missile', 'l2', P8),
    CreateUnit(1, 'Heavy Missile', 'l3', P8),
    CreateUnit(1, 'Heavy Missile', 'l4', P8),
    CreateUnit(1, 'Heavy Missile', 'l5', P8),
    CreateUnit(1, 'Heavy Missile', 'l6', P8),
    CreateUnit(1, 'Heavy Missile', 'l7', P8),
    CreateUnit(1, 'Heavy Missile', 'l8', P8),
    CreateUnit(1, 'Heavy Missile', 'l9', P8),
])

for i in range(1, 10):
    Shoot(i * 5, [
        MoveYRow(10 - i),
        GiveUnits(All, 'Heavy Missile', P8, 'yall', P7),
    ])

for i in range(1, 10):
    Shoot((30 + i * 5) % 50, [
        MoveYRow(10 - i),
        GiveUnits(All, 'Heavy Missile', P7, 'yall', P8),
    ])

Loop(50)
