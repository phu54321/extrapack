'''
마이크로마우스
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '####### #',
    '     ## #',
    ' ###  #  ',
    '  # # # #',
    '# #   # #',
    '# # # #  ',
    '  #  ### ',
    '# ##     ',
    '# #######',
])

SelectCounter(0)

#######

looptm = 48

Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "u2", P7))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "d4", P8))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "u6", P7))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "d8", P8))

Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "r2", P8))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "l4", P7))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "r6", P8))
Shoot(60 % looptm, CreateUnit(1, "Fast Missile", "l8", P7))


Loop(looptm)
