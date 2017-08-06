from eudplib import *
import savecode
from loadcode import checkcode
from timer import (
    f_istimerhit,
    f_starttimer,
)
from stages.stages_commonlib import patternname_list
import config
import os

if __name__ == '__main__':
    raise RuntimeError('Run main.py')


# Make list of patterns
pndbs = [0] * (max(patternname_list.keys()) + 1)
for k, v in patternname_list.items():
    pndbs[k] = Db(u2b(v) + b'\0')
pndb_arr = EUDArray(pndbs)


@EUDFunc
def f_bgmloop():
    # BGM Loop
    if EUDIf()(f_istimerhit() == 1):
        f_starttimer(48000)
        for player in range(8):
            DoActions([
                SetCurrentPlayer(player),
                PlayWAV('staredit\\wav\\bgmmono.wav')
            ])
    EUDEndIf()


@EUDFunc
def f_getstringaddr(strid):
    br = EUDByteReader()
    strsection_addr = f_dwread_epd(EPD(0x5993D4))
    br.seekoffset(strsection_addr + 2 * strid)
    ch1 = br.readbyte()
    ch2 = br.readbyte()
    stroffset = 256 * ch2 + ch1
    soffset = strsection_addr + stroffset
    return soffset


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
tryn = EUDVariable()
userpl = EUDVariable()


@EUDFunc
def main():
    f_initextstr()

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

    # checkauthor()  # 리플레이 방지 & 방장인식

    # 코드 인식
    initialstage = EUDVariable()

    if not config.debugmode:
        DoActions([
            [
                SetCurrentPlayer(player),
                # MuteUnitSpeech(),
                DisplayExtText(SCMD2Text('''\
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
        SetVariables([difficulty, initialstage, tryn], checkcode())
    else:
        difficulty << config.difficulty
        initialstage << config.initialstage
        tryn << 0
        DoActions(RemoveUnitAt(All, '(any unit)', 'lvselbox', AllPlayers))

    proceeded_flag = EUDVariable()
    proceeded_flag << 0  # 탄을 하나라도 깨면 이게 1이 되면서 tryn이 +1된다.

    # Initialization trigger
    DoActions([
        # Resize unit dimension
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
        # SetDeaths(-122781, SetTo, 42, 0),
    ])

    if config.slowmode:
        Trigger(
            Memory(0x006D0F14, Exactly, 0),
            SetDeaths(-122781, SetTo, 84, 0),
        )

    # 세이브 횟수 표기
    saven_strid = EncodeString('\x04라이프 \x03| \x04세이브 횟수 : 00번 이상')
    soffset = f_getstringaddr(saven_strid)
    soffset = f_dbstr_print(soffset, '\x04라이프 \x03| \x04세이브 횟수 : ')
    soffset = f_dbstr_adddw(soffset, tryn)
    if EUDIf()(tryn == 20):  # 20세이브 이상부터는 세이브코드를 따로 발급하지 않음
        soffset << f_dbstr_print(soffset, '번 이상')
    EUDEndIf()

    # Init bgm loop
    f_starttimer(0)

    if config.debugmode:
        initiallife = 150
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
        LeaderBoardResources(Gas, saven_strid),
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
            # 재시도 횟수 업데이트.
            if EUDIf()(proceeded_flag == 0):  # 처음 스테이지
                proceeded_flag << 1
            if EUDElseIf()(proceeded_flag == 1):  # 스테이지를 처음 클리어.
                proceeded_flag << 2
                tryn << tryn + 1
                Trigger(tryn == 21, tryn.SetNumber(20))
            EUDEndIf()

            code = savecode.f_gethash(userpl, difficulty, stage, tryn)

            euda_cursnl = EUDArray(config.stagenarr)

            if EUDIfNot()(stage == euda_cursnl[difficulty]):  # 막탄 아닌 경우
                # 스트링 변형
                target_strid = EncodeString('#' * 512)  # 512byte inside str.
                soffset = f_getstringaddr(target_strid)

                # print names
                soffset = f_dbstr_print(soffset, '\x13\x02')

                if EUDIf()(difficulty == 0):
                    soffset << f_dbstr_print(soffset, 'Easy ')
                if EUDElseIf()(difficulty == 1):
                    soffset << f_dbstr_print(soffset, 'Normal ')
                if EUDElseIf()(difficulty == 2):
                    soffset << f_dbstr_print(soffset, 'Hard ')
                EUDEndIf()

                soffset << f_dbstr_print(soffset, stage + 1, ''' : \x04''')
                soffset << f_dbstr_addstr(
                    soffset,
                    pndb_arr[config.diffn * stage + difficulty]
                )
                soffset << f_dbstr_print(soffset, '\n\x13\x05세이브 코드 : 000000')

                if EUDIf()(stage == 0):
                    f_dbstr_print(soffset - 6, '없음')
                if EUDElse()():
                    savecode.f_writebase24str(code, soffset - 6)
                EUDEndIf()

                # 텍스트 출력
                pl = EUDVariable()
                pl << 0
                if EUDWhile()(pl <= 5):
                    f_setcurpl(pl)

                    DoActions([
                        DisplayText(target_strid),
                        SetMissionObjectives(target_strid)
                    ])
                    pl += 1
                EUDEndWhile()
            EUDEndIf()
            # 끗
            DoActions(SetSwitch('UpdateStageCode', Clear))
        EUDEndIf()

        # 통과속성 다시 활성화
        unitptr, unitepd = f_dwepdread_epd(EPD(0x628430))
        if EUDWhileNot()(unitptr == 0):
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
            playerID = f_dwbreak(f_dwread_epd(unitepd + 0x4C // 4))[2]
            Trigger(
                [
                    Switch('LockMissileP7', Set),
                    playerID.Exactly(EncodePlayer(P7)),
                ],
                [
                    SetDeaths(unitepd + 0x38 // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x3C // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x40 // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x44 // 4, SetTo, 0, 0),
                ]
            )

            Trigger(
                [
                    Switch('LockMissileP8', Set),
                    playerID.Exactly(EncodePlayer(P8)),
                ],
                [
                    SetDeaths(unitepd + 0x38 // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x3C // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x40 // 4, SetTo, 0, 0),
                    SetDeaths(unitepd + 0x44 // 4, SetTo, 0, 0),
                ]
            )

            EUDSetContinuePoint()
            SetVariables([unitptr, unitepd], f_dwepdread_epd(unitepd + 4 // 4))
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
SaveMap('Missile pack [ext] v2.1.scx', main)

# Apply mpaq
# os.system('mpaq temp2.scx "Missile pack [ext] v2.1.scx"')
os.remove('temp.scx')
# os.remove('temp2.scx')
