'''
단순 폭피
'''

from trggen import *
from .stages_commonlib import *

InitWalls([
    '# # # # #',
    '         ',
    ' # # # # ',
    '         ',
    '# # # # #',
    '         ',
    ' # # # # ',
    '         ',
    '# # # # #',
])


#######

SelectCounter(0)

BombPattern(0, 'Protoss Archon', P8, [
    '@#@#@#@#@',
    '         ',
    '#@#@#@#@#',
    '         ',
    '@#@#@#@#@',
    '         ',
    '#@#@#@#@ ',
    '         ',
    '@#@#@#@#@',
])

BombPattern(15, 'Protoss Archon', P8, [
    '@ @ @ @ @',
    '#########',
    ' @ @ @ @ ',
    '#########',
    '@ @ @ @ @',
    '#########',
    ' @ @ @ @ ',
    '#########',
    '@ @ @ @ @',
])


Loop(30)
