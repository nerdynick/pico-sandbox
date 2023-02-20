import machine
import time

sysLED = machine.Pin("LED", mode=machine.Pin.OUT)

while True:
    sysLED.toggle()
    time.sleep(1)