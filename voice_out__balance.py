import os
import sys

print sys.argv[1]

print 'pico2wave -w test.wav "' + sys.argv[1] + '" && aplay test.wav'

os.system('pico2wave -w test.wav "' + sys.argv[1] + '" && aplay test.wav')





