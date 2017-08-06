from trggen import *


Trigger(  # 런방정상화 (비활성화)
    players=[Force1],
    conditions=[
        Deaths(-111927, AtMost, 4, "Terran Marine"),
        Never(),
    ],
    actions=[
        SetDeaths(-111927, SetTo, 5, "Terran Marine"),
        SetDeaths(-111928, SetTo, 5, "Terran Marine"),
        SetDeaths(-111929, SetTo, 5, "Terran Marine"),
        SetDeaths(-111930, SetTo, 5, "Terran Marine"),
        SetDeaths(-111931, SetTo, 5, "Terran Marine"),
        SetDeaths(-111932, SetTo, 5, "Terran Marine"),
        SetDeaths(-111933, SetTo, 5, "Terran Marine"),
        PreserveTrigger(),
    ],
)

Trigger(  # 런방잡기 (비활성화)
    players=[Force1],
    conditions=[
        Deaths(-111927, AtMost, 4, "Terran Marine"),
        Never(),
    ],
    actions=[
        DisplayText("\x04This map cannot be run under reduced lantancy.", 4),
        Defeat(),
    ],
)

#######

Trigger(  # 노런방은 파괴한다
    players=[Force1],
    conditions=[
        Deaths(-111927, Exactly, 5, "Terran Marine"),
    ],
    actions=[
        DisplayText("\x03[참고사항] \x04이 팩은 런방 플레이를 권장합니다.", 4),
        PlayWAV('sound\Misc\Transmission.wav')
    ],
)
