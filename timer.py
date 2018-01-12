from eudplib import *


time = EUDVariable(1234)

@EUDFunc
def f_time():
    return time

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


@EUDFunc
def f_tick():
    time << time + 42
