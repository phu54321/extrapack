'''
TimeLock (Easy)
'''

from trggen import *
from .stages_commonlib import *


InitNormalMissileMove()

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, 'Diagonal Missile RL', 'dl1', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl3', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl5', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl7', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl9', P8),
])

Shoot(10, [
    CreateUnit(1, 'Diagonal Missile RL', 'dl2', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl4', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl6', P8),
    CreateUnit(1, 'Diagonal Missile RL', 'dl8', P8),
])

Loop(20)


# -------
dt = 3

SelectCounter(1)
BombPattern(0 * dt, 'Protoss Archon', P7, [
    '#        ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
])

BombPattern(1 * dt, 'Protoss Archon', P7, [
    '# #      ',
    ' #       ',
    '#        ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
])

BombPattern(2 * dt, 'Protoss Archon', P7, [
    '  # #    ',
    ' # #     ',
    '# #      ',
    ' #       ',
    '#        ',
    '         ',
    '         ',
    '         ',
    '         ',
])

BombPattern(3 * dt, 'Protoss Archon', P7, [
    '    # #  ',
    '   # #   ',
    '  # #    ',
    ' # #     ',
    '# #      ',
    ' #       ',
    '#        ',
    '         ',
    '         ',
])

BombPattern(4 * dt, 'Protoss Archon', P7, [
    '      # #',
    '     # # ',
    '    # #  ',
    '   # #   ',
    '  # #    ',
    ' # #     ',
    '# #      ',
    ' #       ',
    '#        ',
])

BombPattern(5 * dt, 'Protoss Archon', P7, [
    '        #',
    '       # ',
    '      # #',
    '     # # ',
    '    # #  ',
    '   # #   ',
    '  # #    ',
    ' # #     ',
    '# #      ',
])

BombPattern(6 * dt, 'Protoss Archon', P7, [
    '         ',
    '         ',
    '        #',
    '       # ',
    '      # #',
    '     # # ',
    '    # #  ',
    '   # #   ',
    '  # #    ',
])

BombPattern(7 * dt, 'Protoss Archon', P7, [
    '         ',
    '         ',
    '         ',
    '         ',
    '        #',
    '       # ',
    '      # #',
    '     # # ',
    '    # #  ',
])

BombPattern(8 * dt, 'Protoss Archon', P7, [
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '        #',
    '       # ',
    '      # #',
])

BombPattern(9 * dt, 'Protoss Archon', P7, [
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '         ',
    '        #',
])

Loop(10 * dt)
