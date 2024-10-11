from gpiozero import Servo, LED
from time import sleep
import traceback
from datetime import datetime, timedelta

from pins import *

servoVert = Servo(SERVO_V_PIN)
servoHor = Servo(SERVO_H_PIN)

led = LED(LED_PIN)
led.on()
print("LED on")
from random import uniform

VERT_RANGE = (-1.04, 0.64)
HOR_RANGE = (-1.04, 1.04)

def ang(l, r):
    res = uniform(l, r)
    res = round(res,1)
    print(res)
    return res

def _stop():
    """Yielding control fixes jitter, sleep before yield to guarantee previous move is made."""
    sleep(0.2)
    servoVert.value = None
    servoHor.value = None

def move(prev_v, prev_h):
    print(f"Switching positions {servoVert.value} {servoHor.value}")
    servoVert.value = ang(*VERT_RANGE)
    v = servoVert.value
    servoHor.value = ang(*HOR_RANGE)
    h = servoHor.value
    print(f"Switched to {v} {h}")
    _stop()
    return v, h



PLAY_TIME = timedelta(minutes=5)
run_until = datetime.now() + PLAY_TIME
print(f"Starting movement, will run until {run_until}")
try:
    v, h = 0, 0
    while datetime.now() < run_until:
        v, h = move(v, h)
        sleep(3)
except Exception as e:
    led.off()
    print("Shutting down")
    raise e

led.off()
print("Done running.")
