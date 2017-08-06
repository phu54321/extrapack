'''
간단한 폭탄피하기
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
    time += 7

for i in range(9):
    BombPattern(time, 'Zerg Overlord', P8, bevn * i + ball + eall * (8 - i))
    time += 7

Loop(time)
