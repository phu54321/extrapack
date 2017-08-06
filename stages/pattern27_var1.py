'''
크로스해치 + 대각선
possible
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

#######

crosshatch_action = [
    lambda i: CreateUnit(1, "Odd Fast Missile", "ou%d" % i, P7),
    lambda i: CreateUnit(1, "Odd Fast Missile", "ol%d" % (11 - i), P7),
    lambda i: CreateUnit(1, "Odd Fast Missile", "od%d" % (11 - i), P8),
    lambda i: CreateUnit(1, "Odd Fast Missile", "or%d" % i, P8),
]

#### Crosshatch pattern

SelectCounter(0)
for j in range(4):
    for i in range(5):
        Shoot(60 * j + 4 * i, [
            crosshatch_action[j](1),
            crosshatch_action[j](3),
            crosshatch_action[j](5),
            crosshatch_action[j](7),
            crosshatch_action[j](9),

            crosshatch_action[j-3](1),
            crosshatch_action[j-3](3),
            crosshatch_action[j-3](5),
            crosshatch_action[j-3](7),
            crosshatch_action[j-3](9),
        ])

Loop(60 * 4)

# Diagonal Missile

SelectCounter(1)

Shoot(0, [
    CreateUnit(1, "Diagonal Missile RL", "ur1", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur3", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur5", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur7", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur9", P7),
])

Shoot(18, [
    CreateUnit(1, "Diagonal Missile RL", "ur2", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur4", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur6", P7),
    CreateUnit(1, "Diagonal Missile RL", "ur8", P7),
])

Loop(36)
