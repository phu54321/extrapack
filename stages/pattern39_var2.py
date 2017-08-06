'''
마이크로마우스 2 - 타이밍 순화
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

looptm = 80


Shoot(120 % looptm, [
    CreateUnit(1, "Missile", "u3", P7),
])

Shoot(75 % looptm, [
    CreateUnit(1, "Missile", "r3", P8),
])

Shoot(90 % looptm, [
    CreateUnit(1, "Missile", "d5", P8),
])

Shoot(100 % looptm, [
    CreateUnit(1, "Missile", "r7", P8),
])

Shoot(90 % looptm, [
    CreateUnit(1, "Missile", "u7", P7),
])


Loop(looptm)
