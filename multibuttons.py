import RPi.GPIO as GPIO
import time

RED_BTN = 20
BLUE_BTN = 26
GREEN_BTN = 21
RESET_BTN = 19

def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RED_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BLUE_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(GREEN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(RESET_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonlights():
	while True:
	    input_RED = GPIO.input(RED_BTN)
	    input_BLUE = GPIO.input(BLUE_BTN)
	    input_GREEN = GPIO.input(GREEN_BTN)
	    input_RESET = GPIO.input(RESET_BTN)
	
	    if(input_RED == False):
	        print("RED button pushed")
	
	    if(input_BLUE == False):
	        print("BLUE button pushed")
	
	    if(input_GREEN == False):
	        print("GREEN button pushed")
	
	    if(input_RESET == False):
	        print("RESET button pushed")
	   
	    time.sleep(0.2)

def main():
    print("Starting program")
    print("Running setup steps...")
    setup()
    print("Setup steps completed")
    print("Beginning Button Light Program")
    buttonlights()
    GPIO.cleanup()

main()