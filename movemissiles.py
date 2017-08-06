from trggen import *


def OrderNormal(mt):
    return [
        [Order(mt, P7, "u%d" % i, Move, "d%d" % i) for i in range(1, 10)],
        [Order(mt, P7, "l%d" % i, Move, "r%d" % i) for i in range(1, 10)],
        [Order(mt, P8, "d%d" % i, Move, "u%d" % i) for i in range(1, 10)],
        [Order(mt, P8, "r%d" % i, Move, "l%d" % i) for i in range(1, 10)],
    ]


def OrderOdd(mt):
    return [
        [Order(mt, P7, "ou%d" % i, Move, "od%d" % i) for i in range(1, 11)],
        [Order(mt, P7, "ol%d" % i, Move, "or%d" % i) for i in range(1, 11)],
        [Order(mt, P8, "od%d" % i, Move, "ou%d" % i) for i in range(1, 11)],
        [Order(mt, P8, "or%d" % i, Move, "ol%d" % i) for i in range(1, 11)],
    ]


def KillNormal(mt):
    return [
        KillUnitAt(All, mt, "u", P8),
        KillUnitAt(All, mt, "l", P8),
        KillUnitAt(All, mt, "d", P7),
        KillUnitAt(All, mt, "r", P7),
    ]


def MoveTrg(actions):
    Trigger(
        players=[P8],
        conditions=[
            Switch("NormalMissileMove", Set),
        ],
        actions=[
            actions,
            PreserveTrigger(),
        ],
    )


MoveTrg(OrderNormal("Fast Missile"))
MoveTrg(OrderNormal("Missile"))
MoveTrg(OrderNormal("Small Slow Missile"))
MoveTrg(OrderNormal("Small Slow Heavy Missile"))
MoveTrg(OrderNormal("Heavy Missile"))
MoveTrg(OrderOdd("Odd Fast Missile"))


dm1 = 'Diagonal Missile RL'
dm2 = 'Diagonal Missile LR'

Trigger(
    players=[P8],
    conditions=[
        Switch("NormalMissileMove", Set),
    ],
    actions=[
        [Order(dm2, P7, "ul%d" % i, Move, "dr%d" % i) for i in range(1, 10)],
        [Order(dm1, P7, "ur%d" % i, Move, "dl%d" % i) for i in range(1, 10)],
        [Order(dm1, P8, "dl%d" % i, Move, "ur%d" % i) for i in range(1, 10)],
        [Order(dm2, P8, "dr%d" % i, Move, "ul%d" % i) for i in range(1, 10)],
        PreserveTrigger(),
    ],
)


sm = 'Small Missile'
MoveTrg([
    [Order(sm, P7, "su%d" % i, Move, "sd%d" % i) for i in range(1, 19)],
    [Order(sm, P7, "sl%d" % i, Move, "sr%d" % i) for i in range(1, 19)],
])

MoveTrg([
    [Order(sm, P8, "sd%d" % i, Move, "su%d" % i) for i in range(1, 19)],
    [Order(sm, P8, "sr%d" % i, Move, "sl%d" % i) for i in range(1, 19)],
])

# -------

Trigger(
    players=[P8],
    conditions=[
        Switch("NormalMissileMove", Set),
    ],
    actions=[
        KillNormal("Fast Missile"),
        KillNormal("Missile"),
        KillNormal("Odd Fast Missile"),
        KillNormal("Small Slow Missile"),
        KillNormal("Small Missile"),
        KillNormal("Small Slow Heavy Missile"),
        KillNormal("Heavy Missile"),

        KillUnitAt(All, dm1, "diagd_u", P8),
        KillUnitAt(All, dm2, "diagd_u", P8),
        KillUnitAt(All, dm1, "diagd_r", P8),
        KillUnitAt(All, dm2, "diagd_l", P8),

        KillUnitAt(All, dm1, "diagd_d", P7),
        KillUnitAt(All, dm2, "diagd_d", P7),
        KillUnitAt(All, dm1, "diagd_l", P7),
        KillUnitAt(All, dm2, "diagd_r", P7),
        PreserveTrigger(),
    ],
)
