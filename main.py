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
import condblock  # Import to initialized.
from trggen import *

import config
from stages.stages_commonlib import SetStage
import savecode
import winsound

# 스테이지들
from stgl_ez import stagelist_easy
from stgl_nm import stagelist_normal
from stgl_hd import stagelist_hard


config.slowmode = False
config.debugmode = False
config.difficulty = 1
config.initialstage = 1

if config.debugmode:
    stagelists = [[('pattern63_var2', 'testing')] for _ in range(3)]
else:
    stagelists = [stagelist_easy, stagelist_normal, stagelist_hard]


LoadMap("basemap.scx")

##############################################################

run_module('latencycheck')
run_module('alwaysloop')

##############################################################


config.stagenarr = [len(l) for l in stagelists]
config.diffn = len(stagelists)

for diff, stagelist in enumerate(stagelists):
    for i, pdata in enumerate(stagelist):
        SetStage(config.diffn, diff, i + 1, pdata[1])
        run_module('stages.%s' % pdata[0])
        savecode.RegisterStage(diff, i, pdata[0])

    print('#Stages in diff %d : %d' % (diff, len(stagelist)))

savecode.UpdateBasehash()


##############################################################

run_module('movemissiles')
run_module('stagesys')

run_module('lifesys')
run_module('gameend')

##############################################################

SaveMap("temp.scx")

run_module('applyeudpatch')

winsound.MessageBeep()
