from machine import Pin
import time

red = Pin(26, Pin.OUT)
yellow = Pin(27, Pin.OUT)
green = Pin(28, Pin.OUT)

def go():
    green.on()
    yellow.off()
    red.off()
def slow():
    green.off()
    yellow.on()
    red.off()
def stop():
    green.off()
    yellow.off()
    red.on()


while True:
    go()
    time.sleep(1)
    slow()
    time.sleep(1)
    stop()
    time.sleep(1)