from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Heavy Missile', 'u9', P7),
], 6)

SelectCounter(0)

dt = 10
dm = 3

for i in range(dm):
    acts = []
    for j in range(i, 18, dm):
        acts += [
            CreateUnit(1, 'Small Missile', 'su%d' % (j + 1), P7),
            CreateUnit(1, 'Small Missile', 'sd%d' % (18 - j), P8),
        ]
    Shoot(i * dt, acts)

Loop(dt * dm)
