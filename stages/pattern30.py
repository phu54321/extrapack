'''
해처리 연습
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()


SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Missile", 'd1', P8),
    CreateUnit(1, "Missile", 'd3', P8),
    CreateUnit(1, "Missile", 'd5', P8),
    CreateUnit(1, "Missile", 'd7', P8),
    CreateUnit(1, "Missile", 'd9', P8),
])


Shoot(24, [
    CreateUnit(1, "Missile", 'd2', P8),
    CreateUnit(1, "Missile", 'd4', P8),
    CreateUnit(1, "Missile", 'd6', P8),
    CreateUnit(1, "Missile", 'd8', P8),
])

Loop(48)

#######

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Heavy Missile", 'l1', P7),
    CreateUnit(1, "Fast Missile",  'l2', P7),
    CreateUnit(1, "Fast Missile",  'l3', P7),
    CreateUnit(1, "Heavy Missile", 'l4', P7),
    CreateUnit(1, "Fast Missile",  'l5', P7),
    CreateUnit(1, "Fast Missile",  'l6', P7),
    CreateUnit(1, "Heavy Missile", 'l7', P7),
    CreateUnit(1, "Fast Missile",  'l8', P7),
    CreateUnit(1, "Fast Missile",  'l9', P7),
])


Shoot(48, [
    CreateUnit(1, "Fast Missile",  'l1', P7),
    CreateUnit(1, "Fast Missile",  'l2', P7),
    CreateUnit(1, "Heavy Missile", 'l3', P7),
    CreateUnit(1, "Fast Missile",  'l4', P7),
    CreateUnit(1, "Fast Missile",  'l5', P7),
    CreateUnit(1, "Heavy Missile", 'l6', P7),
    CreateUnit(1, "Fast Missile",  'l7', P7),
    CreateUnit(1, "Fast Missile",  'l8', P7),
    CreateUnit(1, "Heavy Missile", 'l9', P7),
])


Shoot(96, [
    CreateUnit(1, "Fast Missile",  'l1', P7),
    CreateUnit(1, "Heavy Missile", 'l2', P7),
    CreateUnit(1, "Fast Missile",  'l3', P7),
    CreateUnit(1, "Fast Missile",  'l4', P7),
    CreateUnit(1, "Heavy Missile", 'l5', P7),
    CreateUnit(1, "Fast Missile",  'l6', P7),
    CreateUnit(1, "Fast Missile",  'l7', P7),
    CreateUnit(1, "Heavy Missile", 'l8', P7),
    CreateUnit(1, "Fast Missile",  'l9', P7),
])

Loop(144)
