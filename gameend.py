from trggen import *
import config


Trigger(  # 카운터 다달면 실패
    players=[Force1],
    conditions=[
        Accumulate(Force1, Exactly, 0, Gas),
        Bring(Force1, Exactly, 0, "Dodger", 'Anywhere'),
        Bring(Force1, AtMost, 0, 'Bunker', 'Anywhere'),
        Deaths(P8, Exactly, 1, "@GameState"),
    ],
    actions=[
        KillUnit("(any unit)", AllPlayers),
        SetDeaths(P8, SetTo, 4, "@GameState"),
    ],
)


for diff, stagen in enumerate(config.stagenarr):
    Trigger(  # 탄 전부 클리어 -> 승리
        players=[Force1],
        conditions=[
            Deaths(P8, Exactly, diff, '@Difficulty'),
            Deaths(P8, Exactly, stagen + 1, "@PatternSelector"),
        ],
        actions=[
            SetDeaths(P8, SetTo, 5, "@GameState"),
        ],
    )

'''
CREDIT LIST
===================================================

mipi_apple
mipi_june
mipi_student
mipi_ruin
mipi_plusclass

'''
