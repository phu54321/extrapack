from trggen import *


# 스테이지 관련
Trigger(  # 패턴 타이머
    players=[P8],
    actions=[
        SetDeaths(P8, Add, 1, "@PatternSubCounter1"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter2"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter3"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter4"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter5"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter6"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter7"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter8"),
        SetDeaths(P8, Add, 1, "@PatternSubCounter9"),
        PreserveTrigger(),
    ],
)

Trigger(
    players=[Force1],
    conditions=[
        Command(Force1, Exactly, 0, 'Skip'),
        Command(P8, AtLeast, 1, 'Skip Chance')
    ],
    actions=[
        CreateUnit(1, 'Skip', 'skipswitch', CurrentPlayer),
        PreserveTrigger()
    ]
)


Trigger(  # 탄 클리어 처리 요청
    players=[Force1],
    conditions=[
        Bring(CurrentPlayer, AtLeast, 1, "(men)", "StageEnd"),
        # Bring(CurrentPlayer, AtLeast, 1, "(men)", "ground"),  # For stage pic
    ],
    actions=[
        SetDeaths(P8, SetTo, 2, "@GameState"),
        PreserveTrigger(),
    ],
)


Trigger(  # 탄 클리어 처리 요청
    players=[Force1],
    conditions=[
        Bring(CurrentPlayer, AtLeast, 1, "Skipped", "skipswitch"),
        # Bring(CurrentPlayer, AtLeast, 1, "(men)", "ground"),  # For stage pic
    ],
    actions=[
        SetDeaths(P8, SetTo, 2, "@GameState"),
        KillUnitAt(All, 'Skipped', 'skipswitch', CurrentPlayer),
        KillUnitAt(1, 'Skip Chance', 'skipchamber', P8),
        PreserveTrigger(),
    ],
)


Trigger(  # 탄 클리어 처리
    players=[P8],
    conditions=[
        Deaths(P8, Exactly, 2, "@GameState"),
    ],
    actions=[
        SetDeaths(P8, Add, 1, "@PatternSelector"),
        SetDeaths(P8, SetTo, 0, "@GameState"),

        SetDeaths(P8, SetTo, 0, "@PatternSubCounter1"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter2"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter3"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter4"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter5"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter6"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter7"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter8"),
        SetDeaths(P8, SetTo, 0, "@PatternSubCounter9"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable1"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable2"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable3"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable4"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable5"),
        SetDeaths(P8, SetTo, 0, "@CustomVariable6"),
        SetSwitch("CustomSwitch1", Clear),
        SetSwitch("CustomSwitch2", Clear),
        SetSwitch("CustomSwitch3", Clear),
        SetSwitch("CustomSwitch4", Clear),
        SetSwitch("CustomSwitch5", Clear),
        SetSwitch("CustomSwitch6", Clear),
        SetSwitch("LockDrone", Clear),
        SetSwitch('LockMissileP7', Clear),
        SetSwitch('LockMissileP8', Clear),
        SetSwitch("NormalMissileMove", Clear),

        KillUnitAt(All, "(men)", "Anywhere", Force2),
        KillUnitAt(All, "Block", "Anywhere", AllPlayers),
        KillUnitAt(All, "NarrowBlock", "Anywhere", AllPlayers),
        RemoveUnit("Dodger", Force1),
        RemoveUnit("Bunker", Force1),
        CreateUnit(1, "Dodger", "StageStart", Force1),
        SetResources(Force1, Add, 15, Gas),

        SetSwitch('UpdateStageCode', Set),
        PreserveTrigger(),
    ],
)
