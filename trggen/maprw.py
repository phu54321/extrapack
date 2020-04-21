'''
Implements LoadMap, SaveMap function
'''

import os
import zipfile
import time

from .mapdata import (
    locnametable,
    swnametable,
    unitnametable,
    strtable,
    uprptable,
    uprpdict,
    trgtable
)

from . import binio, chktok
from .utils import IgnoreColor
from eudplib.core.mapdata import mpqapi


# private variables
_chk = None
_mpqcontent = None
_origfname = None


def _PutDict_NoDup(d, key, value):
    if key in d:  # Duplication
        d[key] = None  # Mark as duplicate
    else:
        d[key] = value


def LoadMap(fname):
    print('Loading map %s' % fname)

    global _chk, _mpqcontent, _origfname

    _origfname = os.path.abspath(fname)

    # read mpq content. The file will be copied to output file.
    _mpqcontent = open(fname, 'rb').read()

    # open mpq file
    mr = mpqapi.MPQ()
    if not mr.Open(fname):
        raise RuntimeError('Failed to open map file \'%s\'.' % fname)

    # extract scenario.chk
    rawchk = mr.Extract('staredit\\scenario.chk')
    chk = chktok.CHK()
    chk.loadchk(rawchk)
    _chk = chk

    # Delete unwanted sections.
    chk.delsection('UPRP')  # Unit properties are ignored here.
    chk.delsection('UPUS')  # related to uprp

    # Load STR section
    strtable.LoadTBL(_chk.getsection('STR'))

    # Init nametables
    locnametable.clear()
    unitnametable.clear()
    swnametable.clear()
    uprptable.clear()
    trgtable.clear()

    # Get location names
    mrgn = _chk.getsection('MRGN')
    if mrgn:
        locn = len(mrgn) // 20
        for i in range(locn):
            locstrid = binio.b2i2(mrgn, i * 20 + 16)
            locstr = IgnoreColor(strtable.GetString(locstrid))
            if not locstr:
                continue

            # SC counts location from 1. Weird
            _PutDict_NoDup(locnametable, locstr, i + 1)

    # Get unit names
    unix = _chk.getsection('UNIx')
    if unix:
        for i in range(228):
            unitstrid = binio.b2i2(unix, 3192 + i * 2)
            unitstr = strtable.GetString(unitstrid)
            # print('unit: %3d: %s' % (i, unitstr))
            if not unitstr:
                continue

            _PutDict_NoDup(unitnametable, unitstr, i)
            cignored = IgnoreColor(unitstr)
            if cignored != unitstr:
                _PutDict_NoDup(unitnametable, cignored, i)

    # Switch names
    swnm = _chk.getsection('SWNM')
    if swnm:
        for i in range(256):
            switchstrid = binio.b2i4(swnm, i * 4)
            switchstr = strtable.GetString(switchstrid)
            if switchstr:
                # print('switch: %3d: %s' % (i, switchstr))
                _PutDict_NoDup(swnametable, switchstr, i)

    uprptable.clear()
    uprpdict.clear()


def SaveMap(fname, backupdb=None):
    '''
    Inject EUDObjects needed for roots into template map and save it to fname.
    Original map file is not altered.
    '''

    print('Saving map %s' % fname)

    ofname = os.path.abspath(fname)
    if ofname == _origfname:
        raise RuntimeError("Overwrite input file is prohibited." % _mpqcontent)

    # write new uprp
    uprpcontent = b''.join(uprptable + [bytes(20 * (64 - len(uprptable)))])
    _chk.setsection('UPRP', uprpcontent)

    # write new upus
    upuscontent = b'\x01\0\0\0' * len(uprptable) + bytes(64 - len(uprptable))
    _chk.setsection('UPUS', upuscontent)

    # write new str
    strcontent = strtable.SaveTBL()
    _chk.setsection('STR', strcontent)

    # write new trigger
    trgcontent = b''.join(trgtable)
    _chk.setsection('TRIG', trgcontent)

    # dump
    rawchk = _chk.savechk()

    # dump mpq content and modify it
    open(fname, 'wb').write(_mpqcontent)
    mw = mpqapi.MPQ()
    if not mw.Open(fname):
        raise RuntimeError('Cannot open output file \'%s\'.' % _mpqcontent)

    mw.PutFile('staredit\\scenario.chk', rawchk)

    # Compact & close
    mw.Compact()
    mw.Close()

    # Backup output file
    if backupdb:
        assert backupdb[-4:] == '.zip'
        mapfile = open(fname, 'rb').read()
        with zipfile.ZipFile(backupdb) as z:
            tm = time.localtime()
            timestr = '%d%d%d_%d%d%d' % (
                tm.tm_year,
                tm.tm_mon,
                tm.tm_mday,
                tm.tm_hour,
                tm.tm_min,
                tm.tm_sec
            )
            z.writestr('backup_%s.scx' % timestr, mapfile)
