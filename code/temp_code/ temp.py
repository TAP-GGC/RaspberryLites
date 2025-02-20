
from time import sleep


# sudo apt update
# sudo apt install python3-gpiozero

led1 = LED(17)


def pulse(led):
    for i in range(0, 101, 5):
        led.value = i / 100
        sleep(0.05)
    for i in range(100, -1, -5):
        led.value = i / 100
        sleep(0.05)

while True:

    led1.on()
    pulse(led1)
    sleep(1)

