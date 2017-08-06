'''
옆으로 변형
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

eall = ['         ']
ball = ['#########']
bodd = ['# # # # #']
bevn = [' # # # # ']


def transpose(arr):
    rarr = [[0] * 9 for _ in range(9)]
    for y in range(9):
        for x in range(9):
            rarr[y][x] = arr[x][y]

    return rarr


time = 0
for i in range(9):
    BombPattern(time, 'Flare', P7,
                transpose(eall * (8 - i) + ball + bodd * i))
    time += 5

for i in range(9):
    BombPattern(time, 'Flare', P8,
                transpose(bevn * i + ball + eall * (8 - i)))
    time += 5

Loop(time)
