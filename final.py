import RPi.GPIO as GPIO
import time

# set GPIO to broadcom system
GPIO.setmode(GPIO.BCM)

# set inputs
RED_BTN = 20
BLUE_BTN = 26
GREEN_BTN = 21
RESET_BTN = 19

LED_RED = 18
LED_BLUE = 17
LED_GREEN = 27

Freq = 100 #Mhz

# setting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BLUE_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GREEN_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RESET_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
    RED.ChangeDutyCycle(R)
    GREEN.ChangeDutyCycle(G)
    BLUE.ChangeDutyCycle(B)
    time.sleep(on_time)

def show_red_light():
    set_light_color(100, 0, 0, 0.02)

def show_blue_light():
    set_light_color(0, 100, 0, 0.02)

def show_green_light():
    set_light_color(0, 0, 100, 0.02)

def cycle_through_colors():
    for runcount in range(0,1):
        for x in range(0,2):
            for y in range(0,2):
                for z in range(0,2):
                    for i in range(0, 101):
				
	    	        input_RED = GPIO.input(RED_BTN)
		        input_BLUE = GPIO.input(BLUE_BTN)
		        input_GREEN = GPIO.input(GREEN_BTN)
		        input_RESET = GPIO.input(RESET_BTN)
			
			global LIGHT_STATE				
			if(get_light_state() != "RESET"):
				print("light state not reset")
				return		
                        set_light_color((x*i),(y*i),(z*i), .01)

def get_light_state():
	input_RED = GPIO.input(RED_BTN)
	input_BLUE = GPIO.input(BLUE_BTN)
	input_GREEN = GPIO.input(GREEN_BTN)
	input_RESET = GPIO.input(RESET_BTN)
	global LIGHT_STATE

	if(input_RED == False):
	        print("RED button pushed")
		LIGHT_STATE = "RED"
	if(input_BLUE == False):
	        print("BLUE button pushed")
		LIGHT_STATE = "BLUE"
	if(input_GREEN == False):
	        print("GREEN button pushed")
		LIGHT_STATE = "GREEN"
	if(input_RESET == False):
	        print("RESET button pushed")
		LIGHT_STATE = "RESET"

	return LIGHT_STATE

def buttonlights():
	global LIGHT_STATE
	LIGHT_STATE = "RESET"
	while True:
	    BUTTON_INPUT = get_light_state()
	
	    if(BUTTON_INPUT == "RED"):
		show_red_light()
	
	    if(BUTTON_INPUT == "BLUE"):
		show_blue_light()
	
	    if(BUTTON_INPUT == "GREEN"):
		show_green_light()
	
	    if(BUTTON_INPUT == "RESET" or LIGHT_STATE == "RESET"):
		cycle_through_colors()
	
	    time.sleep(0.2)

def main():
    print("Starting program")
    print("Running setup steps...")
    print("Setup steps completed")
    print("Beginning Button Light Program")
    buttonlights()
    GPIO.cleanup()

main()