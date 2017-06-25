import RPi.GPIO as GPIO
import time

ledPin = 21

print "Start"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)
print "LED off"
GPIO.output(ledPin,GPIO.LOW)
time.sleep(2)
print "LED on"
GPIO.output(ledPin,GPIO.HIGH)
time.sleep(2)
print "LED off"
GPIO.output(ledPin,GPIO.LOW)
print "Done 1"


count = 0
while(count <= 10):
    print "LED on"
    GPIO.output(ledPin,GPIO.HIGH)
    time.sleep(1)
    print "LED off"
    GPIO.output(ledPin,GPIO.LOW)
    time.sleep(1)
    
    count = count + 1
