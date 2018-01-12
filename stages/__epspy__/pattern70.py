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
# (Line 5) var t = 0;
t = EUDCreateVariables(1)
_IGVA([t], lambda: [0])
# (Line 6) const loopt = 13;
loopt = _CGFW(lambda: [13], 1)[0]
# (Line 8) var gangle = 0;
gangle = EUDCreateVariables(1)
_IGVA([gangle], lambda: [0])
# (Line 9) const dangle = 15;
dangle = _CGFW(lambda: [15], 1)[0]
# (Line 11) function pattern() {
@EUDFunc
def f_pattern():
    # (Line 12) if (iflag == 0) {
    if EUDIf()(iflag == 0):
        # (Line 13) CreateUnit(25, "Recaller", "arbiter", P8);
        # (Line 15) CreateUnit(1, "Small Slow Heavy Missile", "u3", P8);
        # (Line 16) CreateUnit(1, "Small Slow Heavy Missile", "u4", P8);
        # (Line 17) CreateUnit(1, "Small Slow Heavy Missile", "u5", P8);
        # (Line 18) CreateUnit(1, "Small Slow Heavy Missile", "u6", P8);
        # (Line 19) CreateUnit(1, "Small Slow Heavy Missile", "u7", P8);
        # (Line 20) Order("(men)", P8, "u3", Move, "d3");
        # (Line 21) Order("(men)", P8, "u4", Move, "d4");
        # (Line 22) Order("(men)", P8, "u5", Move, "d5");
        # (Line 23) Order("(men)", P8, "u6", Move, "d6");
        # (Line 24) Order("(men)", P8, "u7", Move, "d7");
        # (Line 25) iflag = 1;
        DoActions([
            CreateUnit(25, "Recaller", "arbiter", P8),
            CreateUnit(1, "Small Slow Heavy Missile", "u3", P8),
            CreateUnit(1, "Small Slow Heavy Missile", "u4", P8),
            CreateUnit(1, "Small Slow Heavy Missile", "u5", P8),
            CreateUnit(1, "Small Slow Heavy Missile", "u6", P8),
            CreateUnit(1, "Small Slow Heavy Missile", "u7", P8),
            Order("(men)", P8, "u3", Move, "d3"),
            Order("(men)", P8, "u4", Move, "d4"),
            Order("(men)", P8, "u5", Move, "d5"),
            Order("(men)", P8, "u6", Move, "d6"),
            Order("(men)", P8, "u7", Move, "d7")
        ])
        iflag << (1)
        # (Line 26) }
        # (Line 28) KillUnitAt(All, '(men)', 'u', P7);
    EUDEndIf()
    # (Line 29) KillUnitAt(All, '(men)', 'd', P7);
    # (Line 30) KillUnitAt(All, '(men)', 'l', P7);
    # (Line 31) KillUnitAt(All, '(men)', 'r', P7);
    # (Line 32) KillUnitAt(All, '(men)', 'd', P8);
    # (Line 34) if(t == 1) {
    DoActions([
        KillUnitAt(All, '(men)', 'u', P7),
        KillUnitAt(All, '(men)', 'd', P7),
        KillUnitAt(All, '(men)', 'l', P7),
        KillUnitAt(All, '(men)', 'r', P7),
        KillUnitAt(All, '(men)', 'd', P8)
    ])
    if EUDIf()(t == 1):
        # (Line 35) for(var i = 0 ; i < 2 ; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i < 2):
            def _t20():
                i.__iadd__(1)
            # (Line 36) for(var j = 0 ; j < 5 ; j++) {
            j = EUDVariable()
            j << (0)
            if EUDWhile()(j < 5):
                def _t22():
                    j.__iadd__(1)
                # (Line 37) const x, y = 1 + i * 8, 1 + j * 2;
                x, y = List2Assignable([1 + i * 8, 1 + j * 2])
                # (Line 38) cl.mloc_tile($L('cloc1'), x, y, 0);
                # (Line 39) RunAIScriptAt('Recall Here', 'cloc1');
                cl.f_mloc_tile(GetLocationIndex('cloc1'), x, y, 0)
                # (Line 40) }
                DoActions(RunAIScriptAt('Recall Here', 'cloc1'))
                # (Line 41) }
                EUDSetContinuePoint()
                _t22()
            EUDEndWhile()
            # (Line 42) }
            EUDSetContinuePoint()
            _t20()
        EUDEndWhile()
        # (Line 43) else if(t == loopt) {
    if EUDElseIf()(t == loopt):
        # (Line 44) t = 0;
        t << (0)
        # (Line 45) for(var i = 0 ; i < 2 ; i++) {
        i = EUDVariable()
        i << (0)
        if EUDWhile()(i < 2):
            def _t26():
                i.__iadd__(1)
            # (Line 46) for(var j = 0 ; j < 5 ; j++) {
            j = EUDVariable()
            j << (0)
            if EUDWhile()(j < 5):
                def _t28():
                    j.__iadd__(1)
                # (Line 47) const x, y = 1 + i * 8, 1 + j * 2;
                x, y = List2Assignable([1 + i * 8, 1 + j * 2])
                # (Line 48) cl.mloc_tile($L('cloc1'), x, y, -40);
                # (Line 49) CreateUnit(1, "Small Slow Missile", "cloc1", P7);
                cl.f_mloc_tile(GetLocationIndex('cloc1'), x, y, -40)
                # (Line 50) const px, py = cl.getTilePos(x, y);
                DoActions(CreateUnit(1, "Small Slow Missile", "cloc1", P7))
                px, py = List2Assignable([cl.f_getTilePos(x, y)])
                # (Line 51) const angle = gangle + (36 * 7) * (i + j * 2);
                angle = gangle + (36 * 7) * (i + j * 2)
                # (Line 52) const dx, dy = lengthdir(800, angle);
                dx, dy = List2Assignable([f_lengthdir(800, angle)])
                # (Line 53) const dpx, dpy = cl.getInfiniteVectorEnd(px, py, dx, dy);
                dpx, dpy = List2Assignable([cl.f_getInfiniteVectorEnd(px, py, dx, dy)])
                # (Line 54) cl.mloc_px($L('cloc2'), dpx, dpy, 0);
                # (Line 55) Order('(men)', P7, 'cloc1', Move, 'cloc2');
                cl.f_mloc_px(GetLocationIndex('cloc2'), dpx, dpy, 0)
                # (Line 56) }
                DoActions(Order('(men)', P7, 'cloc1', Move, 'cloc2'))
                # (Line 57) }
                EUDSetContinuePoint()
                _t28()
            EUDEndWhile()
            # (Line 59) gangle += dangle;
            EUDSetContinuePoint()
            _t26()
        EUDEndWhile()
        gangle.__iadd__(dangle)
        # (Line 60) if(gangle >= 360) gangle -= 360;
        if EUDIf()(gangle >= 360):
            gangle.__isub__(360)
            # (Line 61) }
        EUDEndIf()
        # (Line 62) t++;
    EUDEndIf()
    t.__iadd__(1)
    # (Line 63) }
