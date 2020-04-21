'''
scenario.chk section tokenizer. Internally used in eudtrg.
'''


import struct
from . import ubconv, binio

# conversion from string to ulong.
#  ex) TYPE -> 54 59 50 45 -> 0x45505954 -> 1162893652
#


def string2ulong(s):
    # s may be string or bytes. convert to bytes.
    if type(s) is str:
        s = ubconv.u2b(s)

    if len(s) < 4:
        ts = s
        s = [32] * 4  # 32 is ' ' (space). ex) 'VER' translates to 'VER '
        s[0:len(ts)] = ts

    return binio.b2i4(s, 0)


"""
General CHK class.
"""


class CHK:

    def __init__(self):
        self.sections = {}

    def loadblank(self):
        self.sections = {}

    def loadchk(self, b):
        # this code won't handle protection methods properly such as...
        #  - duplicate section name
        #  - jump section protection
        #
        # this program although handles
        #  - invalid section length (too high)
        #  - unused sections

        t = self.sections  # temporarilly store
        self.sections = {}

        try:
            index = 0
            while 1:
                # read data
                sectionname = binio.b2i4(b, index)
                sectionlength = binio.b2i4(b, index + 4)

                if sectionlength < 0:
                    # jsp are not supported.
                    return False

                section = b[index + 8: index + 8 + sectionlength]
                index += sectionlength + 8

                # This code won't handle sections with same sectionname.
                self.sections[sectionname] = section
                # Just overwrite. We're not making another unprotector.

            return True

        except RuntimeError:
            # read failed. unsupported chk protection method applied.
            self.section = t
            return False

        except IndexError:
            return True  # read completed

    def savechk(self):
        # calculate output size
        blist = []
        for name, binary in self.sections.items():
            blist.append(
                b''.join([struct.pack('<LL', name, len(binary)), binary]))

        return b''.join(blist)

    def enumsection(self):
        return list(self.sections.keys())

    def getsection(self, sectionname):
        sectionname = string2ulong(sectionname)
        return self.sections[sectionname]  # Nameerror may be raised.

    def setsection(self, sectionname, b):
        sectionname = string2ulong(sectionname)
        self.sections[sectionname] = bytes(b)

    def delsection(self, sectionname):
        sectionname = string2ulong(sectionname)
        del self.sections[sectionname]
