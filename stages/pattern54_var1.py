from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Small Slow Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Small Slow Heavy Missile', 'u9', P7),
], 6)

# 빠른 미사일 (스카웃)

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
        CreateUnit(1, "Fast Missile", "u4", P7),
        CreateUnit(1, "Fast Missile", "u7", P7),
    ]
)

TimedStageTrigger(
    0,
    [
        Deaths(P8, AtLeast, 11, cv1),
        Deaths(P8, AtMost, 21, cv1),
    ],
    [
        CreateUnit(1, "Fast Missile", "u3", P7),
        CreateUnit(1, "Fast Missile", "u6", P7),
        CreateUnit(1, "Fast Missile", "u9", P7),
    ]
)

TimedStageTrigger(
    0,
    [
        Deaths(P8, AtLeast, 22, cv1),
        Deaths(P8, AtMost, 31, cv1),
    ],
    [
        CreateUnit(1, "Fast Missile", "u2", P7),
        CreateUnit(1, "Fast Missile", "u5", P7),
        CreateUnit(1, "Fast Missile", "u8", P7),
    ]
)

Loop(10)


# 느린 미사일 (배틀)

dt = 25
dm = 2
SelectCounter(1)
for i in range(dm):
    acts = []
    for j in range(i + 1, 10, dm):
        acts += [
            CreateUnit(1, 'Big Slow Missile', 'r%d' % j, P8),
            Order('Big Slow Missile', P8, 'r%d' % j, Move, 'l%d' % j),
        ]
    Shoot(dt * i, acts)

Loop(dt * dm)
AlwaysShoot(KillUnitAt(All, 'Big Slow Missile', 'l', P8))
