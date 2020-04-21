'''
Parses strings that could refer to template maps.
'''


from .trgstrconst import UnitNameDict
from . import ubconv
from .mapdata import (
    strtable,
    unitnametable,
    locnametable,
    swnametable
)
from .utils import IgnoreColor


# Data getter
def ParseLocation(locstring):
    '''
    Location name -> Location id.
     - type(locstring) is int : return as-is
     - type(locstring) in [str, bytes]: find it in template map.
       If matching location name -> return its location id
       If location name is ambigious -> raise RuntimeError
       If location name not found -> raise Runtimeerror
    '''
    try:
        string = ubconv.u2b(locstring)

        # try map-defined location name
        try:
            locidx = locnametable[string]
            if locidx is None:
                raise RuntimeError('Ambigious location name %s' % locstring)
            return locidx

        except KeyError:
            pass

        raise RuntimeError('Unknown location name %s' % locstring)

    except TypeError:
        return locstring


def ParseUnit(unitstring):
    '''
    Unit name -> Unit ID.
     - type(unitstring) is int : return as-is
     - type(unitstring) in [str, bytes]: find it in template map/default names.
       If matching unit name in template map -> return is unit id
       If matching unit name in stock unit name -> return its unit id
       If unit name is ambigious -> raise RuntimeError
       If unit name not found -> raise RuntimeError.
    '''

    try:
        # try map-defined location name
        try:
            string = ubconv.u2b(unitstring)
            unitidx = unitnametable[string]
            if unitidx is None:
                raise RuntimeError('Ambigious unit name %s' % unitstring)
            return unitidx

        except KeyError:
            pass

        # try default unit name
        try:
            string = unitstring
            unitidx = UnitNameDict[string]
            return unitidx

        except KeyError:
            pass

        raise RuntimeError('Unknown unit name %s' % unitstring)

    except TypeError:
        return unitstring  # maybe int


def ParseString(string):
    '''
    String -> string id.
     - type(string) is int : return as-is.
     - type(string) in [str, bytes]:
       If matching string -> returns its string id.
       If no match -> Creates new string & returns its id.
        (May cause string overflow error.)
    '''
    try:
        bstring = ubconv.u2b(string)
        return strtable.GetStringIndex(bstring)

    except TypeError:
        return string


def ParseSwitch(sw):
    try:
        string = ubconv.u2b(sw)

        try:
            swindex = swnametable[string]
            if swindex is None:
                raise RuntimeError('Ambigious switch name %s' % sw)
            return swindex

        except KeyError:
            pass

        raise RuntimeError('Unknown switch name %s' % sw)

    except TypeError:
        return sw
