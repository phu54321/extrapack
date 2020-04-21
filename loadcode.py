"""
세이브코드 입력 부분입니다.
"""

from eudplib import *
import config


def delay(framen):
    if EUDLoopN()(framen):
        DoActions([
            SetCurrentPlayer(f_getuserplayerid()),
            CenterView('Anywhere'),
            SetMemory(0x6509A0, SetTo, 0),
        ])
        EUDDoEvents()
    EUDEndLoopN()


def checkcode():
    diff = EUDVariable()
    stage = EUDVariable(1)

    # 난이도 선택
    DoActions([
        [
            [
                SetCurrentPlayer(pl),
                RunAIScript('Turn ON Shared Vision for Player 1'),
            ] for pl in range(6)
        ],
        SetInvincibility(Enable, "(any unit)", AllPlayers, "Anywhere"),
        SetMemory(0x51CE98, SetTo, 2),  # 터보시야
        SetMemory(0x6509A0, SetTo, 1),  # 터보트리거
    ])
    EUDDoEvents()

    # 난이도를 선택할 플레이어를 설정
    pl_selector = EUDVariable()
    pl_selector << 0
    diff << config.diffn
    userpl = f_getuserplayerid()

    if EUDWhile()(diff == config.diffn):
        DoActions([
            SetCurrentPlayer(userpl),
            DisplayText(SCMD2Text('''\





<13><04>난이도를 선택하세요.







''')),
        ])

        if EUDInfLoop()():
            EUDBreakIfNot(f_playerexist(pl_selector) == 0)
            pl_selector += 1
        EUDEndInfLoop()

        if EUDIf()(Bring(pl_selector, Exactly, 0,
                         'Level Selector', 'Anywhere')):
            DoActions([
                RemoveUnit('Level Selector', AllPlayers),
                CreateUnit(
                    1, 'Level Selector', 'lvsel_selector', pl_selector),
                SetInvincibility(Enable, "(any unit)", AllPlayers, "Anywhere"),
            ])
        EUDEndIf()

        #######################################################################

        Trigger(
            Bring(pl_selector, AtLeast, 1,
                  'Level Selector', 'lvsel_easy'),
            [
                diff.SetNumber(0),
                SetCurrentPlayer(userpl),
                DisplayText(SCMD2Text('''\











<13><03>Easy <04>난이도로 플레이합니다.
<13><05>공방용으로 적합한 난이도'''))
            ]
        )

        #######################################################################

        Trigger(
            Bring(pl_selector, AtLeast, 1, 'Level Selector', 'lvsel_normal'),
            [
                diff.SetNumber(1),
                SetCurrentPlayer(userpl),
                DisplayText(SCMD2Text('''\











<13><03>Normal <04>난이도로 플레이합니다.
<13><05>고수들 전용 난이도'''))
            ]
        )

        #######################################################################

        Trigger(
            Bring(pl_selector, AtLeast, 1, 'Level Selector', 'lvsel_hard'),
            [
                diff.SetNumber(2),
                SetCurrentPlayer(userpl),
                DisplayText(SCMD2Text('''\











<13><03>Hard <04>난이도로 플레이합니다.
<13><05>어려울수도 쉬울수도'''))
            ]
        )

        #######################################################################

        DoActions(SetMemory(0x6509A0, SetTo, 1))
        EUDDoEvents()
    EUDEndWhile()

    DoActions([
        RemoveUnitAt(All, '(any unit)', 'lvselbox', AllPlayers)
    ])

    delay(24 * 3)
    DoActions(DisplayText('\n' * 13))
    return diff, stage
