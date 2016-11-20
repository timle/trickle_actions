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



text_to_read = "I'm sorry, I my pigsternet isn't working right now. Please try again"

my_goal = str(data['goal'])

if my_goal > 0:
    text_to_read = "Your current goal is " + str(my_goal) + "dollars"



# switch this on deployment
#os.system('pico2wave -w test.wav "' + sys.argv[1] + '" && aplay test.wav')
print('pico2wave -w test.wav "' + text_to_read + '" && aplay test.wav')

