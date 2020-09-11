#!/usr/bin/env python3

import re
import os
import sys
import glob

if __name__ == "__main__":
    dirs = ["."]
    if len(sys.argv) > 1:
        dirs = sys.argv[1:]

    for dir in dirs:
        dir = re.sub('/+$', '', dir)
        wavs = glob.glob(dir + "/*.wav")
        for wav in wavs:
            print(wav)
