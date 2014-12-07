__author__ = 'Speedy'

import time
import math
import threading
from threading import Thread

class Dance2(object):

 def __init__(self, _MotionInterface):
    self._MotionInterface = _MotionInterface
    self.SleepTime = 0.02

    self.WaveLegs = [self._MotionInterface._Legs[0], self._MotionInterface._Legs[2], self._MotionInterface._Legs[4], self._MotionInterface._Legs[5], self._MotionInterface._Legs[3], self._MotionInterface._Legs[1]]
    self.Legs = self._MotionInterface._Legs

    leg1Thread = threading.Thread(target=self.Dance)
    leg1Thread.start()

 def executeCommand(self, Command):
    pass

 def Dance(self):
     #wave
     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(self.Legs)

     self.ivar()
     self.waveSingleLeg()
     self.moveUP()
     self.shake(10)
     self.forwardBackward(3)
     self.rotate()
     self.forwardBackward(3)
     self.shake(10)
     self.ivar()
     self.waveSingleLeg()
     self.forwardLegs()

     #self._MotionInterface.LowerLegs(self.Legs)

 def forwardLegs(self):
     self._MotionInterface.setMultiplier(1)
     group1 = [self._MotionInterface._Legs[0], self._MotionInterface._Legs[2], self._MotionInterface._Legs[4]]
     group2 = [self._MotionInterface._Legs[1], self._MotionInterface._Legs[3], self._MotionInterface._Legs[5]]

     steps = 50

     self._MotionInterface.raiseLegs([group1[1], group2[1]])
     self._MotionInterface.MoveLegsForward([group1[1], group2[1]], True, [0,30])
     self._MotionInterface.LowerLegs([group1[1], group2[1]])

     self._MotionInterface.raiseLegs([group1[2], group2[2]], [-450, 90])
     self._MotionInterface.MoveLegsForward([group1[2], group2[2]], True, [0, 90])

     self._MotionInterface.raiseLegs([group1[0], group2[0]], [-300, 0])

     for i in range(0, 3):
         self._MotionInterface.MoveLegsBackward([group1[2], group2[2]], True, [90, 60])
         time.sleep(0.5)
         self._MotionInterface.MoveLegsForward([group1[2], group2[2]], True, [60, 90])
         time.sleep(0.5)

 def moveUP(self):
    self._MotionInterface.setMultiplier(1)

    for i in range(0, 3):
        self._MotionInterface.setLength(65)
        self._MotionInterface.setHeight(55)
        self._MotionInterface.LowerLegs(self.Legs)

        steps = 50
        self._MotionInterface.setMultiplier(3)

        startposAnkle = self.WaveLegs[0].getAnkle()
        for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            for Leg in self.WaveLegs:
                Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 450, step, steps))
                time.sleep(self.SleepTime)

        startposAnkle = self.WaveLegs[0].getAnkle()

        for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            for Leg in self.WaveLegs:
                Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle - 450, step, steps))
                time.sleep(self.SleepTime)

        self._MotionInterface.setMultiplier(1)

        self._MotionInterface.setLength(160)
        self._MotionInterface.setHeight(75)
        self._MotionInterface.LowerLegs(self.Legs)

    self._MotionInterface.setLength(65)
    self._MotionInterface.setHeight(75)
    self._MotionInterface.LowerLegs(self.Legs)

 def shake(self, numberOfShakes=3):
    group = self._MotionInterface._Legs
    angle = 20

    if numberOfShakes < 1:
        numberOfShakes = 1

    self._MotionInterface.setMultiplier(2)

    self._MotionInterface.MoveLegsForward(group, False, [0, angle])
    for i in range(0, numberOfShakes):
        self._MotionInterface.MoveLegsBackward(group, False, [angle, -angle])
        self._MotionInterface.MoveLegsForward(group, False, [-angle, angle])
    self._MotionInterface.MoveLegsBackward(group, False, [angle, 0])

    self._MotionInterface.setMultiplier(1)

 def waveSingleLeg(self):

     self._MotionInterface.setHeight(55)
     self._MotionInterface.LowerLegs(self.Legs)
     self._MotionInterface.setMultiplier(3)

     steps = 50

     for Leg in self.WaveLegs:
         startposAnkle = Leg.getAnkle()

         for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 450, step, steps))
            time.sleep(self.SleepTime)

     self._MotionInterface.setMultiplier(1)

     for i in range(0, 3):
         self._MotionInterface.MoveLegsForward(self.WaveLegs, False, [ 0, 55])
         self._MotionInterface.MoveLegsBackward(self.WaveLegs, False, [ 55, -55])
         self._MotionInterface.MoveLegsForward(self.WaveLegs, False, [ -55, 0])

     self._MotionInterface.setMultiplier(3)

     for Leg in reversed(self.WaveLegs):
         startposAnkle = Leg.getAnkle()

         for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle - 450, step, steps))
            time.sleep(self.SleepTime)

     self._MotionInterface.setMultiplier(1)

     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(self.Legs)

 def ivar(self):
     self._MotionInterface.setMultiplier(1)
     self._MotionInterface.setHeight(55)
     self._MotionInterface.LowerLegs(self.Legs)

     self._MotionInterface.MoveLegsBackward([self.Legs[0], self.Legs[1]], False, [ 0, -100])
     self._MotionInterface.MoveLegsForward([self.Legs[4], self.Legs[5]], False, [ 0, 100])

     self._MotionInterface.setMultiplier(2)

     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(self.Legs)

     steps = 50

     for i in range(0,5):
         self._MotionInterface.setHeight(55)
         self._MotionInterface.LowerLegs(self.Legs)

         if i % 2 == 1:
            tempgroup = [self.Legs[0], self.Legs[5]]
         else:
            tempgroup = [self.Legs[1], self.Legs[4]]

         startposAnkle = tempgroup[0].getAnkle()
         for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            for Leg in tempgroup:

                Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 450, step, steps))
                time.sleep(self.SleepTime)

         time.sleep(1)

         startposAnkle = tempgroup[0].getAnkle()

         for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
            for Leg in tempgroup:
                Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle - 450, step, steps))
                time.sleep(self.SleepTime)

         self._MotionInterface.setHeight(75)
         self._MotionInterface.LowerLegs(self.Legs)

     self._MotionInterface.setMultiplier(1)

 def forwardBackward(self, count=3):
     group = self._MotionInterface._Legs
     angle = 50

     self._MotionInterface.setLength(160)
     self._MotionInterface.setHeight(40)
     self._MotionInterface.LowerLegs(group)
     self._MotionInterface.setMultiplier(3)

     self._MotionInterface.raiseLegs(group)
     self._MotionInterface.MoveLegsForward(group, False, [0,angle])
     self._MotionInterface.LowerLegs(group)

     for i in range(0, count):
        self._MotionInterface.MoveLegsBackward(group, True, [angle, -angle])

        self._MotionInterface.raiseLegs(group)
        self._MotionInterface.MoveLegsForward(group, False, [-angle, angle])
        self._MotionInterface.LowerLegs(group)

     for i in range(0, count):
        self._MotionInterface.raiseLegs(group)
        self._MotionInterface.MoveLegsBackward(group, True, [angle, -angle])
        self._MotionInterface.LowerLegs(group)

        self._MotionInterface.MoveLegsForward(group, False, [-angle, angle])

     self._MotionInterface.raiseLegs(group)
     self._MotionInterface.MoveLegsBackward(group, True, [angle, 0])
     self._MotionInterface.LowerLegs(group)

     self._MotionInterface.setMultiplier(1)
     self._MotionInterface.setLength(65)
     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(group)

 def rotate(self):
     group = self._MotionInterface._Legs
     group1 = [group[0], group[2], group[4]]
     group2 = [group[1], group[3], group[5]]

     angle = 50
     steps = 50
     self._MotionInterface.setLength(160)
     self._MotionInterface.setHeight(40)
     self._MotionInterface.LowerLegs(group)
     self._MotionInterface.setMultiplier(3)

     startposAnkle = group1[0].getAnkle()
     for step in range(1, steps, 1 * self._MotionInterface.getMultiplier()):
        for Leg in group1:
            Leg.moveAnkle(self._MotionInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 450, step, steps))
            time.sleep(self.SleepTime)

     self._MotionInterface.raiseLegs(group2)
     self._MotionInterface.MoveLegsForward(group2, False, [0,angle])
     self._MotionInterface.LowerLegs(group2)

     for i in range(0, 8):
        self._MotionInterface.MoveLegsBackward(group2, True, [angle, -angle])

        self._MotionInterface.raiseLegs(group2)
        self._MotionInterface.MoveLegsForward(group2, False, [-angle, angle])
        self._MotionInterface.LowerLegs(group2)

     self._MotionInterface.MoveLegsBackward(group2, True, [angle, 0])


     self._MotionInterface.setMultiplier(1)
     self._MotionInterface.setLength(65)
     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(group)




 def exit(self):
     self._MotionInterface.setHeight(75)
     self._MotionInterface.LowerLegs(self.Legs)

