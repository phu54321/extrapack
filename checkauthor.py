from eudplib import *

cd_br = EUDByteReader()
cd_bw = EUDByteReader()

cpy3001_db = Db(b'cpy3001\0')
mipi_copy_db = Db(b'Mipi_Copy\0')


@EUDFunc
def f_strcmp(s1, s2):
    br1 = EUDByteReader()
    br2 = EUDByteReader()
    ret = EUDVariable()
    ret << 0

    br1.seekoffset(s1)
    br2.seekoffset(s2)

    if EUDInfLoop()():
        ch1 = br1.readbyte()
        ch2 = br2.readbyte()
        EUDBreakIfNot(ch1 == ch2)

        EUDIf()(ch1 == 0)
        ret << 1
        EUDBreak()
        EUDEndIf()
    EUDEndInfLoop()
    return ret


def checkauthor():
    # 임시 : 리플레이 방지

    if EUDIf()(Memory(0x006D0F14, AtLeast, 1)):
        for pl in range(8):
            f_setcurpl(pl)
            DoActions([
                DisplayText('Replay blocked'),
                Defeat()
            ])

        EUDInfLoop()()
        EUDDoEvents()
        EUDEndInfLoop()
    EUDEndIf()


    # ID Check
    allowexec = EUDVariable()

    # 제작자가 있는가?
    allowexec << 0
    for player in range(8):
        Trigger(
            f_strcmp(0x57EEEB + 36 * player, cpy3001_db) == 1,
            allowexec.SetNumber(1)
        )

        Trigger(
            f_strcmp(0x57EEEB + 36 * player, mipi_copy_db) == 1,
            allowexec.SetNumber(1)
        )

    if EUDIf()(allowexec == 0):
        DoActions([
            DisplayExtText('버그테스트 버젼 실행시엔 제작자가 필요합니다.'),
            KillUnit('(any unit)', AllPlayers),
            SetMemory(0x6509A0, SetTo, 3000),
            Defeat(),
        ])
        EUDDoEvents()
    EUDEndIf()

    # UDP는 매너로 허용하자.
