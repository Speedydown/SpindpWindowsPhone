__author__ = 'Speedy'

import time
import threading

try:
    import RPi.GPIO as GPIO
except:
    print "could not open iopins"

class IOPIN(object):

    def __init__(self):
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(30, GPIO.OUT)
            GPIO.output(30, False)
            GPIO.setup(31, GPIO.OUT)
            GPIO.output(31, False)
        except:
            print "IO pins failed!"

    def Horn(self):
        HornThread = threading.Thread(target=self.hornThread)
        HornThread.start()


    def hornThread(self):
        GPIO.output(30, True)
        GPIO.output(31, True)
        time.sleep(2.5)
        GPIO.output(30, False)
        GPIO.output(31, False)
        time.sleep(0.5)
        GPIO.output(30, True)
        GPIO.output(31, True)
        time.sleep(2.5)
        GPIO.output(30, False)
        GPIO.output(31, False)