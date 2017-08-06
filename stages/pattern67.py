from trggen import *
from .stages_commonlib import *


InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u%d' % i, P7)
    for i in range(1, 10)
])


# ---------------

dt = 7

SelectCounter(0)

for i in range(16):
    if i < 8:
        pos = i + 1
    else:
        pos = 17 - i

    Shoot(i * dt, [
        CreateUnit(1, 'Heavy Missile', 'u%d' % pos, P7),
        CreateUnit(1, 'Heavy Missile', 'd%d' % (10 - pos), P8),
    ])

    Shoot((i + 4) % 16 * dt, [
        CreateUnit(1, 'Heavy Missile', 'l%d' % (10 - pos), P7),
        CreateUnit(1, 'Heavy Missile', 'r%d' % pos, P8)
    ])

Loop(16 * dt)

# ---------------
