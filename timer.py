from eudplib import *


@EUDFunc
def f_time():
    return 0xFFFFFFFF - f_dwread_epd(EPD(0x51CE8C))

dsttimer = EUDVariable()


@EUDFunc
def f_starttimer(duration):
    dsttimer << f_time() + duration - 42


@EUDFunc
def f_istimerhit():
    ret = EUDVariable()
    if EUDIf()(dsttimer <= f_time()):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret
