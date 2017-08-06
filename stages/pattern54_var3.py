# 느린 버젼

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Small Slow Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u9', P7),
], 6)

# 빠른 미사일 (스카웃)

dt = 9
dm = 4
SelectCounter(0)
for i in range(dm):
    acts = []
    for j in range(i, 9, dm):
        acts += [
            CreateUnit(1, 'Fast Missile', 'u%d' % (j + 1), P7),
        ]

    Shoot(dt * i, acts)
Loop(dt * dm)

# 느린 미사일 (배틀)

dt = 23
dm = 3
SelectCounter(1)
for i in range(dm):
    acts = []
    for j in range(i + 1, 10, dm):
        k = 10 - j
        acts += [
            CreateUnit(1, 'Big Slow Missile', 'r%d' % k, P8),
            Order('Big Slow Missile', P8, 'r%d' % k, Move, 'l%d' % k),
        ]
    Shoot(dt * i, acts)

Loop(dt * dm)
AlwaysShoot(KillUnitAt(All, 'Big Slow Missile', 'l', P8))
