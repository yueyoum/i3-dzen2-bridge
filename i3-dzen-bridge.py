#!/usr/bin/env python

"""
Bridge i3status output to dzen2. Make **ICON** in dzen2 display

Author: Wang Chao <https://github.com/yueyoum>
"""


import sys
import os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

PREFIX = os.path.join(PROJECT_PATH, 'xbm-icons')
WIFI   = '^i(%s/net-wifi4.xbm)' % PREFIX
WIRED  = '^i(%s/net-wired.xbm)' % PREFIX
VOL    = '^i(%s/vol-hi.xbm)' % PREFIX
BAT    = '^i(%s/power-bat2.xbm)' % PREFIX
AC     = '^i(%s/power-ac.xbm)' % PREFIX
CPU    = '^i(%s/cpu.xbm)' % PREFIX
TEMP   = '^i(%s/temp.xbm)' % PREFIX
LOAD   = '^i(%s/load.xbm)' % PREFIX



REPLACE_ITEM = {
    '_W': WIFI,
    '_E': WIRED,
    '_V': VOL,
    '_B': BAT,
    '_U': CPU,
    '_T': TEMP,
    '_L': LOAD,
}.items()


while True:
    line = raw_input()
    for k, v in REPLACE_ITEM:
        line = line.replace(k, v)


    sys.stdout.write(line + "\n")
    sys.stdout.flush()

