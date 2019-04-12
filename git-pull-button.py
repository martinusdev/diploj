import RPi.GPIO as GPIO
import time
import subprocess
import os

def ledOn():
    GPIO.output(6, GPIO.HIGH)

def ledOff():
    GPIO.output(6, GPIO.LOW)

def blinkQuick():
    for x in range(4):
        ledOff()
        time.sleep(0.1)
        ledOn()
        time.sleep(0.05)

def blinkSlow():
    for x in range(3):
        ledOff()
        time.sleep(0.4)
        ledOn()
        time.sleep(0.4)
    

print('Diploj button Started')

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.OUT, initial=GPIO.HIGH)

blinkSlow()

while True:
    input_state = GPIO.input(18)
    sleep(0.1)	#cpu
    if input_state == True:
        print('Button pressed')
        p = subprocess.Popen('./real-deploy-command.sh')
        while p.poll() is None:
            blinkQuick()
        print('Deploy done, waiting for button')
        print(time.time())
        time.sleep(0.2)
