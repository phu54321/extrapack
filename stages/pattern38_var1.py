'''
상하좌우 겹치기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Diagonal Missile RL', 'ur1', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur3', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur5', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur7', P7),
    CreateUnit(1, 'Diagonal Missile RL', 'ur9', P7),

    CreateUnit(1, 'Diagonal Missile RL', 'dl2', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl4', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl6', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl8', P8),
])

Loop(18)
