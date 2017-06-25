import RPi.GPIO as GPIO
import time

# set GPIO to broadcom system
GPIO.setmode(GPIO.BCM)

# set inputs
LED_RED = 21
LED_BLUE = 20
LED_GREEN = 16

Freq = 100 #Mhz

# setting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# set LED colors to initial duty cycle of 0 (off)
RED = GPIO.PWM(LED_RED, Freq)
RED.start(0)
GREEN = GPIO.PWM(LED_GREEN, Freq)
GREEN.start(0)
BLUE = GPIO.PWM(LED_BLUE, Freq)
BLUE.start(0)

def set_light_color(R, G, B, on_time):
    print(R, G, B)
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)

def cycle_through_colors():
    for runcount in range(0,1):
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    for i in range(0, 101):
                        set_light_color((x*i),(y*i),(z*i), .01)

def main():
    print("Starting program")
    print("Running setup steps...")
    print("Setup steps completed")
    print("Beginning Button Light Program")
    cycle_through_colors()
    GPIO.cleanup()

main()