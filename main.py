#####
#
# 구조조정 원칙
#
#  1. 단순동작 반복 패턴, 시간을 쓸데없이 끄는 패턴은 없앤다.
#  2. 멋지지 않은 패턴은 없앤다.
#  3. 목숨을 잡아먹으려고 만든 탄은 전부 없앤다.
#  4. 드론에 인위적인 조작을 가하는 탄(무궁화꽃 등) 은 없앤다.
#
#####

from runpy import run_module
from trggen import *
import os
import importlib
import eudplib as ep

import config
from stages import stages_commonlib as cl

# 스테이지들
from stgl_ez import stagelist_easy
from stgl_nm import stagelist_normal
from stgl_hd import stagelist_hard

# pattern54_var4
if config.debugmode:
    stagelists = [[('pattern54_var4', 'testing')] for _ in range(3)]
else:
    stagelists = [stagelist_easy, stagelist_normal, stagelist_hard]


def importModule(modname):
    if not os.path.exists('stages/%s.eps' % modname):
        run_module('stages.%s' % pdata[0])
    else:
        mod = importlib.import_module('stages.%s' % modname)
        f_pattern = getattr(mod, "f_pattern")

        cl.InitNone()

        ####

        cl.inline_eudplib(cl.P8, """\
if EUDIf()([
    Deaths(P8, Exactly, %d, "@PatternSelector"),
    Deaths(P8, Exactly, %d, "@Difficulty"),
    Deaths(P8, Exactly, 1, "@GameState"),
]):
    f_%s()
EUDEndIf()
        """ % (cl.stage, cl.difficulty, modname))

        if 'f_%s' % modname not in ep.GetEUDNamespace():
            ep.EUDRegisterObjectToNamespace('f_%s' % modname, f_pattern)


LoadMap("res/basemap.scx")

##############################################################

run_module('latencycheck')
run_module('alwaysloop')

##############################################################


config.stagenarr = [len(l) for l in stagelists]
config.diffn = len(stagelists)

for diff, stagelist in enumerate(stagelists):
    for i, pdata in enumerate(stagelist):
        cl.SetStage(config.diffn, diff, i + 1, pdata[1])
        importModule(pdata[0])

    print('#Stages in diff %d : %d' % (diff, len(stagelist)))


##############################################################

run_module('movemissiles')
run_module('stagesys')

run_module('lifesys')
run_module('gameend')

##############################################################

SaveMap("temp.scx")

run_module('applyeudpatch')

# Cleanup .tmp files
for path in os.listdir('.'):
    if path.endswith('.tmp'):
        os.unlink(path)
    if path.endswith('.scx'):
        os.replace(path, os.path.join('dist', path))

# OK
try:
    import winsound
    winsound.MessageBeep()
except ImportError:
    pass
