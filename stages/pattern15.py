'''
울트라 + 막쏘기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

ultra = [
    CreateUnit(1, "Fast Missile", "u1", P7),
    CreateUnit(1, "Fast Missile", "u2", P7),
    CreateUnit(1, "Fast Missile", "u3", P7),
    CreateUnit(1, "Fast Missile", "u4", P7),
    CreateUnit(1, "Fast Missile", "u5", P7),
    CreateUnit(1, "Fast Missile", "u6", P7),
    CreateUnit(1, "Fast Missile", "u7", P7),
    CreateUnit(1, "Fast Missile", "u8", P7),
    CreateUnit(1, "Fast Missile", "u9", P7),
]

# 정방향

Shoot(0, [
    ultra,
])

'''
윗방향 공격
'''

for t in range(30):  # t = 0~30
    if t % 2 == 0:
        col = 17 - (t // 2)  # 17 ~ 2
    else:
        col = 9 - (t // 2)  # 9 ~ -6
        if col <= 1:
            col += 16

    Shoot(5 + 2*t, [
        CreateUnit(1, "Small Missile", "sl%d" % col, P7),
        CreateUnit(1, "Small Missile", "sr%d" % col, P8),
    ])


## 역방향

Shoot(70, [
    ultra,
])
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

    Shoot(75 + 2*t, [
        CreateUnit(1, "Small Missile", "sl%d" % col, P7),
        CreateUnit(1, "Small Missile", "sr%d" % col, P8),
    ])


Loop(140)
