from savecode import basehash, makehash, b2u, TranslateToBase24

username = 'Mipi_Copy'


def exhash(savecode):
    h = makehash(basehash(savecode), username, 1)
    c = b2u(TranslateToBase24(h))
    return c

codes = open('stagelist.txt', 'r').read().split('\n')[:-1]

'''
print('username: %s' % username)
for stage, code in enumerate(codes):
    print('[%d] Stage %d : %s : %s'
          % (stage % 3, stage // 3 + 1, exhash(code), code))

'''
