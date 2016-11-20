import os
import sys

import requests



url_bal = 'https://trickle-f05bc.firebaseio.com/kid/balance.json'

#url_1 = 'https://trickle-f05bc.firebaseio.com/kid.json'

response = requests.get(url_bal)
bal_val = response.json()

text_to_read = "I'm sorry, I my pigsternet isn't working right now. Please try again"

if bal_val == 0:
    text_to_read = "Your account is empty!"

if (bal_val > 0) and (bal_val < 1):
    text_to_read = "You have " + str(bal_val) + "cents in your account."

if (bal_val == 1):
    text_to_read = "You have " + str(int(bal_val)) + " dollar in your account."

if (bal_val > 1):
    text_to_read = "You have over " + str(int(bal_val)) + " dollars in your account. You are a great saver, keep it up!"

#switch this on deployment

os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')
#print('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

