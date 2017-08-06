'''
막쏘기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

# 정방향

'''
윗방향 공격
'''

time = 0

for t in range(30):  # t = 0~30
    if t % 2 == 0:
        col = 17 - (t // 2)  # 17 ~ 2
    else:
        col = 9 - (t // 2)  # 9 ~ -6
        if col <= 1:
            col += 16

    Shoot(time, [
        CreateUnit(1, "Small Missile", "sl%d" % col, P7),
    ])
    time += 1

time += 12

'''
아랫방향 공격
'''

for t in range(30):  # t = 0~23
    if t % 2 == 0:
        col = 17 - (t // 2)  # 17 ~ 2
    else:
        col = 9 - (t // 2)  # 9 ~ -6
        if col <= 1:
            col += 16

    col = 19 - col

    Shoot(time, [
        CreateUnit(1, "Small Missile", "sr%d" % col, P8),
    ])
    time += 1

time += 12

Loop(time)
