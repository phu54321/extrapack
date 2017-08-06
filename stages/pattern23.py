'''
이중랜덤의폭포수
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
])

TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 2, "@CustomVariable1"),
    SetSwitch("CustomSwitch1", Set),
)

TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 2, "@CustomVariable2"),
    SetSwitch("CustomSwitch1", Clear),
)


TimedStageTrigger(
    0,
    Switch("CustomSwitch1", Set),
    [
        CreateUnit(1, "Fast Missile", "u1", P7),
        CreateUnit(1, "Fast Missile", "u3", P7),
        CreateUnit(1, "Fast Missile", "u5", P7),
        CreateUnit(1, "Fast Missile", "u7", P7),
        CreateUnit(1, "Fast Missile", "u9", P7),
        SetDeaths(P8, SetTo, 0, "@CustomVariable1"),
        SetDeaths(P8, Add, 1, "@CustomVariable2"),
    ]
)

TimedStageTrigger(
    0,
    Switch("CustomSwitch1", Cleared),
    [
        CreateUnit(1, "Fast Missile", "u2", P7),
        CreateUnit(1, "Fast Missile", "u4", P7),
        CreateUnit(1, "Fast Missile", "u6", P7),
        CreateUnit(1, "Fast Missile", "u8", P7),
        SetDeaths(P8, SetTo, 0, "@CustomVariable2"),
        SetDeaths(P8, Add, 1, "@CustomVariable1"),
    ]
)

for i in range(1, 4):
    TimedStageTrigger(
        0,
        [
            Switch("CustomSwitch2", Set if ((i // 1) % 2) == 0 else Cleared),
            Switch("CustomSwitch3", Set if ((i // 2) % 2) == 0 else Cleared),
        ],
        SetDeaths(P8, SetTo, i * 2, "@PatternSubCounter1"),
    )

Loop(10)
