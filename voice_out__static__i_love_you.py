import os
import random

this = random.randint(1,5)

if this == 1:

    text_to_read = "How many Apples grow on a tree?... All of them!"
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 2:

    text_to_read = "I shouldn't have had the seafood... I'm feeling a little eel."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 3:

    text_to_read = "Did you hear about the restaurant on the moon?... It lacked atmosphere."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 4:

    text_to_read = "I didn't get just a haircut.. I got them all cut. "
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 5:

    text_to_read = "I once dreamt I was a muffler... I woke up exausted."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')