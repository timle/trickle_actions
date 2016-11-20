import os
import sys
import math
import requests



url_1 = 'https://trickle-f05bc.firebaseio.com/kid.json'

#url_bal = 'https://trickle-f05bc.firebaseio.com/kid/balance.json'
#url_goal = 'https://trickle-f05bc.firebaseio.com/kid/balance.json'
#url_trickle_amnt = 'https://trickle-f05bc.firebaseio.com/kid/trickleAmount.json'


#response = requests.get(url_bal)
#data = response.json()

response = requests.get(url_1)
data = response.json()

# error catch here

# data['balance']
# data['goal']
# data['trickleAmount']


text_to_read = "I'm sorry, I my pigsternet isn't working right now. Please try again"

sleeps_to_goal = (float(data['goal'] - float(data['balance']))  / data['trickleAmount'])

if sleeps_to_goal < 0:
    text_to_read = "You've reached your goal! I'm so happy! You should set a new goal."

if sleeps_to_goal == 1:
    text_to_read = "One more sleep! Congratulations. Your almost there."

if sleeps_to_goal > 1:
    text_to_read = "You have to wait " + str(int(math.floor(sleeps_to_goal))) + " more sleeps until you reach your goal. Keep saving!"



# switch this on deployment
os.system('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')
print('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

