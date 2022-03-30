import RPi.GPIO as GPIO
import time

def isfloat(val_str):
    try:
        float(val_str)
        return True
    except ValueError:
        return False

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def dec2bin(val):
    return [int(element) for element in bin(val) [2:].zfill(8)]

try:
    while True:
        val_str = input("Введите число от 0 до 255: ")
        if val_str.isdigit():
            val = int(val_str)
            if val > 255:
                print ("Ошибка! Число превышает возможности ЦАП")
                continue
            GPIO.output(dac, dec2bin(val))
            time.sleep(2)
            print("Предполагаемое значение напряжения на выходе ЦАП: ", "{:.4f}".format(3.3 * val / 256), "В")
        elif isfloat(val_str):
            val = float(val_str)
            if val < 0:
                print ("Ошибка! Число должно быть больше 0")
            else:
                print("Ошибка! Число должно быть целым")
        elif val_str == 'q':
            break
        else:
            print ("Ошибка! Это не число")
               
except ValueError:
    print("Неизвестная ошибка")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()