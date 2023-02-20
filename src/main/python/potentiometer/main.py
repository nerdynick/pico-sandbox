from machine import Pin, PWM, ADC

led = PWM(Pin(0))
pot = ADC(Pin(28))

# led.freq(10000)

pDuty = 0
nDuty = 0

while True:
    nDuty = pot.read_u16()

    if nDuty <= 300:
        led.duty_u16(0)
    else:
        led.duty_u16(nDuty)

    if nDuty != pDuty:
        print(nDuty)
    
    pDuty = nDuty