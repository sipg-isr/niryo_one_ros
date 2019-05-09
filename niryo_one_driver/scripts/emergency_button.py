import RPi.GPIO as GPIO
import time
from niryo_one_python_api.niryo_one_api import *


n = NiryoOne()

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
             
def callback_function_falling(channel):
    print("Button Activated...")
    try:
        n.activate_learning_mode(True)
        print("Robot Learning Mode Active")
    except NiryoOneException as e:
        print(e)

GPIO.add_event_detect(16, GPIO.FALLING, callback=callback_function_falling)
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
