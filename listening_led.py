import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #sets pin numbering, dont change

GPIO.setwarnings(False) # i dunno

GPIO.setup(19,GPIO.OUT) # tells pi that we want to use this port

GPIO.output(19,GPIO.HIGH) #set output on to high
time.sleep(4) # wait 4  seconds
print "LED off"
GPIO.output(19,GPIO.LOW) # set output to low)
