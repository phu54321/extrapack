# 배틀 + 스카웃계단

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

# 느린 미사일 (배틀)

dt = 25
dm = 3
SelectCounter(0)
for i in range(dm):
    acts = []
    for j in range(i + 1, 10, dm):
        k = 10 - j
        acts += [
            CreateUnit(1, 'Big Slow Missile', 'u%d' % k, P7),
            Order('Big Slow Missile', P7, 'u%d' % k, Move, 'd%d' % k),
        ]

    Shoot(dt * i, acts)
Loop(dt * dm)

# 느린 미사일 (배틀)

dt = 20
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
AlwaysShoot([
    KillUnitAt(All, 'Big Slow Missile', 'l', P8),
    KillUnitAt(All, 'Big Slow Missile', 'd', P7),
])
