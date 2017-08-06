'''
간단한 폭탄피하기
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()

SelectCounter(0)

BombPattern(0, 'Flare', P8, [
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
    '# # # # #',
])

BombPattern(18, 'Flare', P8, [
    '#########',
    '         ',
    '#########',
    '         ',
    '#########',
    '         ',
    '#########',
    '         ',
    '#########',
])

Loop(36)
