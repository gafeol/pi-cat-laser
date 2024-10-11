from gpiozero import Servo, LED
from time import sleep

LED_PIN = 4
SERVO_V_PIN = 14
SERVO_H_PIN = 15

servoVert = Servo(SERVO_V_PIN)
servoHor = Servo(SERVO_H_PIN)

led = LED(LED_PIN)
led.on()
print("LED on")
from random import uniform

VERT_RANGE = (-1, 0.5)
HOR_RANGE = (-1, 1)

def ang(l, r):
    res = uniform(l, r)
    print(res)
    return res

print("Starting movement")
try:
    while True:
        print("Switching positions")
        servoVert.value = ang(*VERT_RANGE)
        servoHor.value = ang(*HOR_RANGE)
        sleep(3)
except Exception as e:
    print(f"Exception: {e}")
    led.off()
    print("Shutting down")
