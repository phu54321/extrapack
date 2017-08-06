# 위에서 랜덤 + 밑에서 계단
''' EASY '''


from trggen import *
from .stages_commonlib import *

InitNormalMissileMove([
    CreateUnit(1, 'Heavy Missile', 'u1', P7),
    CreateUnit(1, 'Heavy Missile', 'u2', P7),
    CreateUnit(1, 'Heavy Missile', 'u3', P7),
    CreateUnit(1, 'Heavy Missile', 'u4', P7),
    CreateUnit(1, 'Heavy Missile', 'u5', P7),
    CreateUnit(1, 'Heavy Missile', 'u6', P7),
    CreateUnit(1, 'Heavy Missile', 'u7', P7),
    CreateUnit(1, 'Heavy Missile', 'u8', P7),
    CreateUnit(1, 'Heavy Missile', 'u9', P7),
], 6)


# -------


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

# 0 ~ 31 : 32개 가짓수. 평균 5개씩
# 0 ~ 4
# 5 ~ 9
# 10 ~ 15
# 16 ~ 20
# 21 ~ 25
# 26 ~ 31

msel = [
    [
        CreateUnit(1, "Missile", "u1", P7),
        CreateUnit(1, "Missile", "u4", P7),
        CreateUnit(1, "Missile", "u7", P7),
    ],
    [
        CreateUnit(1, "Missile", "u3", P7),
        CreateUnit(1, "Missile", "u6", P7),
        CreateUnit(1, "Missile", "u9", P7),
    ],
    [
        CreateUnit(1, "Missile", "u2", P7),
        CreateUnit(1, "Missile", "u5", P7),
        CreateUnit(1, "Missile", "u8", P7),
    ]
]


def tstarr(s, e, msels):
    TimedStageTrigger(
        0,
        [
            Deaths(P8, AtMost, e, cv1),
            Deaths(P8, AtLeast, s, cv1)
        ],
        msel[msels[0]]
    )

    TimedStageTrigger(
        13,
        [
            Deaths(P8, AtMost, e, cv1),
            Deaths(P8, AtLeast, s, cv1)
        ],
        msel[msels[1]]
    )

    TimedStageTrigger(
        26,
        [
            Deaths(P8, AtMost, e, cv1),
            Deaths(P8, AtLeast, s, cv1)
        ],
        msel[msels[2]]
    )

# 0 ~ 4
# 5 ~ 9
# 10 ~ 15
# 16 ~ 20
# 21 ~ 25
# 26 ~ 31
tstarr(0,  4, [0, 1, 2])
tstarr(5,  9, [0, 2, 1])
tstarr(10, 15, [1, 0, 2])
tstarr(16, 20, [1, 2, 0])
tstarr(21, 25, [2, 0, 1])
tstarr(26, 31, [2, 1, 0])

Loop(39)


# -------


SelectCounter(1)
Shoot(0, [
    CreateUnit(1, 'Heavy Missile', 'd1', P8),
    CreateUnit(1, 'Heavy Missile', 'd4', P8),
    CreateUnit(1, 'Heavy Missile', 'd7', P8),
])
Shoot(11, [
    CreateUnit(1, 'Heavy Missile', 'd2', P8),
    CreateUnit(1, 'Heavy Missile', 'd5', P8),
    CreateUnit(1, 'Heavy Missile', 'd8', P8),
])
Shoot(22, [
    CreateUnit(1, 'Heavy Missile', 'd3', P8),
    CreateUnit(1, 'Heavy Missile', 'd6', P8),
    CreateUnit(1, 'Heavy Missile', 'd9', P8),
])
Loop(33)
