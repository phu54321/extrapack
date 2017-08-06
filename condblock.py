import trggen
from contextlib import contextmanager

from trggen import (
    P8,

    Deaths,
    SetDeaths,
    PreserveTrigger,

    Exactly,
    Add,
    Subtract,
)

_condLevel = 0
_oldTrigger = trggen.Trigger


# Monkey patched trigger

def _Trigger(players, conditions=None, actions=None, flag=None):
    if conditions is None:
        conditions = []

    conditions = trggen.FlattenList(conditions)

    if _condLevel != 0:
        conditions.insert(0, Deaths(P8, Exactly, _condLevel, "@CondLevel"))

    return _oldTrigger(players, conditions, actions, flag)


trggen.Trigger = _Trigger


# Scope opener & closer

@contextmanager
def CondBlock(player, conditions):
    global _condLevel

    _Trigger(
        player,
        conditions,
        [
            SetDeaths(P8, Add, 1, "@CondLevel"),
            PreserveTrigger()
        ],
    )
    _condLevel += 1

    yield

    _Trigger(
        player,
        actions=[
            SetDeaths(P8, Subtract, 1, "@CondLevel"),
            PreserveTrigger()
        ],
    )

    _condLevel -= 1
