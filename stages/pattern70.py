'''
Insane의 수준
'''

from . import stages_commonlib
from eudplib import *
from .ep_commonlib import *
from .pattern70_impl import f_pattern70

dt = 1
mCount = 13

xUnit = "@CustomVariable5"
yUnit = "@CustomVariable6"


def GetVStorage(i):
    player = [P7, P8, P9, P10, P11][i % 5]
    unit = [
        "@CustomVariable1",
        "@CustomVariable2",
        "@CustomVariable3",
    ][i // 5]
    return player, unit


stages_commonlib.InitNone()

####

stages_commonlib.inline_eudplib(stages_commonlib.P8, """\
if EUDIf()([
    Deaths(P8, Exactly, %d, "@PatternSelector"),
    Deaths(P8, Exactly, %d, "@Difficulty"),
    Deaths(P8, Exactly, 1, "@GameState"),
]):
    f_pattern70()
EUDEndIf()
""" % (stages_commonlib.stage, stages_commonlib.difficulty))


EUDRegistered(f_pattern70)
