# -*- coding: utf-8 -*-

import sys

AtoZ = 26
inStr = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."

def main():
    
    for offset in range(24):
        ptxt = ""
        # offset分ずらす
        for ch in inStr:
            if ord('a') <= ord(ch) and ord(ch) <= ord('z'):
                base = ord('a')
                new_ch = chr((ord(ch) - base + offset) % AtoZ + base)
            elif ord('A') <= ord(ch) and ord(ch) <= ord('Z'):
                base = ord('A')
                new_ch = chr((ord(ch) - base + offset) % AtoZ + base)
            else:
                new_ch = ch

            ptxt += new_ch

        print(ptxt)


if __name__ == '__main__':
    main()