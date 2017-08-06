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

hv_sact = lambda dir, x: [
    CreateUnit(1, "Odd Fast Missile", hv_sloc[dir][x][i], hv_sp[dir])
    for i in range(len(hv_sloc[dir][x]))
]

dg_sloc = [
    [
        ['ul1', 'ul3', 'ul5', 'ul7', 'ul9'],
        ['ul2', 'ul4', 'ul6', 'ul8']
    ],
    [
        ['dl2', 'dl4', 'dl6', 'dl8'],
        ['dl1', 'dl3', 'dl5', 'dl7', 'dl9']
    ],
    [
        ['dr2', 'dr4', 'dr6', 'dr8'],
        ['dr1', 'dr3', 'dr5', 'dr7', 'dr9']
    ],
    [
        ['ur1', 'ur3', 'ur5', 'ur7', 'ur9'],
        ['ur2', 'ur4', 'ul6', 'ul8']
    ],
]

dg_sp = [P7, P8, P8, P7]


def dg_sact(dir, x):
    if dir in [0, 2]:
        ms = "Diagonal Missile LR"
    else:
        ms = "Diagonal Missile RL"

    return [
        CreateUnit(1, ms, dg_sloc[dir][x][i], dg_sp[dir])
        for i in range(len(dg_sloc[dir][x]))
    ]


#######


dt = 12
time = 0


Shoot(time, hv_sact(0, 0))
time += dt
Shoot(time, hv_sact(0, 1))
Shoot(time, dg_sact(0, 0))
time += dt
Shoot(time, dg_sact(0, 1))
Shoot(time, hv_sact(1, 0))
time += dt
Shoot(time, hv_sact(1, 1))
Shoot(time, dg_sact(1, 0))
time += dt
Shoot(time, dg_sact(1, 1))
Shoot(time, hv_sact(2, 0))
time += dt
Shoot(time, hv_sact(2, 1))
Shoot(time, dg_sact(2, 0))
time += dt
Shoot(time, dg_sact(2, 1))
Shoot(time, hv_sact(3, 0))
time += dt
Shoot(time, hv_sact(3, 1))
Shoot(time, dg_sact(3, 0))
time += dt
Shoot(time, dg_sact(3, 1))
Loop(time)


#######
