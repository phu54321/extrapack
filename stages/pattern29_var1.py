'''
폭탄 + 퀸
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Heavy Missile", 'u2', P7),
    CreateUnit(1, "Heavy Missile", 'u4', P7),
    CreateUnit(1, "Heavy Missile", 'u6', P7),
    CreateUnit(1, "Heavy Missile", 'u8', P7),
])

# Bombing

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, "Small Slow Missile", 'd1', P8),
    CreateUnit(1, "Small Slow Missile", 'd2', P8),
    CreateUnit(1, "Small Slow Missile", 'd3', P8),
    CreateUnit(1, "Small Slow Missile", 'd4', P8),
    CreateUnit(1, "Small Slow Missile", 'd5', P8),
    CreateUnit(1, "Small Slow Missile", 'd6', P8),
    CreateUnit(1, "Small Slow Missile", 'd7', P8),
    CreateUnit(1, "Small Slow Missile", 'd8', P8),
    CreateUnit(1, "Small Slow Missile", 'd9', P8),
])
Loop(49)


# Missile

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Fast Missile", 'u1', P7),
    CreateUnit(1, "Fast Missile", 'u3', P7),
    CreateUnit(1, "Fast Missile", 'u5', P7),
    CreateUnit(1, "Fast Missile", 'u7', P7),
    CreateUnit(1, "Fast Missile", 'u9', P7),
])

Shoot(14, [
    CreateUnit(1, "Fast Missile", 'u2', P7),
    CreateUnit(1, "Fast Missile", 'u4', P7),
    CreateUnit(1, "Fast Missile", 'u6', P7),
    CreateUnit(1, "Fast Missile", 'u8', P7),
])

Loop(28)
