'''
4괘
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)


#################################
# Effect blocks
#################################

def GiveBlock(x, y, lastplayer, thisplayer):
    if 1 <= x <= 9 and 1 <= y <= 9:
        return [
            MoveMainloc(x, y),
            CreateUnit(1, "Balloon", 'xymain', thisplayer),
            KillUnitAt(All, "Balloon", 'xymain', thisplayer),
            RemoveUnitAt(All, "(any unit)", 'xymain', Force1),
            GiveUnits(1, 'White Flare', lastplayer, 'xymain', thisplayer)
        ]

    else:
        return []


def CreateBlock(x, y, player):
    if 1 <= x <= 9 and 1 <= y <= 9:
        return [
            MoveMainloc(x, y),
            CreateUnit(1, "Balloon", 'xymain', player),
            KillUnitAt(All, "Balloon", 'xymain', player),
            RemoveUnitAt(All, "(men)", 'xymain', Force1),
            CreateUnit(1, "White Flare", 'xymain', player)
        ]

    else:
        return []


def KillBlock(x, y, player):
    if 1 <= x <= 9 and 1 <= y <= 9:
        return [
            MoveMainloc(x, y),
            CreateUnit(1, "Protoss Corsair", 'xymain', player),
            KillUnitAt(All, "Protoss Corsair", 'xymain', player),
            RemoveUnitAt(All, "White Flare", 'xymain', player)
        ]

    else:
        return []


def KillEff(x, y, player):
    if 1 <= x <= 9 and 1 <= y <= 9:
        return [
            MoveMainloc(x, y),
            CreateUnit(1, "Protoss Corsair", 'xymain', player),
            KillUnitAt(All, "Protoss Corsair", 'xymain', player),
        ]

    else:
        return []


#
#
#################################
# Pattern blocks
#################################

timestep = 3


def cliprect(l):
    return [(x, y) for x, y in l if 1 <= x <= 9 and 1 <= y <= 9]


def inv(i):
    return 10 - i

posfunc = [
    [lambda i, k=k: (i, k) for k in [1, 3, 5, 7, 9]],
    [lambda i, k=k: (i + k, i - k) for k in [-4, -2, 0, 2, 4]],
    [lambda i, k=k: (k, i) for k in [1, 3, 5, 7, 9]],
    [lambda i, k=k: (inv(i + k), i - k) for k in [-5, -3, -1, 1, 3, 5]],
    [lambda i, k=k: (inv(i), k) for k in [1, 3, 5, 7, 9]],
    [lambda i, k=k: (inv(i + k), inv(i - k)) for k in [-4, -2, 0, 2, 4]],
    [lambda i, k=k: (k, inv(i)) for k in [1, 3, 5, 7, 9]],
    [lambda i, k=k: (i + k, inv(i - k)) for k in [-5, -3, -1, 1, 3, 5]],
]

# first run

time = 0

for i in range(1, 10):
    acts = []

    onlytp = cliprect([f(i) for f in posfunc[0]])

    for x, y in onlytp:
        acts.append(CreateBlock(x, y, P7))

    StageTrigger(
        [
            Deaths(P8, Exactly, time, "@PatternSubCounter1"),
            Switch("CustomSwitch1", Cleared)
        ],
        [
            acts,
            PreserveTrigger()
        ]
    )

    time = time + timestep


# after

time = 0

for k in range(0, 8, 2):
    thisposfunc = posfunc[k]
    thisplayer = (k % 4 == 0) and P7 or P8
    lastposfunc = posfunc[(k + 6) % 8]
    lastplayer = (k % 4 == 0) and P8 or P7

    gridarray = [[0] * 10 for _ in range(10)]  # 0(unused), 1 ~ 9
    #
    # 0 : Empty    1 : lp
    # 2 : cp       3 : intermediate
    #

    for i in range(1, 10):
        lp = cliprect([f(i) for f in lastposfunc])
        for x, y in lp:
            gridarray[y][x] = 1

    for i in range(1, 10):
        thisexp = [[False] * 10 for _ in range(10)]

        acts = []

        lp = cliprect([f(i) for f in lastposfunc])
        tp = cliprect([f(i) for f in thisposfunc])

        for x, y in tp:
            if gridarray[y][x] == 0:
                acts.append(CreateBlock(x, y, thisplayer))

            elif gridarray[y][x] == 1:
                acts.append(GiveBlock(x, y, lastplayer, thisplayer))
            gridarray[y][x] += 2
            thisexp[y][x] = True

        for x, y in lp:
            if thisexp[y][x]:
                continue

            if gridarray[y][x] == 1:
                acts.append(KillBlock(x, y, lastplayer))

            elif gridarray[y][x] == 3:
                acts.append(KillEff(x, y, lastplayer))

            gridarray[y][x] -= 1

        StageTrigger(
            [
                Deaths(P8, Exactly, time, "@PatternSubCounter1"),
                Switch("CustomSwitch1", Set) if k == 0 else []
            ],
            [
                acts,
                SetSwitch('CustomSwitch1', Set),
                PreserveTrigger()
            ]
        )

        time = time + timestep

Loop(time)
