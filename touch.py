import os
import sys

fname = sys.argv[1]

def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

if __name__ == '__main__':
    import plac; plac.call(touch)
