# Test blink.
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.value(1)
    print ("On")
    utime.sleep(0.75)
    led_onboard.value(0)
    print ("Off")
    utime.sleep(0.75)
#end
    