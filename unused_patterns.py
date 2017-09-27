from stgl_ez import stagelist_easy
from stgl_nm import stagelist_normal
from stgl_hd import stagelist_hard
import os

stagelists = stagelist_easy + stagelist_normal + stagelist_hard
names = set(map(lambda x: x[0] + '.py', stagelists))

for stage in os.listdir('stages'):
    if stage not in names:
        print('Unused stage : %s' % stage)

