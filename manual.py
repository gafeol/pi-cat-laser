#!/usr/bin/python3
from gpiozero import Servo, LED
from time import sleep
from pins import *

servoVert = Servo(SERVO_V_PIN)
servoHor = Servo(SERVO_H_PIN)

def _stop():
    sleep(0.5)
    servoVert.value = None
    servoHor.value = None
_stop()

led = LED(LED_PIN)
led.on()

control = int(input("What do you wish to control?\n[1] only vertical servo\n[2] only horizontal servo\n[3] both\n\n"))


try:
    while True:
        if control&1:
            pos = float(input("Vert pos? (-1, 1)"))
            servoVert.value = pos
            print(f"Set servoVert to {servoVert.value}")
        if control&2:
            pos = float(input("Hor pos? (-1, 1)"))
            servoHor.value = pos
            print(f"Set servoHor to {servoHor.value}")
        _stop()
except Exception as e:
    print(f"Exception: {e}")
    led.off()
    print("Shutting down")
