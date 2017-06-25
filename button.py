import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    inputValue = GPIO.input(21)
    if(inputValue==False):
        count = count + 1
        print("Button pressed for " + str(count) + " ms")
    else:
        count = 0
    time.sleep(0.1)