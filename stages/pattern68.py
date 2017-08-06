from trggen import *
from .stages_commonlib import *


InitNone([
    CreateUnit(1, 'Heavy Missile', 'u%d' % i, P7)
    for i in range(1, 10)
])

AlwaysShoot([
    KillUnitAt(All, "Small Slow Heavy Missile", "u", P7),
    KillUnitAt(All, "Small Missile", "r", P8),
])

# ---------------

SelectCounter(0)

Shoot(0, [
    [
        CreateUnit(1, "Small Slow Heavy Missile", "d%d" % i, P7),
        Order("Small Slow Heavy Missile", P7, "d%d" % i, Move, "u%d" % i)
    ] for i in range(1, 10)
])

Loop(96)


# ---------------

SelectCounter(1)

for i in range(16):
    interval = 2.3
    dx = interval / 7
    if i < 8:
        x0 = i * dx
    elif i < 12:
        x0 = interval * 0.5 - (i - 8) * dx
    else:
        x0 = interval * 1.5 - (i - 8) * dx

    Shoot(3 * i, [[
        PxMoveLocation("cloc1", -3, x0 + j * interval),
        PxMoveLocation("cloc2", 12, x0 + j * interval),
        CreateUnit(1, "Small Missile", "cloc1", P8),
        Order("Small Missile", P8, "cloc1", Move, "cloc2"),
    ] for j in range(-3, 6) if 0 <= (x0 + j * interval) <= 9])

Loop(48)

# ---------------
