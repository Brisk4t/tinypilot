import OPi.GPIO as GPIO
import time

POWER_BUTTON_PIN = 'PA10'
RESET_BUTTON_PIN = 'PA13'
CLICK_TIMER_SEC = 0.5
HOLD_TIMER_SEC = 10

GPIO.setmode(GPIO.SUNXI)
GPIO.setup(POWER_BUTTON_PIN, GPIO.OUT, initial=GPIO.HIGH) #Gpio 10 on orangepi zero
GPIO.setup(RESET_BUTTON_PIN, GPIO.OUT, initial=GPIO.HIGH) #Gpio 10 on orangepi zero



def click_power_button():
    GPIO.output(POWER_BUTTON_PIN, 0) # Pull the pin to GNDREF (LOW)
    time.sleep(CLICK_TIMER_SEC)
    GPIO.output(POWER_BUTTON_PIN, 1) # Pull the pin HIGH

def hold_power_button():
    GPIO.output(POWER_BUTTON_PIN, 0) # Pull the pin to GNDREF (LOW)
    time.sleep(HOLD_TIMER_SEC)
    GPIO.output(POWER_BUTTON_PIN, 1) # Pull the pin HIGH


def click_reset_button():
    GPIO.output(RESET_BUTTON_PIN, 0) # Pull the pin to GNDREF (LOW)
    time.sleep(CLICK_TIMER_SEC)
    GPIO.output(RESET_BUTTON_PIN, 1) # Pull the pin HIGH