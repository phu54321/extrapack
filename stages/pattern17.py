'''
가디언 사이드의 진헌곡
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Small Slow Heavy Missile", "u1", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u2", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u3", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u4", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u5", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u6", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u7", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u8", P7),
    CreateUnit(1, "Small Slow Heavy Missile", "u9", P7),
])

SelectCounter(0)

Shoot(0, [
    CreateUnit(1, "Big Slow Missile", "l1", P7),
    CreateUnit(1, "Big Slow Missile", "l3", P7),
    CreateUnit(1, "Big Slow Missile", "l5", P7),
    CreateUnit(1, "Big Slow Missile", "l7", P7),
    CreateUnit(1, "Big Slow Missile", "l9", P7),

    CreateUnit(1, "Big Slow Missile", "r2", P8),
    CreateUnit(1, "Big Slow Missile", "r4", P8),
    CreateUnit(1, "Big Slow Missile", "r6", P8),
    CreateUnit(1, "Big Slow Missile", "r8", P8),

    Order('(men)', P7, "l1", Move, "r1"),
    Order('(men)', P7, "l3", Move, "r3"),
    Order('(men)', P7, "l5", Move, "r5"),
    Order('(men)', P7, "l7", Move, "r7"),
    Order('(men)', P7, "l9", Move, "r9"),

    Order('(men)', P8, "r2", Move, "l2"),
    Order('(men)', P8, "r4", Move, "l4"),
    Order('(men)', P8, "r6", Move, "l6"),
    Order('(men)', P8, "r8", Move, "l8"),

    KillUnitAt(All, '(men)', 'r', P7),
    KillUnitAt(All, '(men)', 'l', P8),
])

Loop(30)
