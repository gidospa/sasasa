#!/usr/bin/env python3

import struct
import io

def tag(wavfile):

    with io.open(wavfile, 'rb') as fh:
        riff, size, fformat = struct.unpack('<4sI4s', fh.read(12))
        #print("RIFF: %s, Chunk Size: %i, format: %s" % (riff, size, fformat))
        if riff != b'RIFF' or fformat != b'WAVE':
            exit()

        #Read header
        chunk_header = fh.read(12)
        list, lsize, lformat = struct.unpack('<4sI4s', chunk_header)
        #print("LIST: %s, Chunk Size: %i, list: %s" % (list, lsize, lformat))

        if lformat != b'INFO':
            exit()

        #Read subchunk
        tags = {}
        lsize -= 4  # for INFO
        while (lsize > 0):
            chunk_header = fh.read(8)
            lsize -= 8
            subchunkid, subchunksize = struct.unpack('<4sI', chunk_header)
            #print("id: %s, Chunk Size: %i" % (subchunkid, subchunksize))
            key = subchunkid.decode('shift-jis')
            data = fh.read(subchunksize)
            tags[key] = data[:-1].decode('shift-jis')
            
            lsize -= subchunksize
            if subchunksize % 2 == 1:
                # remove padding
                fh.read(1)
                lsize -= 1
        return tags

if __name__ == '__main__':
    print(tag('tmp/prologue.wav'))

