'''
상하좌우 겹치기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Diagonal Missile LR', 'ul1', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul3', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul5', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul7', P7),
    CreateUnit(1, 'Diagonal Missile LR', 'ul9', P7),

    CreateUnit(1, 'Diagonal Missile RL', 'ur1', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur3', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur5', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur7', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur9', P7),

    CreateUnit(1, 'Diagonal Missile LR', 'dr2', P8),
    CreateUnit(1, 'Diagonal Missile LR', 'dr4', P8),
    CreateUnit(1, 'Diagonal Missile LR', 'dr6', P8),
    CreateUnit(1, 'Diagonal Missile LR', 'dr8', P8),

    CreateUnit(1, 'Diagonal Missile RL', 'dl2', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl4', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl6', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl8', P8),
])

Loop(18)
