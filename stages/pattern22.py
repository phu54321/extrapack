'''
4울
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove()
SelectCounter(0)

####


def ultra(d):
    player = {'u': P7, 'l': P7, 'd': P8, 'r': P8}[d]

    return [
        CreateUnit(1, "Fast Missile", "%s1" % d, player),
        CreateUnit(1, "Fast Missile", "%s2" % d, player),
        CreateUnit(1, "Fast Missile", "%s3" % d, player),
        CreateUnit(1, "Fast Missile", "%s4" % d, player),
        CreateUnit(1, "Fast Missile", "%s5" % d, player),
        CreateUnit(1, "Fast Missile", "%s6" % d, player),
        CreateUnit(1, "Fast Missile", "%s7" % d, player),
        CreateUnit(1, "Fast Missile", "%s8" % d, player),
        CreateUnit(1, "Fast Missile", "%s9" % d, player),
    ]

timetb = [0, 30, 30, 60]

for i, d in enumerate(['d', 'l', 'r', 'u']):
    Shoot(timetb[i], [
        ultra(d),
    ])

Loop(80)
