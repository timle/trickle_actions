import os
import random

this = random.randint(1,2)

if this == 1:

    text_to_read = "I heard you ask me what a savings account is. Trickles loves talking about savings."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "A savings account is how you grow your money. Sometimes you need the money right away."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "But most of the time, you save as much as you can. It's nice to have extra money as you get older."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "If you ask me again, I'll tell you more about what a savings account is."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

if this == 2:

    text_to_read = "I heard you ask me what a savings account is. Savings is my favorite topic."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "I like to help show you save your money. I'll show your money grow over time."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "You can ask me how much money you have ."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

    text_to_read = "If you ask me again, I'll tell you more about what a savings account is."
    os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')


#print('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')