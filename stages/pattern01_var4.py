'''
매우 간단
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
    BombPattern(time, 'Flare', P8, eall * (8 - i) + bodd + eall * i)
    time += 2

for i in range(9):
    BombPattern(time, 'Flare', P8, eall * i + bevn + eall * (8 - i))
    time += 2

Loop(time)
