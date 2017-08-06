'''
4울 가디언버젼
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Small Slow Heavy Missile', 'u%d' % i, P7)
    for i in range(1, 10)
])

SelectCounter(0)

####


def ultra(d):
    player = {'u': P7, 'l': P7, 'd': P8, 'r': P8}[d]

    return [
        CreateUnit(1, "Small Slow Missile", "%s1" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s2" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s3" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s4" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s5" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s6" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s7" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s8" % d, player),
        CreateUnit(1, "Small Slow Missile", "%s9" % d, player),
    ]

timetb = [0, 25, 50, 75]

for i, d in enumerate(['d', 'l', 'u', 'r']):
    Shoot(timetb[i], [
        ultra(d),
    ])

Loop(100)
