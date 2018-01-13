from trggen import *
from .stages_commonlib import *


def cract(rottype, mtype, x, y):
    return [
        MoveMainloc(x, y), CreateUnit(1, mtype, 'xymain', P8),
        MoveMainloc(y, 10 - x), CreateUnit(1, mtype, 'xymain', P8),
        MoveMainloc(10 - x, 10 - y), CreateUnit(1, mtype, 'xymain', P8),
        MoveMainloc(10 - y, x), CreateUnit(1, mtype, 'xymain', P8),
    ]


mtups = [
    (1, 'Fast Missile', 1, 1),
    (1, 'Missile', 1, 2),
    (0, 'Heavy Missile', 1, 3),
    (0, 'Small Slow Missile', 3, 3),
    (1, 'Small Missile', 2, 1),
    (1, 'Big Slow Missile', 2, 3),
]

InitWalls([
    '#### ####',
    '#       #',
    '#       #',
    '#       #',
    '         ',
    '#       #',
    '#       #',
    '#       #',
    '#### ####',
], additionalactions=[
    cract(*mtup) for mtup in mtups
])


def odact(rottype, mtype, x, y):
    StageTrigger(
        Always(),
        [
            MoveMainloc(x, y),
            MoveLocation('cloc1', 'Map Revealer', P8, 'xymain'),
            MoveMainloc(y, 10 - x),
            MoveLocation('cloc2', 'Map Revealer', P8, 'xymain'),
            MoveMainloc(10 - x, 10 - y),
            MoveLocation('cloc3', 'Map Revealer', P8, 'xymain'),
            MoveMainloc(10 - y, x),
            MoveLocation('cloc4', 'Map Revealer', P8, 'xymain'),
        ]
    )

    if rottype:
        StageTrigger(
            [
                Bring(P8, AtLeast, 1, mtype, 'cloc1'),
                Bring(P8, AtLeast, 1, mtype, 'cloc2'),
                Bring(P8, AtLeast, 1, mtype, 'cloc3'),
                Bring(P8, AtLeast, 1, mtype, 'cloc4'),
            ],
            [
                Order(mtype, P8, 'cloc1', Move, 'cloc2'),
                Order(mtype, P8, 'cloc2', Move, 'cloc3'),
                Order(mtype, P8, 'cloc3', Move, 'cloc4'),
                Order(mtype, P8, 'cloc4', Move, 'cloc1'),
            ]
        )

    else:
        StageTrigger(
            [
                Bring(P8, AtLeast, 1, mtype, 'cloc1'),
                Bring(P8, AtLeast, 1, mtype, 'cloc2'),
                Bring(P8, AtLeast, 1, mtype, 'cloc3'),
                Bring(P8, AtLeast, 1, mtype, 'cloc4'),
            ],
            [
                Order(mtype, P8, 'cloc1', Move, 'cloc4'),
                Order(mtype, P8, 'cloc2', Move, 'cloc1'),
                Order(mtype, P8, 'cloc3', Move, 'cloc2'),
                Order(mtype, P8, 'cloc4', Move, 'cloc3'),
            ]
        )


for mtup in mtups:
    odact(*mtup)
