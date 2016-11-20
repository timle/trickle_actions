import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) #sets pin numbering, dont change

GPIO.setwarnings(False) # i dunno

GPIO.setup(19,GPIO.OUT) # tells pi that we want to use this port

GPIO.output(19,GPIO.HIGH) #set output on to high
time.sleep(2.5)
print "LED off"
time.sleep(6)
GPIO.output(19,GPIO.LOW) # set output to low)
