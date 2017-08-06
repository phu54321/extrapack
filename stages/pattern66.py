from trggen import *
from .stages_commonlib import *


InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u%d' % i, P7)
    for i in range(1, 10)
])


# ---------------

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'l1', P7),
    CreateUnit(1, 'Fast Missile', 'l4', P7),
    CreateUnit(1, 'Fast Missile', 'l7', P7),
])

Shoot(9, [
    CreateUnit(1, 'Fast Missile', 'l2', P7),
    CreateUnit(1, 'Fast Missile', 'l5', P7),
    CreateUnit(1, 'Fast Missile', 'l8', P7),
])

Shoot(18, [
    CreateUnit(1, 'Fast Missile', 'l3', P7),
    CreateUnit(1, 'Fast Missile', 'l6', P7),
    CreateUnit(1, 'Fast Missile', 'l9', P7),
])

Loop(27)

# ---------------

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'r3', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r9', P8),
])

Shoot(8, [
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r5', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
])

Shoot(16, [
    CreateUnit(1, 'Fast Missile', 'r1', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r7', P8),
])

Loop(24)
