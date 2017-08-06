'''
Weird Fast Missile Set
'''

from trggen import *
from .stages_commonlib import *

InitNone()
SelectCounter(0)

AlwaysShoot([
    KillUnitAt(All, "Fast Missile", "r", P7),
    KillUnitAt(All, "Fast Missile", "l", P8),
])

###########################
dt = 15

Shoot(dt * 0, [
    CreateUnit(1, "Fast Missile", "ol1", P7),
    CreateUnit(1, "Fast Missile", "or3", P8),
    CreateUnit(1, "Fast Missile", "ol5", P7),
    CreateUnit(1, "Fast Missile", "or7", P8),
    CreateUnit(1, "Fast Missile", "ol9", P7),
    Order("Fast Missile", P7, "ol1", Move, "or2"),
    Order("Fast Missile", P8, "or3", Move, "ol4"),
    Order("Fast Missile", P7, "ol5", Move, "or6"),
    Order("Fast Missile", P8, "or7", Move, "ol8"),
    Order("Fast Missile", P7, "ol9", Move, "or10"),
])

Shoot(dt * 1, [
    CreateUnit(1, "Fast Missile", "ol2", P7),
    CreateUnit(1, "Fast Missile", "or4", P8),
    CreateUnit(1, "Fast Missile", "ol6", P7),
    CreateUnit(1, "Fast Missile", "or8", P8),
    CreateUnit(1, "Fast Missile", "ol10", P7),
    Order("Fast Missile", P7, "ol2", Move, "or1"),
    Order("Fast Missile", P8, "or4", Move, "ol3"),
    Order("Fast Missile", P7, "ol6", Move, "or5"),
    Order("Fast Missile", P8, "or8", Move, "ol7"),
    Order("Fast Missile", P7, "ol10", Move, "or9"),
])

Shoot(dt * 2, [
    CreateUnit(1, "Fast Missile", "ol1", P7),
    CreateUnit(1, "Fast Missile", "or3", P8),
    CreateUnit(1, "Fast Missile", "ol5", P7),
    CreateUnit(1, "Fast Missile", "or7", P8),
    CreateUnit(1, "Fast Missile", "ol9", P7),
    Order("Fast Missile", P7, "ol1", Move, "or3"),
    Order("Fast Missile", P8, "or3", Move, "ol5"),
    Order("Fast Missile", P7, "ol5", Move, "or7"),
    Order("Fast Missile", P8, "or7", Move, "ol9"),
    Order("Fast Missile", P7, "ol9", Move, "or10"),
])

Shoot(dt * 3, [
    CreateUnit(1, "Fast Missile", "ol2", P7),
    CreateUnit(1, "Fast Missile", "or4", P8),
    CreateUnit(1, "Fast Missile", "ol6", P7),
    CreateUnit(1, "Fast Missile", "or8", P8),
    CreateUnit(1, "Fast Missile", "ol10", P7),
    Order("Fast Missile", P7, "ol2", Move, "or1"),
    Order("Fast Missile", P8, "or4", Move, "ol2"),
    Order("Fast Missile", P7, "ol6", Move, "or4"),
    Order("Fast Missile", P8, "or8", Move, "ol6"),
    Order("Fast Missile", P7, "ol10", Move, "or8"),
])


Shoot(dt * 4, [
    CreateUnit(1, "Fast Missile", "ol1", P7),
    CreateUnit(1, "Fast Missile", "or3", P8),
    CreateUnit(1, "Fast Missile", "ol5", P7),
    CreateUnit(1, "Fast Missile", "or7", P8),
    CreateUnit(1, "Fast Missile", "ol9", P7),
    Order("Fast Missile", P7, "ol1", Move, "or4"),
    Order("Fast Missile", P8, "or3", Move, "ol6"),
    Order("Fast Missile", P7, "ol5", Move, "or8"),
    Order("Fast Missile", P8, "or7", Move, "ol10"),
    Order("Fast Missile", P7, "ol9", Move, "or10"),
])


Shoot(dt * 5, [
    CreateUnit(1, "Fast Missile", "ol2", P7),
    CreateUnit(1, "Fast Missile", "or4", P8),
    CreateUnit(1, "Fast Missile", "ol6", P7),
    CreateUnit(1, "Fast Missile", "or8", P8),
    CreateUnit(1, "Fast Missile", "ol10", P7),
    Order("Fast Missile", P7, "ol2", Move, "or1"),
    Order("Fast Missile", P8, "or4", Move, "ol1"),
    Order("Fast Missile", P7, "ol6", Move, "or3"),
    Order("Fast Missile", P8, "or8", Move, "ol5"),
    Order("Fast Missile", P7, "ol10", Move, "or7"),
])


Loop(dt * 6)
