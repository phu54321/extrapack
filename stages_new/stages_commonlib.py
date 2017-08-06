from trggen import *

counterunit = 0
stage = None
difficulty = 0  # 0:Normal, 1:Hard, 2:Insane
patternname_list = {}

#######


def SelectCounter(counterid):
    global counterunit
    counterunit = "@PatternSubCounter%d" % (counterid + 1)


def SetStage(diffn, newdifficulty, newstage, patternname):
    global stage, difficulty
    global counterunit
    global patternname_list

    stage = newstage
    difficulty = newdifficulty
    counterunit = None
    patternname_list[(stage - 1) * diffn + difficulty] = patternname


#######


def P8ApplyByPattern(conditions, actionfunc, pattern, additionalactions=None):
    """
    pattern_example = [
        '###### ',  # Everything except # is void.
        '   ### ',
        ' # # # ',
        ' #   # ',
        '@# # # ',  # @ is equivilant to space
        ' ###   ',
        ' ######',
    ]

    action_func(x, y) : 1 <= x,y <= 7
    """

    if additionalactions is None:
        additionalactions = []

    actions = [
        [
            [
                actionfunc(x + 1, y + 1)
                for x in range(9) if pattern[y][x] == '#'
            ] for y in range(9)
        ], additionalactions
    ]

    actions = FlattenList(actions)

    for i in range(0, len(actions), 63):
        subactions = actions[i:i + 63]
        Trigger(
            players=[P8],
            conditions=[
                conditions,
            ],
            actions=[
                subactions,
                PreserveTrigger()
            ],
        )


########

def MoveMainloc(x, y):
    return [
        MoveLocation('y%d' % y, 'Map Revealer', P8, 'xyorigin'),
        MoveLocation('x%d' % x, 'Map Revealer', P8, 'y%d' % y),
        MoveLocation('xymain', 'Map Revealer', P8, 'x%d' % x),
    ]


def MoveXRow(x):
    return [
        MoveLocation('x%d' % x, 'Map Revealer', P8, 'xyorigin'),
        MoveLocation('xall', 'Map Revealer', P8, 'x%d' % x),
        MoveLocation('xrow', 'Map Revealer', P8, 'xall'),
    ]


def MoveYRow(y):
    return [
        MoveLocation('y%d' % y, 'Map Revealer', P8, 'xyorigin'),
        MoveLocation('yall', 'Map Revealer', P8, 'y%d' % y),
        MoveLocation('yrow', 'Map Revealer', P8, 'yall'),
    ]


def InitWalls(pattern, unit='Block', player=P7, additionalactions=[]):
    P8ApplyByPattern(
        [
            Deaths(P8, Exactly, stage, "@PatternSelector"),
            Deaths(P8, Exactly, difficulty, "@Difficulty"),
            Deaths(P8, Exactly, 0, "@GameState"),
        ],
        lambda x, y: [
            MoveMainloc(x, y),
            CreateUnit(1, 'Protoss Shuttle', 'xymain', P7),
            KillUnitAt(All, 'Protoss Shuttle', 'xymain', P7),
            CreateUnit(1, unit, 'xymain', player)
        ],
        pattern,
        [
            additionalactions,
            SetSwitch("NormalMissileMove", Set),
            SetDeaths(P8, SetTo, 1, "@GameState"),
            PreserveTrigger(),
        ],
    )


def InitNormalMissileMove(actions=None, delay=0):
    if actions is None:
        actions = []

    actions += [
        SetSwitch("NormalMissileMove", Set),
        PreserveTrigger(),
    ]

    actions = FlattenList(actions)

    for i in range(0, len(actions), 64):
        Trigger(
            players=P8,
            conditions=[
                Deaths(P8, Exactly, stage, "@PatternSelector"),
                Deaths(P8, Exactly, difficulty, "@Difficulty"),
                Deaths(P8, Exactly, 0, "@GameState"),
                Deaths(P8, Exactly, 0, '@PatternSubCounter1'),
            ],
            actions=actions[i:i + 64]
        )

    Trigger(
        players=P8,
        conditions=[
            Deaths(P8, Exactly, stage, "@PatternSelector"),
            Deaths(P8, Exactly, difficulty, "@Difficulty"),
            Deaths(P8, Exactly, 0, "@GameState"),
            Deaths(P8, Exactly, delay * 2, '@PatternSubCounter1'),
        ],
        actions=[
            SetDeaths(P8, SetTo, 1, "@GameState"),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter1'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter2'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter3'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter4'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter5'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter6'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter7'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter8'),
            SetDeaths(P8, SetTo, 0, '@PatternSubCounter9'),
            PreserveTrigger(),
        ],
    )


def InitNone(additionalactions=None):
    if additionalactions is None:
        additionalactions = []

    Trigger(
        players=P8,
        conditions=[
            Deaths(P8, Exactly, stage, "@PatternSelector"),
            Deaths(P8, Exactly, difficulty, "@Difficulty"),
            Deaths(P8, Exactly, 0, "@GameState"),
        ],
        actions=[
            additionalactions,
            SetDeaths(P8, SetTo, 1, "@GameState"),
            PreserveTrigger(),
        ],
    )

########


def StageTrigger(conds, acts):
    acts = FlattenList(acts)
    for i in range(0, len(acts), 64):
        Trigger(
            players=[P8],
            conditions=[
                Deaths(P8, Exactly, stage, "@PatternSelector"),
                Deaths(P8, Exactly, difficulty, "@Difficulty"),
                Deaths(P8, Exactly, 1, "@GameState"),
                conds
            ],
            actions=acts[i:i + 64],
            flag=preserved
        )


def TimedStageTrigger(time, conds, acts):
    StageTrigger(
        [conds, Deaths(P8, Exactly, time * 2, counterunit)],
        acts
    )


def Shoot(time, actions):
    TimedStageTrigger(time, [], actions)


def AlwaysShoot(actions):
    StageTrigger([], actions)


def BombPattern(time, unit, bombplayer, pattern):
    P8ApplyByPattern(
        [
            Deaths(P8, Exactly, stage, "@PatternSelector"),
            Deaths(P8, Exactly, difficulty, "@Difficulty"),
            Deaths(P8, Exactly, 1, "@GameState"),
            Deaths(P8, Exactly, time * 2, counterunit),
        ],
        lambda x, y: [
            MoveMainloc(x, y),
            RemoveUnitAt(All, '(any unit)', 'xymain', Force1),
            CreateUnit(1, unit, 'xymain', bombplayer),
            KillUnitAt(All, unit, 'xymain', bombplayer),
        ],
        pattern
    )

'''
def PxMoveLocation(loc, x, y, size):
    loc = ParseLocation(loc)
    return [
        SetMemory(0x58DC60 + (loc - 1) * 20 + 0x0, SetTo, x - size),
        SetMemory(0x58DC60 + (loc - 1) * 20 + 0x4, SetTo, y - size),
        SetMemory(0x58DC60 + (loc - 1) * 20 + 0x8, SetTo, x + size),
        SetMemory(0x58DC60 + (loc - 1) * 20 + 0xC, SetTo, y + size),
    ]
'''

#######


def Loop(time):
    Trigger(
        players=[P8],
        conditions=[
            Deaths(P8, Exactly, stage, "@PatternSelector"),
            Deaths(P8, Exactly, difficulty, "@Difficulty"),
            Deaths(P8, Exactly, 1, "@GameState"),
            Deaths(P8, Exactly, time * 2 - 1, counterunit),
        ],
        actions=[
            SetDeaths(P8, SetTo, -1, counterunit),
            PreserveTrigger(),
        ],
    )
