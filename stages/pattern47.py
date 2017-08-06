from trggen import *
from .stages_commonlib import *


InitWalls([
    '######## ',
    '         ',
    ' ########',
    '         ',
    '######## ',
    '         ',
    ' ########',
    '         ',
    '######## ',
])

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Fast Missile', 'l2', P7),
    CreateUnit(1, 'Fast Missile', 'l6', P7),
    CreateUnit(1, 'Fast Missile', 'r4', P8),
    CreateUnit(1, 'Fast Missile', 'r8', P8),
])

Loop(23)
