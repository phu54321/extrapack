from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

sall1 = [
    CreateUnit(1, 'Heavy Missile', 'r1', P8),
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r3', P8),
    CreateUnit(1, 'Heavy Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r5', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Heavy Missile', 'r7', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
    CreateUnit(1, 'Fast Missile', 'r9', P8),
]

sall2 = [
    CreateUnit(1, 'Fast Missile', 'r1', P8),
    CreateUnit(1, 'Heavy Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r3', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Heavy Missile', 'r5', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r7', P8),
    CreateUnit(1, 'Heavy Missile', 'r8', P8),
    CreateUnit(1, 'Fast Missile', 'r9', P8),
]


sall3 = [
    CreateUnit(1, 'Fast Missile', 'r1', P8),
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Heavy Missile', 'r3', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r5', P8),
    CreateUnit(1, 'Heavy Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r7', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
    CreateUnit(1, 'Heavy Missile', 'r9', P8),
]

sodd = [
    CreateUnit(1, 'Fast Missile', 'r1', P8),
    CreateUnit(1, 'Fast Missile', 'r3', P8),
    CreateUnit(1, 'Fast Missile', 'r5', P8),
    CreateUnit(1, 'Fast Missile', 'r7', P8),
    CreateUnit(1, 'Fast Missile', 'r9', P8),
]

seven = [
    CreateUnit(1, 'Fast Missile', 'r2', P8),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r6', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
]


SelectCounter(0)
Shoot(1 * 16, seven)
Shoot(2 * 16, sodd)
Shoot(4 * 16, sodd)
Shoot(5 * 16, seven)
Loop(6 * 16)

SelectCounter(1)
Shoot(0 * 16, sall1)
Shoot(3 * 16, sall2)
Shoot(6 * 16, sall3)
Loop(9 * 16)
