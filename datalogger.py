import machine
import utime
import os
machine.freq(75000000)
sensor_temp = machine.ADC(machine.ADC.CORE_TEMP)
led_onboard = machine.Pin(25, machine.Pin.OUT)
conversion_factor = 3.3 / (65535)

# startup indicator flah 3 times
for i in range(3):
    led_onboard.value(1)
    utime.sleep(0.75)
    led_onboard.value(0)
    utime.sleep(0.75)

utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)
utime.sleep(6)

#Time delay to stop the program manualy, so it won't ovorwrite temps.txt
#I dont now how to append it yet

file = open("temps.txt", "w")


while True:
# for j in range(10):
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    led_onboard.value(1)
    utime.sleep(1)
    file.write(str(temperature) + "\n")
    file.flush()
    utime.sleep(4)
    print(temperature)
    led_onboard.value(0)
    utime.sleep(10)


