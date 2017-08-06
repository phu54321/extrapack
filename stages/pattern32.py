'''
사방에서 퀸

적당히 어려운 편
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Heavy Missile", 'u2', P7),
    CreateUnit(1, "Heavy Missile", 'u4', P7),
    CreateUnit(1, "Heavy Missile", 'u6', P7),
    CreateUnit(1, "Heavy Missile", 'u8', P7),
])

SelectCounter(0)


dirdict = ['u', 'l', 'd', 'r']
plydict = [P7, P7, P8, P8]

shootodd = lambda dir: [
    CreateUnit(1, "Missile", '%s1' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s3' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s5' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s7' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s9' % dirdict[dir], plydict[dir]),
]

shooteven = lambda dir: [
    CreateUnit(1, "Missile", '%s2' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s4' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s6' % dirdict[dir], plydict[dir]),
    CreateUnit(1, "Missile", '%s8' % dirdict[dir], plydict[dir]),
]

Shoot(0, [
    shootodd(0),
    shootodd(1),
    shootodd(2),
    shootodd(3),
])

Shoot(28, [
    shooteven(0),
    shooteven(1),
    shooteven(2),
    shooteven(3),
])

Loop(56)
