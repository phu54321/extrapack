'''
칼타이밍 변형
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

eall = ['         ']
ball = ['#########']
bodd = ['# # # # #']
bevn = [' # # # # ']

time = 0
for i in range(9):
    BombPattern(time, 'Zerg Overlord', P8, eall * (8 - i) + ball + bodd * i)
    time += 1

for i in range(9):
    BombPattern(time, 'Zerg Overlord', P8, bevn * i + ball + eall * (8 - i))
    time += 5

Loop(time + 3)
