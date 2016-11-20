import os
import random



text_to_read = "I love you too!"
os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

