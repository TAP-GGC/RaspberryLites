from gpiozero import LED, Button
from time import sleep


# sudo apt update
# sudo apt install python3-gpiozero

led1 = LED(17)
button = Button(18)

def pulse(led):
    for i in range(0, 101, 5):
        led.value = i / 100
        sleep(0.05)
    for i in range(100, -1, -5):
        led.value = i / 100
        sleep(0.05)

while True:
    if button.is_pressed:
        led1.on()
        pulse(led1)
        sleep(1)
    else:
        led1.off()
        sleep(0.5)
