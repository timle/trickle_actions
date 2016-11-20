# simple wrapper to read text which is given as second argument for this script
# part of trickle action scripts (for voice out actions)

import os
import sys
import requests

print sys.argv[1]


print 'pico2wave -w test.wav "' + sys.argv[1] + '" && aplay test.wav'

os.system('pico2wave -w test.wav "' + sys.argv[1] + '" && aplay test.wav')

