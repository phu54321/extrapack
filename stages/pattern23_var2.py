'''
랜덤폭포수 - 반칸미사일
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
    SetSwitch("CustomSwitch2", Random),
    SetSwitch("CustomSwitch3", Random),
    SetSwitch("CustomSwitch4", Random),
    SetSwitch("CustomSwitch5", Random),
    SetDeaths(P8, SetTo, 0, "@CustomVariable1"),
])

cv1 = "@CustomVariable1"

TimedStageTrigger(0, Switch("CustomSwitch1", Set), SetDeaths(P8, Add, 1, cv1))
TimedStageTrigger(0, Switch("CustomSwitch2", Set), SetDeaths(P8, Add, 2, cv1))
TimedStageTrigger(0, Switch("CustomSwitch3", Set), SetDeaths(P8, Add, 4, cv1))
TimedStageTrigger(0, Switch("CustomSwitch4", Set), SetDeaths(P8, Add, 8, cv1))
TimedStageTrigger(0, Switch("CustomSwitch5", Set), SetDeaths(P8, Add, 16, cv1))

TimedStageTrigger(
    0,
    [
        Deaths(P8, AtMost, 10, cv1),
    ],
    [
        CreateUnit(1, "Fast Missile", "u1", P7),
        CreateUnit(1, "Odd Fast Missile", "ou3", P7),
        CreateUnit(1, "Fast Missile", "u4", P7),
        CreateUnit(1, "Odd Fast Missile", "ou6", P7),
        CreateUnit(1, "Fast Missile", "u7", P7),
        CreateUnit(1, "Odd Fast Missile", "ou9", P7),
    ]
)

TimedStageTrigger(
    0,
    [
        Deaths(P8, AtLeast, 11, cv1),
        Deaths(P8, AtMost, 21, cv1),
    ],
    [
        CreateUnit(1, "Odd Fast Missile", "ou2", P7),
        CreateUnit(1, "Fast Missile", "u3", P7),
        CreateUnit(1, "Odd Fast Missile", "ou5", P7),
        CreateUnit(1, "Fast Missile", "u6", P7),
        CreateUnit(1, "Odd Fast Missile", "ou8", P7),
        CreateUnit(1, "Fast Missile", "u9", P7),
        PreserveTrigger(),
    ]
)

TimedStageTrigger(
    0,
    [
        Deaths(P8, AtLeast, 22, cv1),
        Deaths(P8, AtMost, 31, cv1),
    ],
    [
        CreateUnit(1, "Odd Fast Missile", "ou1", P7),
        CreateUnit(1, "Fast Missile", "u2", P7),
        CreateUnit(1, "Odd Fast Missile", "ou4", P7),
        CreateUnit(1, "Fast Missile", "u5", P7),
        CreateUnit(1, "Odd Fast Missile", "ou7", P7),
        CreateUnit(1, "Fast Missile", "u8", P7),
        CreateUnit(1, "Odd Fast Missile", "ou10", P7),
        PreserveTrigger(),
    ]
)

Loop(8)
