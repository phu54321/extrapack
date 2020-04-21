from eudplib import *
from loadcode import checkcode
from timer import (
    f_istimerhit,
    f_starttimer,
)
from stages.stages_commonlib import patternname_list
import config
import os
from checkauthor import checkauthor

if __name__ == '__main__':
    raise RuntimeError('Run main.py')


# Make list of patterns


@EUDFunc
def f_bgmloop():
    # BGM Loop
    if EUDIf()(f_istimerhit() == 1):
        f_starttimer(48000)
        for player in range(8):
            DoActions([
                SetCurrentPlayer(player),
                PlayWAV('staredit\\wav\\bgmmono.ogg')
            ])
    EUDEndIf()


def delay(framen):
    EUDLoopN()(framen)
    DoActions([
        RemoveUnit("Zerg Larva", Force1),
        SetMemory(0x6509A0, SetTo, 0),  # 터보트리거
    ])
    EUDDoEvents()
    EUDEndLoopN()


stage = EUDVariable()
difficulty = EUDVariable()
userpl = EUDVariable()


@EUDFunc
def main():
    if EUDIf()(Memory(0x57F0B4, Exactly, 0)):
        DoActions([
            [
                SetCurrentPlayer(player),
                DisplayText('\x05싱글플레이를 하실 수 없습니다.'),
                Draw()
            ] for player in range(6)
        ])

        if EUDInfLoop()():
            EUDDoEvents()
        EUDEndInfLoop()
    EUDEndIf()

    checkauthor()
    # if config.debugmode:
    #     checkauthor()

    # 코드 인식
    initialstage = EUDVariable()

    if not config.debugmode:
        DoActions([
            [
                SetCurrentPlayer(player),
                # MuteUnitSpeech(),
                DisplayText(SCMD2Text('''\
    <13><0F><04>Missile pack <02>[Extra]<04>

    <13><05>Created by cpy3001

    ''')),
            ] for player in range(6)])

        if EUDLoopN()(3000 // 48):
            DoActions([
                CenterView('Anywhere'),
                SetMemory(0x6509A0, SetTo, 0),
            ])
            EUDDoEvents()
        EUDEndLoopN()
        SetVariables([difficulty, initialstage], checkcode())
        MPQAddFile(
            "staredit\\wav\\bgmmono.ogg",
            open("bgmmono.ogg", "rb").read()
        )
    else:
        difficulty << config.difficulty
        initialstage << config.initialstage
        DoActions(RemoveUnitAt(All, '(any unit)', 'lvselbox', AllPlayers))

    # Initialization trigger
    DoActions([
        [
            [
                SetCurrentPlayer(pl),
                RunAIScript('Turn ON Shared Vision for Player 8'),
            ] for pl in range(6)
        ],        # Resize unit dimension
        # 머신샵
        SetMemory(0x6617C8 + 120 * 8 + 0, SetTo, 0x001F001F),
        SetMemory(0x6617C8 + 120 * 8 + 4, SetTo, 0x001F001F),

        # 라자갈 (커세어)
        SetMemory(0x6617C8 + 98 * 8 + 0, SetTo, 0x00010001),
        SetMemory(0x6617C8 + 98 * 8 + 4, SetTo, 0x00010001),

        # 다크아콘
        SetMemory(0x6617C8 + 63 * 8 + 0, SetTo, 0x00140014),
        SetMemory(0x6617C8 + 63 * 8 + 4, SetTo, 0x00130013),

        # 아콘
        SetMemory(0x6617C8 + 68 * 8 + 0, SetTo, 0x00140014),
        SetMemory(0x6617C8 + 68 * 8 + 4, SetTo, 0x00130013),

        # 스카웃
        # 12 00 11 00 11 00 10 00
        SetMemory(0x6617C8 + 70 * 8 + 0, SetTo, 0x00120012),  # 그냥
        SetMemory(0x6617C8 + 70 * 8 + 4, SetTo, 0x00110011),
        SetMemory(0x6617C8 + 80 * 8 + 0, SetTo, 0x00120012),  # mojo
        SetMemory(0x6617C8 + 80 * 8 + 4, SetTo, 0x00110011),
        SetMemory(0x6617C8 + 88 * 8 + 0, SetTo, 0x00120012),  # Artanis
        SetMemory(0x6617C8 + 88 * 8 + 4, SetTo, 0x00110011),

        # Make units unclickable
        SetMemory(0x66C150 + 292, SetTo, 0x00000001),  # Machine shop
        SetMemory(0x66C150 + 188, SetTo, 0x00000000),  # Pylon
        SetMemory(0x66C150 + 140, SetTo, 0x00000000),  # Scout & Heros
        SetMemory(0x66C150 + 242, SetTo, 0x00000000),  # Wraith & Heros
        SetMemory(0x66C150 + 24, SetTo, 0x00000000),  # Guardian
        SetMemory(0x66C150 + 936, SetTo, 0x00000101),  # Valkyrie
        SetMemory(0x66C150 + 216, SetTo, 0x00000101),  # Battlecruiser
        SetMemory(0x66C150 + 132, SetTo, 0x00000000),  # Archon
        SetMemory(0x66C150 + 924, SetTo, 0x00000000),  # Dark Archon
        SetMemory(0x66C150 + 40, SetTo, 0x00000000),  # Overlord
        SetMemory(0x66C150 + 16, SetTo, 0x00000000),  # Drone
        SetMemory(0x66C150 + 0, SetTo, 0x00000000),  # Scourge

        # Set turn radius to minimal (1)
        # 6C9E20 : Flingy.dat - turn radius
        SetMemory(0x6C9E20 + 0, SetTo, 0x00281B7F),  # Scourge (0) -> 127
        SetMemory(0x6C9E20 + 4, SetTo, 0x2800281B),  # Guardian (7)
        SetMemory(0x6C9E20 + 40, SetTo, 0x28282828),  # Scout (43)
        SetMemory(0x6C9E20 + 80, SetTo, 0x0D0D2828),  # Wraith (80)
        SetMemory(0x6C9E20 + 188, SetTo, 0x282828),  # Valkyrie & Corsair
        SetMemory(0x6C9E20 + 68, SetTo, 0x28280000),  # Battlecruiser (70)

        # 게임속도 Fastest로 고정
        SetDeaths(-122781, SetTo, 42, 0),
    ])
    # Init bgm loop
    f_starttimer(0)

    if config.debugmode:
        initiallife = 100
    else:
        initiallife = 30

    DoActions([
        [(
            SetCurrentPlayer(player),
        ) for player in range(6)],

        SetMemory(0x51CE98, SetTo, 2),  # 터보시야
        SetDeaths(P8, SetTo, initialstage - 1, "@PatternSelector"),
        SetDeaths(P8, SetTo, difficulty, "@Difficulty"),
        SetDeaths(P8, SetTo, 2, "@GameState"),
        SetResources(Force1, SetTo, initiallife - 20, Gas),
        LeaderBoardResources(Gas, '\x04라이프 \x03'),
        LeaderBoardComputerPlayers(Disable),
        SetMemory(0x51CE98, SetTo, 2),  # 터보시야
        SetMemory(0x6509A0, SetTo, 1),
    ])

    EUDDoEvents()

    # Repulse map handle : 공중유닛끼리 밀림 현상 방지용
    reph_epd = f_epdread_epd(EPD(0x6D5CD8))

    userpl << f_getuserplayerid()

    if EUDInfLoop()():
        f_bgmloop()
        RunTrigTrigger()

        # Debugmode → Slow mode를 활성화
        if config.debugmode and config.slowmode:
            if EUDIf()(Bring(Force1, AtLeast, 1, "Dodger", "slow")):
                if EUDIf()(Deaths(-122781, Exactly, 42, 0)):
                    DoActions([
                        MoveUnit(All, "Dodger", Force1, "slow", "StageStart"),
                        SetDeaths(-122781, SetTo, 84, 0),
                    ])
                if EUDElse()():
                    DoActions([
                        MoveUnit(All, "Dodger", Force1, "slow", "StageStart"),
                        SetDeaths(-122781, SetTo, 42, 0),
                    ])
                EUDEndIf()
            EUDEndIf()


        # 코드 계산 시작
        stage << f_dwread_epd(12 * EncodeUnit('@PatternSelector') + 7) - 1
        difficulty << f_dwread_epd(12 * EncodeUnit('@Difficulty') + 7)

        # 패배 처리
        if EUDIf()(Deaths(P8, Exactly, 4, "@GameState")):
            # 세이브코드 요약
            losetext()

            # 패배 처리
            for pl in range(6):
                DoActions([
                    SetCurrentPlayer(pl),
                    Defeat()
                ])
            EUDInfLoop()()
            EUDDoEvents()
            EUDEndInfLoop()

        # 승리 처리
        if EUDElseIf()(Deaths(P8, Exactly, 5, "@GameState")):
            victorytext()

            DoActions([
                [
                    SetCurrentPlayer(pl),
                    SetAllianceStatus(Force1, AlliedVictory)
                ] for pl in range(6)
            ])

            DoActions([
                [
                    SetCurrentPlayer(pl),
                    Victory()
                ] for pl in range(6)
            ])

            EUDInfLoop()()
            EUDDoEvents()
            EUDEndInfLoop()
        EUDEndIf()

        # 코드 재계산
        if EUDIf()(Switch('UpdateStageCode', Set)):
            euda_cursnl = EUDArray(config.stagenarr)

            if EUDIfNot()(stage == euda_cursnl[difficulty]):  # 막탄 아닌 경우
                f_setcurpl(f_getuserplayerid())
                # 스트링 변형
                for k in patternname_list.keys():
                    targetStage = k // config.diffn
                    targetDifficulty = k % config.diffn
                    diffstr = ['Easy', 'Normal', 'Hard'][targetDifficulty]
                    target_string = (
                        "\x13\x02%s %d : \x04%s\n" %
                        (diffstr, targetStage + 1, patternname_list[k])
                    )
                    if EUDIf()([
                        stage == targetStage,
                        difficulty == targetDifficulty
                    ]):
                        DoActions(DisplayText(target_string))
                    EUDEndIf()
            EUDEndIf()
            # 끗
            DoActions(SetSwitch('UpdateStageCode', Clear))
        EUDEndIf()

        # 통과속성 다시 활성화
        unitepd = EUDVariable()
        unitepd << EPD(0x59CCA8)
        if EUDWhile()(unitepd <= EPD(0x59CCA8) + 336 // 4 * 1699):
            # 존재하지 않는 유닛은 특수처리
            if EUDIf()(MemoryEPD(unitepd + 0xC // 4, Exactly, 0)):
                DoActions(SetMemoryEPD(unitepd + 0x64 // 4, SetTo, 0))
                EUDContinue()
            EUDEndIf()

            # 통과속성 적용 안할 유닛들 제외
            unitType = f_dwread_epd(unitepd + 0x64 // 4)
            EUDContinueIf(unitType == EncodeUnit('Block'))
            EUDContinueIf(unitType == EncodeUnit('NarrowBlock'))
            EUDContinueIf(unitType == EncodeUnit('Bunker'))
            EUDContinueIf(unitType == EncodeUnit('Dodger'))

            # statusFlag 설정
            statusFlag = f_dwread_epd(unitepd + 0xDC // 4)
            statusFlag = f_bitor(statusFlag, 0x200000)  # Gathering
            f_dwwrite_epd(unitepd + 0xDC // 4, statusFlag)

            # 멈춤 설정
            # /*0x034*/ u32           flingyTopSpeed;
            # /*0x060*/ u32         shieldPoints;
            playerID = f_dwbreak(f_dwread_epd(unitepd + 0x4C // 4))[2]
            c = EUDVariable()
            c << 0
            if EUDIf()(playerID.Exactly(EncodePlayer(P7))):
                c << 2
                Trigger(Switch('LockMissileP7', Set), c.SetNumber(1))
            if EUDElseIf()(playerID.Exactly(EncodePlayer(P8))):
                c << 2
                Trigger(Switch('LockMissileP8', Set), c.SetNumber(1))
            EUDEndIf()

            if EUDIf()(c == 1):
                oldTopSpeed = f_dwread_epd(unitepd + 0x34 // 4)
                Trigger(
                    oldTopSpeed != 100,
                    [
                        SetMemoryEPD(unitepd + 0x34 // 4, SetTo, 100),
                        SetMemoryEPD(unitepd + 0x64 // 4, Add, 65536 * oldTopSpeed),
                    ]
                )
            if EUDElseIf()(c == 2):
                cachedTopV = f_dwbreak(f_dwread_epd(unitepd + 0x64 // 4))[1]
                Trigger(
                    cachedTopV != 0,
                    [
                        SetMemoryEPD(unitepd + 0x34 // 4, SetTo, cachedTopV),
                        SetMemoryEPD(unitepd + 0x64 // 4, Subtract, 65536 * cachedTopV),
                    ]
                )
            EUDEndIf()

            EUDSetContinuePoint()
            unitepd += 336 // 4
        EUDEndWhile()

        #
        # Repulse Map를 계속 0으로 설정 -> 공중유닛끼리 밀림 현상 방지
        m = EUDVariable()
        m << reph_epd
        t = EUDLightVariable()
        t << 29244 // 4

        if EUDWhile()(t >= 1):
            DoActions([
                t.SubtractNumber(1),
                SetDeaths(m, SetTo, 0, 0),
                m.AddNumber(1)
            ])
        EUDEndWhile()
        #

        # 락다운 처리
        if EUDIf()(Switch('LockDrone', Set)):
            for player in range(6):
                Trigger(
                    Bring(player, AtLeast, 1, 'Dodger', 'ground'),
                    [
                        MoveLocation('ptrace', 'Dodger', player, 'Anywhere'),
                        CreateUnit(1, 'Kakaru', 'ptrace', P8),
                        KillUnitAt(All, 'Kakaru', 'ptrace', P8),
                        MoveUnit(All, 'Dodger', player, 'ptrace', 'ptrace'),
                    ]
                )
            DoActions(KillUnit('Kakaru', P8))
        EUDEndIf()

        # 터보트리거 등등
        DoActions(SetMemory(0x6509A0, SetTo, 0))
        EUDDoEvents()
    EUDEndInfLoop()


# ----------
#
#  Game ending
#
# ----------


def dptext(text):
    DoActions([
        SetCurrentPlayer(userpl),
        DisplayText(text)
    ])


@EUDFunc
def losetext():
    if EUDLoopN()(2):
        DoActions([
            SetCurrentPlayer(userpl),
            DisplayText('\x13\x08^^^^^^^^^^ 마지막 탄 정보 ^^^^^^^^^^'),
            DisplayText('#' * 512),  # 패턴 정보 등등
            DisplayText('\x13\x08^^^^^^^^^^ 마지막 탄 정보 ^^^^^^^^^^'),
        ])
        delay(24 * 3)
    EUDEndLoopN()
    dptext('\n' * 13)


def victorytext():
    dptext(SCMD2Text('''\
<13><1E>====================================
<13><02>Final Stage : <04>엔딩
<13><05>세이브 코드 : ??????
<13><1E>===================================='''))
    delay(24 * 4)

    dptext(SCMD2Text('''\








<13><1E>====================================
<13><02>제작 계기/방향
<13><04>eudplib/trggen 데모맵
<13><04>미사일팩의 장르화 연구
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\







<13><1E>====================================    　
<13><02>아이디어를 얻은 맵들
<13><04>Level up bound
<13><04>Extreme pack 1.xG
<13><04>미사일피하기 MsPack
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\




<13><1E>====================================
<13><02>Special Thanks To
<13><04>Qwe  Lead  Love  Eud[fx]
<13><04>rhwkplayer1  Uin`

<13><04>http://cafe.naver.com/missilewarfare
<13><1E>===================================='''))

    delay(24 * 5)

    dptext(SCMD2Text('''\






<13><1E>====================================
<13><04>플레이해주셔서 감사합니다.

<13>ㄴㅓㅈㅣㅎㅏ
<13>ㄷㅃㅓㅅㄴ
<13>ㅗㄹㄷㅏ

<13><04>개발기간 : 2014.02.24 ~ 2015.07.15
<13><1E>===================================='''))

    delay(24 * 5)


LoadMap('temp.scx')
CompressPayload(True)
SaveMap(f'Missile pack [ext] {config.version}.scx', main)
os.remove('temp.scx')
