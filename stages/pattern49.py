from trggen import *
from .stages_commonlib import *


InitWalls([
    '######## ',
    '       # ',
    ' ##### # ',
    ' #   # # ',
    ' # # # # ',
    ' # #   # ',
    ' # ##### ',
    ' #       ',
    ' ########',
])

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Odd Fast Missile', 'od2', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od4', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od6', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od8', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od10', P8),
])

Shoot(14, [
    CreateUnit(1, 'Odd Fast Missile', 'od1', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od3', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od5', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od7', P8),
    CreateUnit(1, 'Odd Fast Missile', 'od9', P8),
])

Loop(28)
