from trggen import *


# 무브로케이션 & 해처리 인식 준비
Trigger(
    players=[Force1],
    conditions=[
        Always(),
    ],
    actions=[
        MoveLocation("ptrace", "Dodger", CurrentPlayer, "Board"),
        MoveLocation("htrace", "Bunker", CurrentPlayer, "Board"),
        SetSwitch("HasHatchery", Set),
        PreserveTrigger(),
    ],
)

# 해처리 인식
Trigger(
    players=[Force1],
    conditions=[
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "Anywhere")
    ],
    actions=[
        SetSwitch("HasHatchery", Clear),
        PreserveTrigger()
    ]
)

# 드론 - 미사일 충돌
Trigger(
    players=[Force1],
    conditions=[
        Bring(Force2, AtLeast, 1, "(men)", "ptrace"),
        Bring(CurrentPlayer, AtLeast, 1, "(men)", "ptrace"),
        Bring(CurrentPlayer, Exactly, 0, "(men)", "StageStart"),
        Bring(CurrentPlayer, Exactly, 0, "(men)", "StageEnd"),
        Deaths(P8, Exactly, 1, "@GameState"),
    ],
    actions=[
        KillUnitAt(All, "Dodger", "ptrace", CurrentPlayer),
        PreserveTrigger(),
    ],
)

# 건설중 해처리 - 헤비미사일 충돌
Trigger(
    players=[Force1],
    conditions=[
        Bring(Force2, AtLeast, 1, "Heavy Missile", "htrace"),
        Switch("HasHatchery", Set),
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "StageStart"),
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "StageEnd"),
        Deaths(P8, Exactly, 1, "@GameState"),
    ],
    actions=[
        KillUnitAt(All, "Bunker", "htrace", CurrentPlayer),
        PreserveTrigger(),
    ],
)


# 건설중 해처리 - 헤비미사일 충돌
Trigger(
    players=[Force1],
    conditions=[
        Bring(Force2, AtLeast, 1, "Small Slow Heavy Missile", "htrace"),
        Switch("HasHatchery", Set),
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "StageStart"),
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "StageEnd"),
        Deaths(P8, Exactly, 1, "@GameState"),
    ],
    actions=[
        KillUnitAt(All, "Bunker", "htrace", CurrentPlayer),
        PreserveTrigger(),
    ],
)

# 해처리 완성시 터트리기
Trigger(
    players=[Force1],
    conditions=[
        Bring(CurrentPlayer, AtLeast, 1, "Bunker", "Board"),
    ],
    actions=[
        RemoveUnitAt(All, "Bunker", "Board", CurrentPlayer),
        DisplayText("\x03[Error]\x04 해처리를 완성할 수 없습니다.", 4),
        PreserveTrigger(),
    ],
)

# 부활
Trigger(
    players=[Force1],
    conditions=[
        Bring(CurrentPlayer, Exactly, 0, "Dodger", "Board"),
        Bring(CurrentPlayer, AtMost, 0, "Bunker", "Board"),
        Accumulate(CurrentPlayer, AtLeast, 1, Gas),
        Deaths(P8, Exactly, 1, "@GameState"),
    ],
    actions=[
        CreateUnit(1, "Dodger", "StageStart", CurrentPlayer),
        PlayWAV('sound\Misc\OutOfGas.wav'),
        DisplayText("\x04다시 해보세요.", 4),
        SetResources(CurrentPlayer, Subtract, 1, Gas),
        PreserveTrigger(),
    ],
)


# 150개 이상 라이프는 제거
Trigger(
    players=[Force1],
    conditions=[
        Accumulate(CurrentPlayer, AtLeast, 101, Gas),
    ],
    actions=[
        PlayWAV('sound\Misc\Transmission.wav'),
        DisplayText("\x04최대 라이프수 100에 맞췄습니다.", 4),
        SetResources(CurrentPlayer, SetTo, 100, Gas),
        PreserveTrigger(),
    ],
)
