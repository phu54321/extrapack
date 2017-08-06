'''
마이크로마우스
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '###### ##',
    '###### ##',
    '     #   ',
    '## # # ##',
    '## # # ##',
    '## # # ##',
    '   #     ',
    '## ######',
    '## ######',
])

SelectCounter(0)

#######

looptm = 48


Shoot(60 % looptm, [
    CreateUnit(1, "Fast Missile", "u3", P7),
])

Shoot(50 % looptm, [
    CreateUnit(1, "Fast Missile", "r3", P8),
])

Shoot(50 % looptm, [
    CreateUnit(1, "Fast Missile", "d5", P8),
])

Shoot(51 % looptm, [
    CreateUnit(1, "Fast Missile", "r7", P8),
])

Shoot(40 % looptm, [
    CreateUnit(1, "Fast Missile", "u7", P7),
])


Loop(looptm)
