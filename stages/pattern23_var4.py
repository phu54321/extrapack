'''
랜덤의폭포수
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
    SetDeaths(P8, SetTo, 2, "@CustomVariable3"),
], delay=4)

SelectCounter(0)

# 랜덤 스위치

Shoot(0, [
    SetSwitch("CustomSwitch1", Random),  # 움직일 방향
    SetSwitch("CustomSwitch2", Random),  # 타이머
    SetSwitch("CustomSwitch3", Random),  # 타이머
])

# 한쪽 방향으로 3번 연속으로 움직였으면 다른 방향으로 꺾는다.
TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 3, "@CustomVariable1"),
    SetSwitch("CustomSwitch1", Set),
)

TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 3, "@CustomVariable2"),
    SetSwitch("CustomSwitch1", Clear),
)

# 전체 방향을 움직인다.
TimedStageTrigger(
    0,
    Switch("CustomSwitch1", Cleared),
    SetDeaths(P8, Subtract, 1, "@CustomVariable3")
)

TimedStageTrigger(
    0,
    Switch("CustomSwitch1", Set),
    SetDeaths(P8, Add, 1, "@CustomVariable3")
)

# % 4

TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 0, "@CustomVariable3"),
    SetDeaths(P8, SetTo, 4, "@CustomVariable3")
)

TimedStageTrigger(
    0,
    Deaths(P8, Exactly, 5, "@CustomVariable3"),
    SetDeaths(P8, SetTo, 1, "@CustomVariable3")
)

for i in range(4):
    TimedStageTrigger(
        0,
        Deaths(P8, Exactly, i + 1, "@CustomVariable3"),
        [
            CreateUnit(1, "Small Missile", "su%d" % (j + 1), P7)
            for j in range(18) if j % 4 != i and (j // 2) % 2 == (i // 2)
        ] + [
            CreateUnit(1, "Fast Missile", "u%d" % (j + 1), P7)
            for j in range(9) if j % 2 != (i // 2)
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
