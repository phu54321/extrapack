from trggen import *


Trigger( # Force1 동맹
    players=[Force2],
    conditions=[
        Always(),
    ],
    actions=[
        SetAllianceStatus(Force1, Ally),
    ],
)

Trigger( # 미니맵 업데이트
    players=[Force1],
    actions=[
        MinimapPing("minimapping"),
        PreserveTrigger(),
    ],
)


Trigger( # 무적 & P12삭제 & 라바삭제
    players=[AllPlayers],
    conditions=[
        Always(),
    ],
    actions=[
        SetInvincibility(Enable, "(any unit)", AllPlayers, "Anywhere"),
        KillUnit("(men)", P12),
        KillUnit("Bunker", P12),
        RemoveUnit("Zerg Larva", Force1),
        PreserveTrigger(),
    ],
)

'''
Trigger(
    players=[Force1],
    conditions=Accumulate(CurrentPlayer, AtMost, 29, Gas),
    actions=SetResources(CurrentPlayer, SetTo, 30, Gas),
    flag=preserved
)
'''