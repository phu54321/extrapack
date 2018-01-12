## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName
    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

class _ARRW:
     def __init__(self, obj, index):
         self.obj = obj
         self.index = index
     def __lshift__(self, r):
         self.obj[self.index] = r

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 2) const mvloc = $L("mvloc");
mvloc = _CGFW(lambda: [GetLocationIndex("mvloc")], 1)[0]
# (Line 4) function move_mvloc(x, y) {
@EUDFunc
def f_move_mvloc(x, y):
    # (Line 5) const x0 = 736 + (x - 1) * 64;
    x0 = 736 + (x - 1) * 64
    # (Line 6) const y0 = 736 + (y - 1) * 64;
    y0 = 736 + (y - 1) * 64
    # (Line 7) SetMemory(0x58DC60 + 20 * mvloc + 0x00, SetTo, x0);
    # (Line 8) SetMemory(0x58DC60 + 20 * mvloc + 0x04, SetTo, y0);
    # (Line 9) SetMemory(0x58DC60 + 20 * mvloc + 0x08, SetTo, x0 + 64);
    # (Line 10) SetMemory(0x58DC60 + 20 * mvloc + 0x0C, SetTo, y0 + 64);
    # (Line 11) }
    DoActions([
        SetMemory(0x58DC60 + 20 * mvloc + 0x00, SetTo, x0),
        SetMemory(0x58DC60 + 20 * mvloc + 0x04, SetTo, y0),
        SetMemory(0x58DC60 + 20 * mvloc + 0x08, SetTo, x0 + 64),
        SetMemory(0x58DC60 + 20 * mvloc + 0x0C, SetTo, y0 + 64)
    ])
