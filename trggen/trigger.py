'''
Templates for TRIG section triggers. Uesd internally in eudtrg.
'''

from struct import pack
from . import binio
from .mapdata import trgtable
from .utils import FlattenList
from .trgconst import ParsePlayer, actexec, preserved, disabled

# constructor
_bc_dict = {
    1: binio.i2b1,
    2: binio.i2b2,
    4: binio.i2b4,
    None: (lambda x: x)
}


class _bpack:

    def __init__(self, b):
        self.b = b


def _bconstruct(vspair):
    btb = []
    for value, size in vspair:
        btb.append(_bc_dict[size](value))
    return b''.join(btb)


def Condition(locid, player, amount, unitid,
              comparison, condtype, restype, flag):
    if player < 0:
        player += 0x100000000  # EPD
    return _bpack(pack('<IIIHBBBBBB', locid, player, amount, unitid,
                       comparison, condtype, restype, flag, 0, 0))


def Action(locid1, strid, wavid, time, player1, player2,
           unitid, acttype, amount, flags):
    if player1 < 0:
        player1 += 0x100000000  # EPD
    if player2 < 0:
        player2 += 0x100000000  # EPD
    return _bpack(pack('<IIIIIIHBBBBBB', locid1, strid, wavid, time, player1,
                       player2, unitid, acttype, amount, flags, 0, 0, 0))


_triggers = []


def Trigger(players, conditions=[], actions=[], flag=None):
    if flag is None:
        flag = []

    players = FlattenList(players)
    conditions = FlattenList(conditions)
    actions = FlattenList(actions)
    flag = FlattenList(flag)

    assert len(conditions) <= 16
    assert len(actions) <= 64

    peff = bytearray(28)
    for p in players:
        p = ParsePlayer(p)
        peff[p] = 1

    trg_flag = 0
    if actexec in flag:
        trg_flag |= 1
    if preserved in flag:
        trg_flag |= 4
    if disabled in flag:
        trg_flag |= 8

    b = _bconstruct(
        [(cond.b, None) for cond in conditions] +
        [(bytes(20 * (16 - len(conditions))), None)] +
        [(act.b, None) for act in actions] +
        [(bytes(32 * (64 - len(actions))), None)] +
        [(trg_flag, 4)] +
        [(bytes(peff), None)]
    )

    assert len(b) == 2400
    trgtable.append(b)
