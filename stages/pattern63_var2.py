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
    CreateUnit(1, 'Fast Missile', 'r3', P8),
    CreateUnit(1, 'Fast Missile', 'l5', P7),
    CreateUnit(1, 'Fast Missile', 'r7', P8),
    CreateUnit(1, 'Fast Missile', 'l9', P7),
])

Loop(5)

# -------

SelectCounter(1)

Shoot(0, [
    KillUnitAt(1, 'Fast Missile', 'l1', P7),
    KillUnitAt(1, 'Fast Missile', 'r3', P8),
    KillUnitAt(1, 'Fast Missile', 'l5', P7),
    KillUnitAt(1, 'Fast Missile', 'r7', P8),
    KillUnitAt(1, 'Fast Missile', 'l9', P7),
])

Loop(20)

# --------

SelectCounter(2)

Shoot(0, [
    CreateUnit(1, 'Missile', 'd1', P8),
    CreateUnit(1, 'Missile', 'd3', P8),
    CreateUnit(1, 'Missile', 'd5', P8),
    CreateUnit(1, 'Missile', 'd7', P8),
    CreateUnit(1, 'Missile', 'd9', P8),
])

Loop(7)

# -------

SelectCounter(3)

Shoot(0, [
    KillUnitAt(2, 'Missile', 'd1', P8),
    KillUnitAt(2, 'Missile', 'd3', P8),
    KillUnitAt(2, 'Missile', 'd5', P8),
    KillUnitAt(2, 'Missile', 'd7', P8),
    KillUnitAt(2, 'Missile', 'd9', P8),
])

Loop(28)

# --------

