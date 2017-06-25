import time
import RPi.GPIO as GPIO

LED_ENABLE = 0
LED_DISABLE = 1
RGB_ENABLE = 1
RGB_DISABLE = 0

# LED PORTS
LED1 = 12
LED2 = 16
LED3 = 18
LED4 = 22
LED5 = 7
LED = (LED1, LED2, LED3, LED4, LED5)
RGB_RED = 11
RGB_GREEN = 13
RGB_BLUE = 15
RGB = (RGB_RED, RGB_GREEN, RGB_BLUE)

def led_setup():
    GPIO.setmode(GPIO.BOARD)
    for val in LED:
        GPIO.setup(val, GPIO.OUT)
    for val in RGB:
        GPIO.setup(val, GPIO.OUT)

def led_activte(led, colour):
    GPIO.output(led,LED_ENABLE)
    GPIO.output(colour,RGB_ENABLE)

def led_deactivate(led, colour):
    GPIO.output(led, LED_DISABLE)
    GPIO.output(colour, RGB_DISABLE)

def led_clear():
    for val in LED:
        GPIO.output(val,LED_DISABLE)
    for val in RGB:
        GPIO.output(val, RGB_DISABLE)

def main():
    led_setup()
    led_clear()
    led_activate(LED1, RGB_RED)
    time.sleep(5)
    led.deactivate(LED1, RGB_RED)
    led_clear()
    GPIO.cleanup()

main()