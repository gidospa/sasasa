#!/usr/bin/env python3

import re
import sys
import glob
import subprocess
from subprocess import PIPE
import riff


wavtag2flac = {'IART': 'ARTIST', 'INAM': 'TITLE', 'IPRD': 'ALBUM', 'IGNR': 'GENRE', 'ITRK': 'TRACKNUMBER'}


if __name__ == "__main__":
    dirs = ["."]
    if len(sys.argv) > 1:
        dirs = sys.argv[1:]

    for dir in dirs:
        dir = re.sub('/+$', '', dir)
        wavs = glob.glob(dir + "/*.wav")
        for wav in wavs:
            print(wav, end=': ')
            wavtag = riff.tag(wav)
            command = ['flac', '"{}"'.format(wav.replace('"', '\\"'))]
            for id in wavtag.keys():
                if id in wavtag2flac:
                    command.append("-T")
                    command.append("\"{}={}\"".format(wavtag2flac[id].replace('"', '\\"'), wavtag[id].replace('"', '\\"')))
            returncode = subprocess.call(' '.join(command), shell=True, stdout=PIPE, stderr=PIPE)
            if returncode == 0:
                print('done')
            else:
                print('false')
