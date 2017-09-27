'''
미사일 + 폭탄 변형 (Easy)

2@@@ 못깹니다.

'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

eall = ['         ']
bodd = ['# # # # #']
bevn = [' # # # # ']

time = 0

for i in range(9):
    BombPattern(time, 'White Flare', P8, eall * (8 - i) + bodd * (i + 1))
    time += 6

Shoot(time - 20, [
    CreateUnit(1, 'Missile', 'u1', P7),
    CreateUnit(1, 'Missile', 'u3', P7),
    CreateUnit(1, 'Missile', 'u5', P7),
    CreateUnit(1, 'Missile', 'u7', P7),
    CreateUnit(1, 'Missile', 'u9', P7),
])

for i in range(9):
    BombPattern(time, 'Flare', P7, bevn * (i + 1) + eall * (8 - i))
    time += 6

Shoot(time - 20, [
    CreateUnit(1, 'Missile', 'd2', P8),
    CreateUnit(1, 'Missile', 'd4', P8),
    CreateUnit(1, 'Missile', 'd6', P8),
    CreateUnit(1, 'Missile', 'd8', P8),
])


Loop(time)
