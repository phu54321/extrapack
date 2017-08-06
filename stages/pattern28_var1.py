'''
최소공배수 - 간격넓음
'''

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
], 12)


def run(c, t):
    SelectCounter(c)
    Shoot(
        123457 % t,
        CreateUnit(1, 'Small Slow Heavy Missile', 'u%d' % (c + 1), P7)
    )
    Loop(t)

dt = 9

run(0, dt * 6)
run(1, dt * 7)
run(2, dt * 5)
run(3, dt * 9)
run(4, dt * 6)
run(5, dt * 5)
run(6, dt * 4)
run(7, dt * 8)
run(8, dt * 4)
