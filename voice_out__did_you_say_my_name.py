import os
import random



import os
import random



this = random.randint(1,1)

if this == 1:
    text_to_read = "Hi."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 2:
    text_to_read = "I heard my name."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')




this = random.randint(1,6)

if this == 1:

    text_to_read = "Can you repeat the question? "
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 2:

    text_to_read = "It's hard to hear, can you repeat?"
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 3:

    text_to_read = "I'll tell you a joke if you ask."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 4:

    text_to_read = "I'm sorry! Please repeat the question. "
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 5:

    text_to_read = "Repeat it one more time?"
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 6:

    text_to_read = "Thanks for being patient, can you repeat your question?"
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

