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

# (Line 1) import stages.ep_commonlib as cl;
from stages import ep_commonlib as cl
# (Line 3) var iflag = 0;
iflag = EUDCreateVariables(1)
_IGVA([iflag], lambda: [0])
# (Line 4) var t = 23;
t = EUDCreateVariables(1)
_IGVA([t], lambda: [23])
# (Line 5) var sx, sy = 1, 1;
sx, sy = EUDCreateVariables(2)
_IGVA([sx, sy], lambda: [1, 1])
# (Line 6) const dt = 24;
dt = _CGFW(lambda: [24], 1)[0]
# (Line 8) function pattern70() {
@EUDFunc
def f_pattern70():
    # (Line 9) if (iflag == 0) {
    if EUDIf()(iflag == 0):
        # (Line 10) CreateUnit(25, "Recaller", "arbiter", P8);
        # (Line 11) iflag = 1;
        DoActions(CreateUnit(25, "Recaller", "arbiter", P8))
        iflag << (1)
        # (Line 12) }
        # (Line 14) t++;
    EUDEndIf()
    t.__iadd__(1)
    # (Line 15) if(t == dt - 1) {
    if EUDIf()(t == dt - 1):
        # (Line 16) for(var i = 0 ; i < 3 ; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i < 3):
            def _t5():
                i.__iadd__(1)
            # (Line 17) for(var j = 0 ; j < 3 ; j++) {
            j = EUDVariable()
            j << (0)
            if EUDWhile()(j < 3):
                def _t7():
                    j.__iadd__(1)
                # (Line 18) const x, y = sx + i * 3, sy + j * 3;
                x, y = List2Assignable([sx + i * 3, sy + j * 3])
                # (Line 19) cl.move_mvloc(x, y);
                # (Line 20) CreateUnit(1, "Small Slow Heavy Missile", "mvloc", P7);
                cl.f_move_mvloc(x, y)
                # (Line 21) }
                DoActions(CreateUnit(1, "Small Slow Heavy Missile", "mvloc", P7))
                # (Line 22) }
                EUDSetContinuePoint()
                _t7()
            EUDEndWhile()
            # (Line 23) sx++;
            EUDSetContinuePoint()
            _t5()
        EUDEndWhile()
        sx.__iadd__(1)
        # (Line 24) if(sx == 4) {
        if EUDIf()(sx == 4):
            # (Line 25) sx = 1;
            sx << (1)
            # (Line 26) sy++;
            sy.__iadd__(1)
            # (Line 27) if(sy == 4) sy = 1;
            if EUDIf()(sy == 4):
                sy << (1)
                # (Line 28) }
            EUDEndIf()
            # (Line 29) }
        EUDEndIf()
        # (Line 30) else if(t == dt) {
    if EUDElseIf()(t == dt):
        # (Line 31) t = 0;
        t << (0)
        # (Line 32) for(var i = 0 ; i < 3 ; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i < 3):
            def _t13():
                i.__iadd__(1)
            # (Line 33) for(var j = 0 ; j < 3 ; j++) {
            j = EUDVariable()
            j << (0)
            if EUDWhile()(j < 3):
                def _t15():
                    j.__iadd__(1)
                # (Line 34) const x, y = sx + i * 3, sy + j * 3;
                x, y = List2Assignable([sx + i * 3, sy + j * 3])
                # (Line 35) cl.move_mvloc(x, y);
                # (Line 36) RunAIScriptAt('Recall Here', 'mvloc');
                cl.f_move_mvloc(x, y)
                # (Line 37) }
                DoActions(RunAIScriptAt('Recall Here', 'mvloc'))
                # (Line 38) }
                EUDSetContinuePoint()
                _t15()
            EUDEndWhile()
            # (Line 39) }
            EUDSetContinuePoint()
            _t13()
        EUDEndWhile()
        # (Line 40) }
    EUDEndIf()
