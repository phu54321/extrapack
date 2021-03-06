# 돌피하기 5탄

from trggen import *
from .stages_commonlib import *


dt = 21

InitWalls([
    ' ########',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '######## ',
], additionalactions=[
    CreateUnit(1, 'Small Slow Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u9', P7),
])


# -------

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Heavy Missile', 'l1', P7),
    CreateUnit(1, 'Heavy Missile', 'l3', P7),
    CreateUnit(1, 'Heavy Missile', 'l5', P7),
    CreateUnit(1, 'Heavy Missile', 'l7', P7),
    CreateUnit(1, 'Heavy Missile', 'l9', P7),
    CreateUnit(1, 'Small Slow Missile', 'r2', P8),
    CreateUnit(1, 'Small Slow Missile', 'r4', P8),
    CreateUnit(1, 'Small Slow Missile', 'r6', P8),
    CreateUnit(1, 'Small Slow Missile', 'r8', P8),
])
Shoot(dt, [
    CreateUnit(1, 'Small Slow Missile', 'l1', P7),
    CreateUnit(1, 'Small Slow Missile', 'l3', P7),
    CreateUnit(1, 'Small Slow Missile', 'l5', P7),
    CreateUnit(1, 'Small Slow Missile', 'l7', P7),
    CreateUnit(1, 'Small Slow Missile', 'l9', P7),
    CreateUnit(1, 'Heavy Missile', 'r2', P8),
    CreateUnit(1, 'Heavy Missile', 'r4', P8),
    CreateUnit(1, 'Heavy Missile', 'r6', P8),
    CreateUnit(1, 'Heavy Missile', 'r8', P8),
])
Loop(dt * 2)
