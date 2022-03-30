import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

try:
    T = float(input("Введите период: "))
    val = 0
    while True:
        while val < 255:
            val += 1
            GPIO.output(dac, dec2bin(val))
            time.sleep(T/512)
        while val > 0:
            val -= 1
            GPIO.output(dac, dec2bin(val))
            time.sleep(T/512)
except  KeyboardInterrupt:
    print("Программа завершена")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

