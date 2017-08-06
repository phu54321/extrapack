'''
팔방에서 줄긋기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

#######

SelectCounter(0)

hv_sloc = [
    [
        ['ou1', 'ou3', 'ou5', 'ou7', 'ou9'],
        ['ou2', 'ou4', 'ou6', 'ou8', 'ou10'],
    ],
    [
        ['ol2', 'ol4', 'ol6', 'ol8', 'ol10'],
        ['ol1', 'ol3', 'ol5', 'ol7', 'ol9'],
    ],
    [
        ['od2', 'od4', 'od6', 'od8', 'od10'],
        ['od1', 'od3', 'od5', 'od7', 'od9'],
    ],
    [
        ['or1', 'or3', 'or5', 'or7', 'or9'],
        ['or2', 'or4', 'or6', 'or8', 'or10'],
    ],
]

hv_sp = [P7, P7, P8, P8]


def hv_sact(dir, x):
    return [
        CreateUnit(1, "Odd Fast Missile", hv_sloc[dir][x][i], hv_sp[dir])
        for i in range(len(hv_sloc[dir][x]))
    ]


#######


dt = 15
time = 0


Shoot(time, hv_sact(0, 0))
time += dt
Shoot(time, hv_sact(0, 1))
Shoot(time, hv_sact(1, 0))
time += dt
Shoot(time, hv_sact(1, 1))
Shoot(time, hv_sact(2, 0))
time += dt
Shoot(time, hv_sact(2, 1))
Shoot(time, hv_sact(3, 0))
time += dt
Shoot(0, hv_sact(3, 1))
Loop(time)


#######
