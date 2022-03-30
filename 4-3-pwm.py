import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 50)
p.start(50)

try:
    while True:
        power = float(input("duty cycle: "))
        p.start(power)
        print(str(3.3 * power / 100) + "В")
except KeyboardInterrupt:
    print("Программа завершена")
finally:
    GPIO.cleanup()