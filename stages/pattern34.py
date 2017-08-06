'''
무한반복 - 혼돈
손꼬이는 패턴
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

Shoot(0, [
    CreateUnit(1, 'Odd Fast Missile', 'ou1', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ou3', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ou5', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ou7', P7),

    CreateUnit(1, 'Odd Fast Missile', 'ol2', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ol4', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ol6', P7),
    CreateUnit(1, 'Odd Fast Missile', 'ol8', P7),

    CreateUnit(1, 'Odd Fast Missile', 'od2', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od4', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od6', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od8', P8),

    CreateUnit(1, 'Odd Fast Missile', 'or1', P8),
    CreateUnit(1, 'Odd Fast Missile', 'or3', P8),
    CreateUnit(1, 'Odd Fast Missile', 'or5', P8),
    CreateUnit(1, 'Odd Fast Missile', 'or7', P8),
])

Loop(30)
