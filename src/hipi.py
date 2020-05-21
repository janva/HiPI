import RPi.GPIO as GPIO
import time

RED_LED_PIN = 17
# We want to use something called Broadcom SOC chanel designation
# This allows us GPIO numbers rather than physical pin numbers
# GPIO.setmode(GPIO.BOARD) uses physical pin numbering.
GPIO.setmode(GPIO.BCM)
# set red pin led to be used as output
GPIO.setup(RED_LED_PIN, GPIO.OUT)

while True:
    GPIO.output(RED_LED_PIN, GPIO.HIGH)
    print("ON")
    time.sleep(1)
    GPIO.output(RED_LED_PIN, GPIO.LOW)
    time.sleep(1)
