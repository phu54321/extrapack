from eudplib import *
import hashlib
import struct
import config

randbox = [
    0x3DD895D7, 0x5CB36A04, 0x5BDEAE1D, 0xDD0D7CC9, 0xC5BA3BBE, 0x4369E96A,
    0xF00F9344, 0xD56041E4, 0x26D930AC, 0x54DE5729, 0x95BF4A82, 0x2CD99E8B,
    0x9ABFB3B6, 0xACBCF940, 0x9FBFE4A5, 0x7D079EB1, 0x89D32BE0, 0x646BA8C0,
    0xC90C2086, 0x6E6B06E7, 0x67DD4ACC, 0x8CD37CF3, 0x4C69105E, 0xC30C8EA1,
    0xB5D0CF31, 0xD4BB30E2, 0xDBBBC9D6, 0x3903B3C2, 0xE0D5E91E, 0x14015C4F,
    0x6B6B51F4, 0x09B64C2B, 0x4E048354, 0x98D220BC, 0xF6B9265B, 0x4DB26158,
    0x47B2CF7F, 0x1C6C6162, 0xFD62F97A, 0x4669BE79, 0x18B74777, 0x316E8EEF,
    0xAF0A1B4C, 0xBC66831A, 0x79DCB8A4, 0xB0D09822, 0xA3BC0074, 0xB966D409,
    0xEE0E612C, 0xD3D6F4FB, 0xC60CD9B2, 0x8708A3D2, 0x45DF5C75, 0x166CCF45,
    0x4ADFA541, 0xE3630B12, 0xAED16A4A, 0x17B7BE43, 0x12B7E950, 0x77073096,
    0x806567CB, 0xA7672661, 0x65B0D9C6, 0x9609A88E, 0xC7D7A8B4, 0x2D02EF8D,
    0x5D681B02, 0xCC0C7795, 0xF9B9DF6F, 0x0BDBDF21, 0xC1611DAB, 0x856530D8,
    0xD70DD2EE, 0x136C9856, 0xB10BE924, 0x05005713, 0x1E01F268, 0x60B08ED5,
    0x5EDEF90E, 0xBFD06116, 0xA00AE278, 0x66063BCA, 0xDF60EFC3, 0x24B4A3A6,
    0x9B64C2B0, 0x21B4F4B5, 0xB3667A2E, 0xD9D65ADC, 0xA50AB56B, 0x9DD277AF,
    0xF4D4B551, 0xE6635C01, 0xE10E9818, 0xBE0B1010, 0xF862AE69, 0x086D3D2D,
    0xEDB88320, 0x270241AA, 0x5268E236, 0xE8B8D433, 0x2802B89E, 0x1ADAD47D,
    0x30B5FFE9, 0x92D28E9B, 0x72076785, 0xFCB9887C, 0x9C0906A9, 0x63066CD9,
    0xA4D1C46D, 0x59B33D17, 0x36034AF6, 0x91646C97, 0x7CDCEFB7, 0xDEBB9EC5,
    0x3C03E4D1, 0x83D385C7, 0x7A6A5AA8, 0x3E6E77DB, 0xFF0F6A70, 0xD1BB67F1,
    0x56B3C423, 0x8A65C9EC, 0x7F6A0DBB, 0xE7B82D07, 0x32D86CE3, 0x5505262F,
    0xDA60B8D0, 0xE5D5BE0D, 0x7EB17CBD, 0xBDBDF21C, 0x3B6E20C8, 0x756AA39C,
    0x346ED9FC, 0xA867DF55, 0xF762575D, 0x76DC4190, 0x990951BA, 0x94643B84,
    0xB7BD5C3B, 0x2A6F2B94, 0x0CB61B38, 0x38D8C2C4, 0xD06016F7, 0x196C3671,
    0x6C0695ED, 0xFBD44C65, 0x37D83BF0, 0xA6BC5767, 0xE2B87A14, 0xD80D2BDA,
    0xEAD54739, 0x0EDB8832, 0x68DDB3F8, 0x74B1D29A, 0xEFD5102A, 0xE40ECF0B,
    0x03B6E20C, 0xEC63F226, 0x4FDFF252, 0xA9BCAE53, 0xCABAC28A, 0xE963A535,
    0x0F00F934, 0x71B18589, 0x8EBEEFF9, 0x2F6F7C87, 0x0D6D6A3E, 0x33031DE5,
    0x11010B5C, 0xC2D7FFA7, 0x62DD1DDF, 0x9309FF9D, 0x0A00AE27, 0x706AF48F,
    0xF1D4E242, 0x7BB12BAE, 0x5A05DF1B, 0xB8BDA50F, 0xAD678846, 0xC8D75180,
    0xF3B97148, 0xCE61E49F, 0x1DB71064, 0x40DF0B66, 0xD20D85FD, 0x076DC419,
    0xB40BBE37, 0xCFBA9599, 0x88085AE6, 0x206F85B3, 0xFA0F3D63, 0xC0BA6CAD,
    0xC4614AB8, 0x6DDDE4EB, 0xFED41B76, 0x6906C2FE, 0x84BE41DE, 0xA2677172,
    0x4B04D447, 0xB2BD0B28, 0xD6D6A3E8, 0x3FB506DD, 0x48B2364B, 0x4969474D,
    0x8D080DF5, 0x8BBEB8EA, 0x29D9C998, 0x220216B9, 0xB6662D3D, 0x10DA7A5A,
    0xAA0A4C5F, 0x04DB2615, 0x44042D73, 0x2EB40D81, 0x8F659EFF, 0x01DB7106,
    0x1FDA836E, 0x1B01A57B, 0x35B5A8FA, 0x026D930A, 0x6FB077E1, 0xBB0B4703,
    0x3AB551CE, 0x5768B525, 0xEB0E363F, 0x7807C9A2, 0x53B39330, 0x81BE16CD,
    0xABD13D59, 0x23D967BF, 0x86D3D2D4, 0xCDD70693, 0xBAD03605, 0x15DA2D49,
    0x5005713C, 0x616BFFD3, 0x51DE003A, 0xF50FC457, 0x06B6B51F, 0xA1D1937E,
    0x90BF1D91, 0xF262004E, 0x73DC1683, 0xCB61B38C, 0x42B2986C, 0x9E6495A3,
    0x256FD2A0, 0x58684C11, 0x2BB45A92, 0x6AB020F2, 0x8208F4C1, 0x41047A60,
    0xDCD60DCF, 0x5F058808, 0x97D2D988,
]

digits = b'2346789BCDFGHJKMPQRTVWXY'
salt = 'extra_v2.5_test_IX'

############


def basehash(savecode):
    global salt
    hashinput = u2b(savecode + salt)
    digest = hashlib.sha512(hashinput).digest()

    # Trim down to 32bit integer
    dwords = struct.unpack('<16I', digest)
    dwout = 0
    for dw in dwords:
        dwout ^= dw

    return dwout


def mix(a, b):
    for i in range(40):
        a, b = b, a ^ (b + b + b + 0xBBBBBBBB) & 0xffffffff
    return a ^ b


@EUDFunc
def f_mix(a, b):
    if EUDLoopN()(40):
        SetVariables([a, b], [b, a ^ (b + b + b + 0xBBBBBBBB) & 0xffffffff])
    EUDEndLoopN()
    return a ^ b


def makehash(basehash, username, retryn):
    username = u2b(username)
    a = 1
    b = 1
    c = 1
    for ch in username:
        if b'a'[0] <= ch <= b'z'[0]:
            ch += b'A'[0] - b'a'[0]

        a = (a + ch) % 255
        b = (b + a) % 255
        c = (c + b) % 255

    randboxhash = a ^ randbox[a] ^ randbox[b] ^ randbox[c]
    finalhash = mix(basehash ^ 0x3F3F3F3F, randboxhash)
    finalhash = mix(finalhash, retryn)
    finalhash %= (24 ** 6)
    return finalhash


def TranslateToBase24(finalhash):
    ch1 = digits[finalhash % 24]
    ch2 = digits[finalhash // 24 % 24]
    ch3 = digits[finalhash // 24 // 24 % 24]
    ch4 = digits[finalhash // 24 // 24 // 24 % 24]
    ch5 = digits[finalhash // 24 // 24 // 24 // 24 % 24]
    ch6 = digits[finalhash // 24 // 24 // 24 // 24 // 24 % 24]

    return bytes([ch6, ch5, ch4, ch3, ch2, ch1])


#############################################################


@EUDFunc
def f_makehash(basehash, username_db, retryn):
    a, b, c = EUDCreateVariables(3)
    SetVariables([a, b, c], [1, 1, 1])

    br = EUDByteReader()
    br.seekoffset(username_db)
    if EUDInfLoop()():
        ch = br.readbyte()
        # toupper
        if EUDIf()([b'a'[0] <= ch, ch <= b'z'[0]]):
            ch += b'A'[0] - b'a'[0]
        EUDEndIf()

        EUDBreakIf(ch == 0)
        a += ch
        Trigger(a >= 255, a.SubtractNumber(255))
        b += a
        Trigger(b >= 255, b.SubtractNumber(255))
        c += b
        Trigger(c >= 255, c.SubtractNumber(255))
    EUDEndInfLoop()

    randbox_array = EUDArray(randbox)
    randboxhash = a ^ randbox_array[a] ^ randbox_array[b] ^ randbox_array[c]
    finalhash = f_mix(basehash ^ 0x3F3F3F3F, randboxhash)
    finalhash = f_mix(finalhash, retryn)

    finalhash = finalhash % (24 ** 6)
    return finalhash


@EUDFunc
def f_writebase24str(finalhash, outputaddr):
    finalhash, ch1 = f_div(finalhash, 24)
    finalhash, ch2 = f_div(finalhash, 24)
    finalhash, ch3 = f_div(finalhash, 24)
    finalhash, ch4 = f_div(finalhash, 24)
    finalhash, ch5 = f_div(finalhash, 24)
    finalhash, ch6 = f_div(finalhash, 24)

    bw = EUDByteWriter()
    bw.seekoffset(outputaddr)
    digits_array = EUDArray([d for d in digits])
    bw.writebyte(digits_array[ch6])
    bw.writebyte(digits_array[ch5])
    bw.writebyte(digits_array[ch4])
    bw.writebyte(digits_array[ch3])
    bw.writebyte(digits_array[ch2])
    bw.writebyte(digits_array[ch1])
    bw.flushdword()


# --------------------------------------

stagedict = {}
stagedict_inv = {}
basehashlist = EUDArray(0)

fp = None


def RegisterStage(difficulty, stage, savecode):
    global fp
    savecode = 'diff%d_%s' % (difficulty, savecode)
    assert savecode not in stagedict_inv, 'Duplicate savecode %s' % savecode
    stagedict[config.diffn * stage + difficulty] = savecode
    stagedict_inv[savecode] = config.diffn * stage + difficulty

    if fp is None:
        fp = open('stagelist.txt', 'w')

    fp.write("%s\n" % savecode)
    print('[%d] Stage %2d : %s' % (difficulty, stage + 1, savecode))


def UpdateBasehash():
    global basehashlist

    def GetBasehash(i):
        try:
            return basehash(stagedict[i])
        except KeyError:
            return 0xFFFFFFFF

    basehashlist = EUDArray(
        [GetBasehash(i) for i in range(len(stagedict))]
    )


@EUDFunc
def f_gethash(player, difficulty, stage, tryn):
    username = 0x57EEEB + 36 * player
    return f_makehash(
        basehashlist[config.diffn * stage + difficulty],
        username,
        tryn
    )
