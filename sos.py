# S.O.S. blinker.
import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

# Not tho best code for a sos morse code blinker.


while True:
    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(1.125)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(1.125)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(1.125)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(0.375)

    led_onboard.value(1)
    utime.sleep(0.375)
    led_onboard.value(0)
    utime.sleep(2.625)


#end
    