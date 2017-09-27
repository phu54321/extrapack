"""
세이브코드 입력 부분입니다.
"""

from binascii import crc32

from eudplib import *

import savecode
import keypress

import config

digits = '2346789BCDFGHJKMPQRTVWXY'


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
    stage = EUDVariable()
    retryn = EUDVariable()
    nosavecode = Forward()  # 처음부터 시작
    found_match = Forward()  # 코드 찾음

    # 화면 끄기
    DoActions([
        [
            [
                SetCurrentPlayer(pl),
                RunAIScript('Turn OFF Shared Vision for Player 1'),
            ] for pl in range(6)
        ],
        SetMemory(0x51CE98, SetTo, 2),  # 터보시야
        SetMemory(0x6509A0, SetTo, 1),  # 터보트리거
    ])
    EUDDoEvents()  # 시야 가리기를 기다림

    # 만약 P1이 없으면 스킵 & 바로 변경
    if EUDIf()(f_playerexist(0) == 0):
        stage << 1
        retryn << 0
        EUDJump(nosavecode)
    EUDEndIf()

    # 유닛 생성 & 강제선택
    lu_ptr, lu_epd = f_dwepdread_epd(EPD(0x628438))
    DoActions([
        CreateUnit(1, 'Joystick', 'Anywhere', P1),
        SetMemory(0x6284E8, SetTo, lu_ptr),
    ])

    userpl = f_getuserplayerid()

    # 코드 입력용
    codestr = DBString('______')
    codecursor = EUDVariable()
    chs = EUDArray(6)
    codecursor << 0
    bw = EUDByteWriter()

    # 남은 시간
    remainingtime = EUDVariable()
    remainingtime << 240

    # 화면 출력용
    time_subcounter = EUDVariable()
    time_subcounter << 24
    need_update = EUDVariable()
    need_update << 1

    orderpos_table = [((i & 0xFF00) << 8 | (i & 0xFF)) + 0x04000400
                      for i in [crc32(bytes([i])) & 0xFFFF for i in range(24)]]
    assert len(set(orderpos_table)) == 24, 'Duplicate items'

    if EUDWhile()(remainingtime > 0):
        EUDBreakIf(f_playerexist(0) == 0)
        # 키인식 트리거
        ks = keypress.KeyState(*([ch for ch in digits]))
        ks.update()

        # 숫자 입력
        if EUDIf()([userpl == 0, Memory(0x6284E8, Exactly, lu_ptr)]):
            for digit, ch in enumerate(digits):
                if EUDIf()(ks.newlyKeyDown(ch)):
                    QueueGameCommand_RightClick(orderpos_table[digit])
                EUDEndIf()
        EUDEndIf()

        # 공유조건 인식
        for digit, ch in enumerate(digits):
            if EUDIf()(Deaths(
                lu_epd + 0x16,
                Exactly,
                orderpos_table[digit],
                0)
            ):
                chs[codecursor] = digit
                bw.seekoffset(codestr.GetStringMemoryAddr() + codecursor)
                bw.writebyte(ord(ch))
                bw.flushdword()
                codecursor += 1
                need_update << 1
            EUDEndIf()

        DoActions([
            MoveUnit(1, 'Joystick', P1, 'Anywhere', 'Anywhere'),
            CenterView('Anywhere'),
            SetMemory(0x6509A0, SetTo, 0),
        ])

        # 키 인식
        if EUDIf()(codecursor == 6):  # 4자리가 다 채워짐
            ic = (
                chs[0] * (24 ** 5) +
                chs[1] * (24 ** 4) +
                chs[2] * (24 ** 3) +
                chs[3] * (24 ** 2) +
                chs[4] * (24 ** 1) +
                chs[5] * (24 ** 0)
            )
            curstage = EUDVariable()
            curretryn = EUDVariable()
            curdf = EUDVariable()

            euda_cursnl = EUDArray(config.stagenarr)

            curdf << 2
            if EUDWhileNot()(curdf == 0xFFFFFFFF):
                curstage << euda_cursnl[curdf] - 1
                # curstage == 0 : 1스테이지 : 코드 체크를 하지 않는다.
                if EUDWhileNot()(curstage == 0):
                    curretryn << 0
                    if EUDWhile()(curretryn <= 10):
                        if EUDIf()(savecode.f_gethash(
                                0, curdf, curstage, curretryn) == ic):
                            # match
                            diff << curdf
                            stage << curstage + 1
                            retryn << curretryn
                            EUDJump(found_match)
                        EUDEndIf()
                        curretryn += 1
                    EUDEndWhile()
                    curstage += 0xFFFFFFFF
                EUDEndWhile()
                curdf -= 1
            EUDEndWhile()

            # No match
            codecursor << 0
            bw.seekoffset(codestr.GetStringMemoryAddr())
            bw.writebyte(b'_'[0])
            bw.writebyte(b'_'[0])
            bw.writebyte(b'_'[0])
            bw.writebyte(b'_'[0])
            bw.writebyte(b'_'[0])
            bw.writebyte(b'_'[0])
            bw.flushdword()
        EUDEndIf()

        # 카운트다운
        Trigger(
            remainingtime % 24 == 0,
            [
                need_update.SetNumber(1),
                [
                    [
                        SetCurrentPlayer(pl),
                        PlayWAV('sound\glue\countdown.wav'),  # 카운트다운
                    ] for pl in range(6)
                ]
            ]
        )

        # 화면출력
        DoActions([
            SetCurrentPlayer(userpl),
            CenterView('Anywhere'),
            SetMemory(0x6509A0, SetTo, 0),  # EUD터보
        ])

        if EUDIf()(need_update == 1):
            userstr = DBString(1024)
            if EUDIf()(userpl == 0):
                f_dbstr_print(userstr, SCMD2Text('''\









    <13><04>키보드로 세이브 코드를 입력하세요.
    <13><05>'''), codestr, SCMD2Text('''
    <13><03>'''), (remainingtime + 23) // 24, SCMD2Text('''초 남았습니다.
    '''))

            if EUDElse()():
                f_dbstr_print(userstr, SCMD2Text('''\









    <13><08>P1<04>의 코드 입력을 기다리고 있습니다...
    <13><05>'''), codestr, SCMD2Text('''
    <13><03>'''), remainingtime // 24, SCMD2Text('''초 남았습니다.
    '''))
            EUDEndIf()

            DoActions(userstr.GetDisplayAction())

            need_update << 0

        EUDEndIf()

        EUDDoEvents()

        remainingtime -= 1
    EUDEndWhile()

    # 매치 못찾음
    stage << 1
    retryn << 0
    EUDJump(nosavecode)

    #
    #
    # -----------
    # -----------
    #
    #

    # 매치 찾았을경우
    execend = Forward()

    found_match << NextTrigger()
    usaddr = EUDVariable()
    usaddr << userstr.GetStringMemoryAddr()
    diffstr = DBString(1024)

    if EUDIf()(diff == 0):
        f_dbstr_print(diffstr, 'Easy')
    if EUDElseIf()(diff == 1):
        f_dbstr_print(diffstr, 'Normal')
    if EUDElseIf()(diff == 2):
        f_dbstr_print(diffstr, 'Hard')
    EUDEndIf()

    usaddr << f_dbstr_print(usaddr, SCMD2Text('''\









<13><1D>'''), diffstr, ' \x02', stage, SCMD2Text('''탄<04>부터 시작합니다.
<13><04>세이브 횟수 : '''), retryn)

    if EUDIf()(retryn == 20):
        usaddr << f_dbstr_print(usaddr, '번 이상')
    EUDEndIf()

    usaddr = f_dbstr_print(usaddr, SCMD2Text('''
<13><04>'''), codestr, SCMD2Text('''
<13><05>배경음을 Ctrl + M키로 꺼주세요.
'''))
    DoActions([
        SetCurrentPlayer(userpl),
        userstr.GetDisplayAction(),
        RemoveUnit('Joystick', P1),
        RemoveUnitAt(All, '(any unit)', 'lvselbox', AllPlayers),
        PlayWAV('sound\glue\scorefillend.wav'),
    ])
    delay(24 * 3)
    EUDJump(execend)

    # 아닌 경우
    nosavecode << NextTrigger()
    DoActions([
        SetCurrentPlayer(userpl),
        DisplayExtText(SCMD2Text('''\









<13><04>인식된 세이브코드가 없습니다.

<13><05>배경음을 Ctrl + M키로 꺼주세요.
''')),
        RemoveUnit('Joystick', P1),
        PlayWAV('sound\glue\scorefillend.wav'),
    ])

    delay(24 * 3)

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

    if EUDWhile()(diff == config.diffn):
        DoActions([
            SetCurrentPlayer(userpl),
            DisplayExtText(SCMD2Text('''\





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
                DisplayExtText(SCMD2Text('''\











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
                DisplayExtText(SCMD2Text('''\











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
                DisplayExtText(SCMD2Text('''\











<13><03>Hard <04>난이도로 플레이합니다.
<13><05>사실 노멀과 비슷함'''))
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

    EUDJump(execend)

    # 진짜 끝
    execend << NextTrigger()
    DoActions(DisplayExtText('\n' * 13))
    return diff, stage, retryn
