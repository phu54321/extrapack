'''
블랙홀 회오리
'''

from trggen import *
from .stages_commonlib import *

InitNone([
    # Simple trap
    CreateUnit(1, "Heavy Missile", "u1", P7),
    CreateUnit(1, "Heavy Missile", "u2", P7),
    CreateUnit(1, "Heavy Missile", "u3", P7),
    CreateUnit(1, "Heavy Missile", "u4", P7),
    CreateUnit(1, "Heavy Missile", "u5", P7),
    CreateUnit(1, "Heavy Missile", "u6", P7),
    CreateUnit(1, "Heavy Missile", "u7", P7),
    Order("Heavy Missile", P7, "u1", Move, "d1"),
    Order("Heavy Missile", P7, "u2", Move, "d2"),
    Order("Heavy Missile", P7, "u3", Move, "d3"),
    Order("Heavy Missile", P7, "u4", Move, "d4"),
    Order("Heavy Missile", P7, "u5", Move, "d5"),
    Order("Heavy Missile", P7, "u6", Move, "d6"),
    Order("Heavy Missile", P7, "u7", Move, "d7"),

    # Missile creator
    CreateUnit(1, "Train Type 1", "qul", P7),
    CreateUnit(1, "Train Type 1", "qur", P7),
    CreateUnit(1, "Train Type 1", "qdr", P7),
    CreateUnit(1, "Train Type 1", "qdl", P7),
    MoveLocation("customtrace1", "Train Type 1", P7, "qul"),
    MoveLocation("customtrace2", "Train Type 1", P7, "qur"),
    MoveLocation("customtrace3", "Train Type 1", P7, "qdr"),
    MoveLocation("customtrace4", "Train Type 1", P7, "qdl"),
])


####

# Simple trap catcher
AlwaysShoot([
    KillUnitAt(All, "Heavy Missile", "d", P7),
])

# Move location
AlwaysShoot([
    MoveLocation("customtrace1", "Train Type 1", P7, "customtrace1"),
    MoveLocation("customtrace2", "Train Type 1", P7, "customtrace2"),
    MoveLocation("customtrace3", "Train Type 1", P7, "customtrace3"),
    MoveLocation("customtrace4", "Train Type 1", P7, "customtrace4"),
    CreateUnit(1, "Protoss Archon", "c44", P7),
    KillUnitAt(All, "Protoss Archon", "c44", P7),
])

# Missile creator move
AlwaysShoot([
    Order("Train Type 1", P7, "qul", Move, "qur"),
    Order("Train Type 1", P7, "qur", Move, "qdr"),
    Order("Train Type 1", P7, "qdr", Move, "qdl"),
    Order("Train Type 1", P7, "qdl", Move, "qul"),
])

####

SelectCounter(0)
Shoot(0, [
    CreateUnit(1, "Small Missile", "customtrace1", P7),
    CreateUnit(1, "Small Missile", "customtrace2", P7),
    CreateUnit(1, "Small Missile", "customtrace3", P7),
    CreateUnit(1, "Small Missile", "customtrace4", P7),
    Order("Small Missile", P7, "Anywhere", Move, "c44"),
    KillUnitAt(All, "Small Missile", "c44", P7),
])
Loop(3)


SelectCounter(1)
Shoot(0, [
    Order("Dodger", Force1, "ground", Move, "c44"),
])
Loop(2)
