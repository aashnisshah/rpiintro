import random, time
import RPi.GPIO as GPIO

# set GPIO to broadcom system
GPIO.setmode(GPIO.BCM)

# set pins
LED_RED = 18
LED_GREEN = 27
LED_BLUE = 17

# set pins to output
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

Freq = 100 #Mhz

# set LED colors to initial duty cycle of 0 (off)
RED = GPIO.PWM(LED_RED, Freq)
RED.start(0)
GREEN = GPIO.PWM(LED_GREEN, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(LED_BLUE, Freq)
BLUE.start(0)

def color(R, G, B, on_time):

    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)

def cycle_through_colors():
    print("Light it up")
    print("R G B\n------------")    
    for runcount in range(0,2):
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    print(x, y, z)
                    for i in range(0, 101):
                        color((x*i),(y*i),(z*i), .02)

def main():
    print("setting up the light config")
    print("starting the lights")
    print("Stage 1: Cycle through the colors")
    cycle_through_colors()
    GPIO.cleanup()

main()