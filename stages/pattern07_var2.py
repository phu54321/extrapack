'''
6계단 사방에서
'''

from trggen import *
from .stages_commonlib import *


InitNone()

SelectCounter(0)

locs = (
    ['u%d' % i for i in range(1, 10)] +
    ['r%d' % i for i in range(1, 10)] +
    ['d%d' % i for i in range(9, 0, -1)] +
    ['l%d' % i for i in range(9, 0, -1)]
)  # len = 36

e_locs = (
    ['d%d' % i for i in range(1, 10)] +
    ['l%d' % i for i in range(1, 10)] +
    ['u%d' % i for i in range(9, 0, -1)] +
    ['r%d' % i for i in range(9, 0, -1)]
)  # len = 36


def pfromidx(idx):
    return (
        [P7] * 9 +
        [P8] * 9 +
        [P8] * 9 +
        [P7] * 9
    )[idx]

dt = 8
time = 0
stream_n = 6


sd = len(locs) // stream_n

assert len(locs) % stream_n == 0

for i in range(sd):
    sact = []
    for j in range(stream_n):
        idx = ((len(locs) - 1 - i) + j * sd) % len(locs)
        player = pfromidx(idx)
        sloc = locs[idx]
        eloc = e_locs[idx]
        sact += [
            CreateUnit(1, 'Fast Missile', sloc, player),
            Order('Fast Missile', player, sloc, Move, eloc)
        ]

    Shoot(time, sact)
    time += dt

Loop(time)

dact = []
for i in range(len(locs)):
    player = pfromidx(i)
    eloc = e_locs[i]
    dact += [KillUnitAt(All, 'Fast Missile', eloc, player)]
AlwaysShoot(dact)
