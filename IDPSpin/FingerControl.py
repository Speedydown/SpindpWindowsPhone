__author__ = 'Matthe Jacobs'
#Class that gets the finger control pulses and controls a leg with it
import threading
from threading import Semaphore

try:
    import serial
except:
    "serial not initialised"

class FingerControl(object):

    def __init__(self, MotionInterface):
        self._MotionInterface = MotionInterface
        #self._Semaphore = threading.Semaphore(1)
        self._Exited = False
        self._MotionInterfaceThread = threading.Thread(target=self.run)
        self._MotionInterfaceThread.start()


    def executeCommand(self, Command):
        pass

    def run(self):

        self._DefaultSpeed = self._MotionInterface.getSpeed()
        self._MotionInterface.setSpeed(0.06)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        self._ForwardLegs = [self._MotionInterface._Legs[4], self._MotionInterface._Legs[5]]
        self._middleLegs = [self._MotionInterface._Legs[2], self._MotionInterface._Legs[3]]

        self._MotionInterface.raiseLegs(self._middleLegs)
        self._MotionInterface.MoveLegsForward(self._middleLegs, True, [0, 20])
        self._MotionInterface.LowerLegs(self._middleLegs)

        self._MotionInterface.raiseLegs(self._ForwardLegs)
        self._MotionInterface.MoveLegsForward(self._ForwardLegs, True, [0, 90])

        for Leg in self._ForwardLegs:
            Leg.moveAnkle(350)
            Leg.moveKnee(250)

        while(not self._Exited):
            #Read incoming data
            #self._Semaphore.acquire()
            

            #self._Semaphore.release()

            incoming = self.ser.readline()
            try:
                if incoming[:2] == 'a1':
                    #Move the leg
                    pulse = int(incoming.strip('a1'))
                    if pulse < 350:
                        pulse = 350
                    print str(pulse) + "a1"
                    self._MotionInterface._Legs[4].moveAnkle(pulse)
            except ValueError:
               print incoming

            try:
                if incoming[:2] == 'a2':
                    #Move the leg
                    pulse = int(incoming.strip('a2'))
                    if pulse > 250:
                        pulse = 250
                    print str(pulse) + "a2"
                    self._MotionInterface._Legs[4].moveKnee(pulse)
            except ValueError:
                print incoming

            try:
                if incoming[:2] == 'b1':
                    #Move the leg
                    pulse = int(incoming.strip('b1'))
                    if pulse < 350:
                        pulse = 350
                    print str(pulse) + "b1"
                    self._MotionInterface._Legs[5].moveAnkle(pulse)
            except ValueError:
                print incoming

            try:
                if incoming[:2] == 'b2':
                    #Move the leg
                    pulse = int(incoming.strip('b2'))
                    if pulse > 250:
                        pulse = 250
                    print str(pulse) + "b2"
                    self._MotionInterface._Legs[5].moveKnee(pulse)
            except ValueError:
                print incoming
            try:
                if incoming[:2] == 'k1':
                    print 'Knop 1'
            except ValueError:
                print incoming

            try:
                if incoming[:2] == 'k0':
                    print 'Knop 0'
            except ValueError:
                print incoming

    def exit(self):
        #self._Semaphore.acquire()
        self._Exited = True
        #self._Semaphore.release()

        self._MotionInterface.raiseLegs(self._ForwardLegs)
        self._MotionInterface.MoveLegsBackward(self._ForwardLegs, True, [self._MotionInterface.convertPulseToDegrees((self._ForwardLegs[0].getHip() - 375)), 0])
        self._MotionInterface.LowerLegs(self._ForwardLegs)

        self._MotionInterface.raiseLegs(self._middleLegs)
        self._MotionInterface.MoveLegsBackward(self._middleLegs, True, [20, 0])
        self._MotionInterface.LowerLegs(self._middleLegs)

        self._MotionInterface.setSpeed(self._DefaultSpeed)
            
