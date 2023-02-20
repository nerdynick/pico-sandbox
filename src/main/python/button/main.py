from machine import Pin

led = Pin(0, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_UP)

while True:
    val = button.value()
    if val == 1:
        led.off()
    elif val == 0:
        led.on()
    else:
        led.off()