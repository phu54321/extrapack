'''
4울 가디언버젼
'''

from trggen import *
from condblock import CondBlock
from .stages_commonlib import *

dt = 1
mCount = 13

xUnit = "@CustomVariable5"
yUnit = "@CustomVariable6"


def GetVStorage(i):
    player = [P7, P8, P9, P10, P11][i % 5]
    unit = [
        "@CustomVariable1",
        "@CustomVariable2",
        "@CustomVariable3",
    ][i // 5]
    return player, unit


InitNone([
    CreateUnit(25, "Recaller", "arbiter", P8),
    SetSwitch("CustomSwitch2", Clear)
])

####

AlwaysShoot([
    KillUnitAt(All, "Small Missile", "u", P8),
    KillUnitAt(All, "Small Missile", "l", P8),
    KillUnitAt(All, "Small Missile", "d", P8),
    KillUnitAt(All, "Small Missile", "r", P8),
    KillUnitAt(All, "Small Missile", "arbiter", P8),
])

SelectCounter(0)

lSrc = ParseLocation("cloc1")
lDst = ParseLocation("cloc2")


with OnTime(0):
    pSrc, uSrc = GetVStorage(0)
    pDst, uDst = GetVStorage(mCount - 1)

    # Queue 이동
    for i in range(1, mCount):
        p1, u1 = GetVStorage(i)
        p2, u2 = GetVStorage(i - 1)
        CopyDeaths(p1, u1, p2, u2)

    with CondBlock(P8, Switch("CustomSwitch2", Set)):
        # Create unit & missile in desired position
        CopyDeaths(pSrc, uSrc, P8, xUnit)
        DoActions(SetDeaths(P8, SetTo, 0, yUnit))

        for j in range(15, -1, -1):  # Split XY
            Trigger(
                P8,
                Deaths(P8, AtLeast, 2 ** (j + 16), xUnit),
                [
                    SetDeaths(P8, Subtract, 2 ** (j + 16), xUnit),
                    SetDeaths(P8, Add, 2 ** j, yUnit),
                    PreserveTrigger()
                ]
            )

        # Create Unit there!
        CopyDeaths(
            P8, xUnit,

            EPD(0x58DC60 + (lSrc - 1) * 20 + 0x0), 0,
            EPD(0x58DC60 + (lSrc - 1) * 20 + 0x8), 0,

            EPD(0x58DC60 + (lDst - 1) * 20 + 0x0), 0,
            EPD(0x58DC60 + (lDst - 1) * 20 + 0x8), 0,
        )

        CopyDeaths(
            P8, yUnit,
            EPD(0x58DC60 + (lSrc - 1) * 20 + 0x4), 0,
            EPD(0x58DC60 + (lSrc - 1) * 20 + 0xC), 0,

            EPD(0x58DC60 + (lDst - 1) * 20 + 0x4), 0,
            EPD(0x58DC60 + (lDst - 1) * 20 + 0xC), 0,
        )

        xy0 = 1024 - 32 * 15
        xy1 = 1024 + 32 * 15

        # 1사분면은 밑으로
        Trigger(P8, [
            Deaths(P8, AtMost, 1023, xUnit),
            Deaths(P8, AtMost, 1023, yUnit),
        ], [
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x4, SetTo, xy1),
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0xC, SetTo, xy1),
            PreserveTrigger(),
        ])

        # 2사분면은 오른쪽으로
        Trigger(P8, [
            Deaths(P8, AtMost, 1023, xUnit),
            Deaths(P8, AtLeast, 1024, yUnit),
        ], [
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x0, SetTo, xy1),
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x8, SetTo, xy1),
            PreserveTrigger(),
        ])

        # 3사분면은 위로
        Trigger(P8, [
            Deaths(P8, AtLeast, 1024, xUnit),
            Deaths(P8, AtLeast, 1024, yUnit),
        ], [
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x4, SetTo, xy0),
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0xC, SetTo, xy0),
            PreserveTrigger(),
        ])

        # 4사분면은 왼쪽으로
        Trigger(P8, [
            Deaths(P8, AtLeast, 1024, xUnit),
            Deaths(P8, AtMost, 1023, yUnit),
        ], [
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x0, SetTo, xy0),
            SetMemory(0x58DC60 + (lDst - 1) * 20 + 0x8, SetTo, xy0),
            PreserveTrigger(),
        ])

        # 미사일을 날린다!
        Trigger(
            players=P8,
            actions=[
                CreateUnit(1, "Small Missile", lSrc, P8),
                Order("Small Missile", P8, lSrc, Move, lDst),
                PreserveTrigger(),
            ],
        )

    # 새로 미사일을 만들 장소의 x, y좌표를 정한다.
    # 좌표는 (9 * 64) ^ 2 안에서 만들면 됩니다.
    for i, unit in enumerate([xUnit, yUnit]):
        xy0 = 1024 - 32 * 9
        basemem = 0x58DC60 + (lSrc - 1) * 20 + i * 4
        DoActions([
            SetDeaths(P8, SetTo, xy0, unit),
            SetMemory(basemem + 0, SetTo, xy0),
            SetMemory(basemem + 8, SetTo, xy0),
        ])

        for i in range(9):
            DoActions(SetSwitch("CustomSwitch1", Random))
            Trigger(P8, Switch("CustomSwitch1", Set), [
                SetDeaths(P8, Add, 2 ** i, unit),
                SetMemory(basemem + 0, Add, 2 ** i),
                SetMemory(basemem + 8, Add, 2 ** i),
                PreserveTrigger()
            ])

        for i in range(6):
            DoActions(SetSwitch("CustomSwitch1", Random))
            Trigger(P8, Switch("CustomSwitch1", Set), [
                SetDeaths(P8, Add, 2 ** i, unit),
                SetMemory(basemem + 0, Add, 2 ** i),
                SetMemory(basemem + 8, Add, 2 ** i),
                PreserveTrigger()
            ])

    DoActions([
        RunAIScriptAt('Recall Here', lSrc),
    ])

    # Store to variable
    DoActions(SetDeaths(pDst, SetTo, 0, uDst))
    for i in range(15, -1, -1):
        Trigger(P8, Deaths(P8, AtLeast, 2 ** i, xUnit), [
            SetDeaths(P8, Subtract, 2 ** i, xUnit),
            SetDeaths(pDst, Add, 2 ** i, uDst),
            PreserveTrigger()
        ])

        Trigger(P8, Deaths(P8, AtLeast, 2 ** i, yUnit), [
            SetDeaths(P8, Subtract, 2 ** i, yUnit),
            SetDeaths(pDst, Add, 2 ** (i + 16), uDst),
            PreserveTrigger()
        ])

    DoActions([
        SetDeaths(P8, Add, 1, "@CustomVariable4"),
    ])
    Trigger(
        P8,
        Deaths(P8, Exactly, mCount, "@CustomVariable4"),
        [
            SetSwitch("CustomSwitch2", Set),
            PreserveTrigger()
        ]
    )

Loop(dt)
