'''
Insane의 수준
'''

from . import stages_commonlib
from eudplib import *
from .ep_commonlib import *
from .pattern70_impl import f_pattern70


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
