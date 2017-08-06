'''
간단한 틈피하기 - 주거라
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

# -------

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'l1', P7),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'l7', P7),
    CreateUnit(1, 'Fast Missile', 'r9', P8),
])

Loop(8)

# -------

SelectCounter(1)

Shoot(0, [
    KillUnitAt(1, 'Fast Missile', 'l1', P7),
    KillUnitAt(1, 'Fast Missile', 'r9', P8),

    CreateUnit(1, 'Small Missile', 'sr16', P8),

    CreateUnit(1, 'Small Missile', 'sl3', P7),
    CreateUnit(1, 'Small Missile', 'sl4', P7),
])

Shoot(0, [
    KillUnitAt(1, 'Fast Missile', 'r4', P8),

    CreateUnit(1, 'Small Missile', 'sr5', P8),
    CreateUnit(1, 'Small Missile', 'sr6', P8),

    CreateUnit(1, 'Small Missile', 'sr9', P8),
    CreateUnit(1, 'Small Missile', 'sr11', P8),

    CreateUnit(1, 'Small Missile', 'sl15', P7),
])

Shoot(0, [
    KillUnitAt(1, 'Fast Missile', 'l7', P7),

    CreateUnit(1, 'Small Missile', 'sl10', P7),
    CreateUnit(1, 'Small Missile', 'sl12', P7),
])

Loop(32)
