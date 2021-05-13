from math import nextafter
import sys, os, imageio, textwrap, time
from decimal import *
os.chdir(os.path.split(sys.argv[0])[0])

#This programs expects a "frames" folder that it will read images out of.

#ffmpeg -i "Bad Apple!! - Full Version w_video [Lyrics in Romaji, Translation in English]-9lNZ_Rnr7Jc.mp4" -f lavfi -i color=gray:s=64x64 -f lavfi -i color=black:s=64x64 -f lavfi -i color=white:s=64x64 -filter_complex scale=64:64,threshold frames/frame%09d.png 
input()

sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

getcontext().prec = 64 ** 2

nextTime = 0
for t in range(1, len(os.listdir("frames")) + 1):
    t = str(t).rjust(9, '0')
    g = [''.join(str(sign(o[0])) for o in i) for i in imageio.imread(f'frames/frame{t}.png')]
    w, h = len(g[0]), len(g)
    dh, d2 = Decimal(h), Decimal(2)
    f = lambda x, y: int(((y // dh) * d2 ** (-dh * int(x) - (int(y) % dh))) % d2)
    n = Decimal(h * int(''.join(''.join(g[o][i] for o in range(len(g) - 1, -1, -1)) for i in range(len(g[0]))), 2))
    # print('\n'.join(''.join('██' if f(Decimal(x), n + Decimal(y)) else '[]' for x in range(w - 1, -1, -1)) for y in range(h))) #slow mode
    numberPrint = '\n'.join(textwrap.wrap(str(n), width = 64 * 2))
    pr = str('\n\n' + numberPrint + '\n' + ('\n'.join(i.replace('0', '  ').replace('1', '██') for i in g)))
    sys.stdout.write(pr) #fast mode

    while time.time() < nextTime:
        pass
    
    nextTime = time.time() + (1000 / 24) * 1 / 1000