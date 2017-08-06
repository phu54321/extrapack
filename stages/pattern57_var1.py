'''
울트라 왔다갔다. (사인파)
'''

from trggen import *
from .stages_commonlib import *


def crlbd(i, player):
    return [
        MoveMainloc(1, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(2, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(3, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(4, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(5, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(6, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(7, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(8, i), CreateUnit(1, 'Missile', 'xymain', player),
        MoveMainloc(9, i), CreateUnit(1, 'Missile', 'xymain', player),
    ]

InitNormalMissileMove([
    crlbd(1, P7),
    crlbd(5, P8),
])

####


SelectCounter(0)

for i in range(9):
    Shoot((i * 6) % 80, [
        MoveMainloc(i + 1, 1),
        MoveLocation('cloc1', 'Map Revealer', P8, 'xymain'),
        MoveMainloc(i + 1, 5),
        Order('Missile', P7, 'cloc1', Move, 'xymain'),

        MoveMainloc(i + 1, 5),
        MoveLocation('cloc1', 'Map Revealer', P8, 'xymain'),
        MoveMainloc(i + 1, 9),
        Order('Missile', P8, 'cloc1', Move, 'xymain'),
    ])

    Shoot((i * 6 + 40) % 80, [
        MoveMainloc(i + 1, 9),
        MoveLocation('cloc1', 'Map Revealer', P8, 'xymain'),
        MoveMainloc(i + 1, 5),
        Order('Missile', P8, 'cloc1', Move, 'xymain'),

        MoveMainloc(i + 1, 5),
        MoveLocation('cloc1', 'Map Revealer', P8, 'xymain'),
        MoveMainloc(i + 1, 1),
        Order('Missile', P7, 'cloc1', Move, 'xymain'),
    ])

Loop(80)
