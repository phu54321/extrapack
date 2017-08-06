'''
랜덤폭포수 - 작은미사일
'''

from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, "Heavy Missile", "u1", P7),
    CreateUnit(1, "Heavy Missile", "u2", P7),
    CreateUnit(1, "Heavy Missile", "u3", P7),
    CreateUnit(1, "Heavy Missile", "u4", P7),
    CreateUnit(1, "Heavy Missile", "u5", P7),
    CreateUnit(1, "Heavy Missile", "u6", P7),
    CreateUnit(1, "Heavy Missile", "u7", P7),
    CreateUnit(1, "Heavy Missile", "u8", P7),
    CreateUnit(1, "Heavy Missile", "u9", P7),
], delay=12)

SelectCounter(0)

Shoot(0, [
    SetSwitch("CustomSwitch1", Random),
])

TimedStageTrigger(
    0,
    [
        Switch("CustomSwitch1", Set),
    ],
    [
        CreateUnit(1, "Small Missile", "su1", P7),
        CreateUnit(1, "Small Missile", "su3", P7),
        CreateUnit(1, "Small Missile", "su5", P7),
        CreateUnit(1, "Small Missile", "su7", P7),
        CreateUnit(1, "Small Missile", "su9", P7),
        CreateUnit(1, "Small Missile", "su11", P7),
        CreateUnit(1, "Small Missile", "su13", P7),
        CreateUnit(1, "Small Missile", "su15", P7),
        CreateUnit(1, "Small Missile", "su17", P7),
    ]
)

TimedStageTrigger(
    0,
    [
        Switch("CustomSwitch1", Cleared),
    ],
    [
        CreateUnit(1, "Small Missile", "su2", P7),
        CreateUnit(1, "Small Missile", "su4", P7),
        CreateUnit(1, "Small Missile", "su6", P7),
        CreateUnit(1, "Small Missile", "su8", P7),
        CreateUnit(1, "Small Missile", "su10", P7),
        CreateUnit(1, "Small Missile", "su12", P7),
        CreateUnit(1, "Small Missile", "su14", P7),
        CreateUnit(1, "Small Missile", "su16", P7),
        CreateUnit(1, "Small Missile", "su18", P7),
    ]
)

Loop(12)
