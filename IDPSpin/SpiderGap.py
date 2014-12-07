__author__ = 'Ivar'

import time
import threading
import math

from threading import Thread

class SpiderGap(object):

    def __init__(self, _MInterface):
        self._MInterface = _MInterface
        self.SleepTime = 0.05

        self.group1 = [self._MInterface._Legs[0], self._MInterface._Legs[1]]#achterpoten
        self.group2 = [self._MInterface._Legs[2], self._MInterface._Legs[3]]
        self.group3 = [self._MInterface._Legs[4], self._MInterface._Legs[5]]#voorpoten


        leg1Thread = threading.Thread(target=self.PullLegsForward)
        leg1Thread.start()

    def executeCommand(self, Command):
        Command = int(Command)

        if Command == 3:
            self.PullLegsForward()

    def exit(self):
        pass #exit methode

    def PullLegsForward(self):
        #groups = [self.group1, self.group2, self.group3]
        AnkleStartpoint = 375
        KneeStartpoint = 375
        HipStartpoint = 375

        steps = 50

        for step in range(1, steps):
            for Leg in self.group1:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(AnkleStartpoint, 225, step, steps))
                #Leg.moveKnee(self._MInterface.calculateVerticalPulse(KneeStartpoint, 375, step, steps))
            time.sleep(self.SleepTime)

        self._MInterface.MoveLegsBackward(self.group1, True, [0, -100])


        #for step in range(1, 20):
            #for Leg in self.group1:

               # Leg.moveHip(self._MInterface.calculateVerticalPulse(HipStartpoint, 175, step, steps))
           # time.sleep(self.SleepTime)

        for step in range(1, steps):
            for Leg in self.group2:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(AnkleStartpoint, 200, step, steps))
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(KneeStartpoint, 200, step, steps))
            time.sleep(self._MInterface.SleepTime)

        for step in range(1, 20):
            for Leg in self.group2:
                Leg.moveHip(self._MInterface.calculateVerticalPulse(HipStartpoint, 375, step, steps))
            time.sleep(self.SleepTime)

        for step in range(1, steps):
            for Leg in self.group3:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(AnkleStartpoint, 225, step, steps))
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(KneeStartpoint, 375, step, steps))
            time.sleep(self.SleepTime)

        self._MInterface.MoveLegsForward(self.group3, True, [0, 100])


        #for step in range(1, 20):
         #   for Leg in self.group3:
          #      Leg.moveHip(self._MInterface.calculateVerticalPulse(HipStartpoint, 550, step, steps))
           # time.sleep(self.SleepTime)

        """
        for step in range(1, steps):
            for Leg in self.group1:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(225, 200, step, steps))
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(375, 125, step, steps))
            time.sleep(self.SleepTime)

        for step in range(1, 20):
            for Leg in self.group1:
                Leg.moveHip(self._MInterface.calculateVerticalPulse(225, 225, step, steps))
            time.sleep(self.SleepTime)

        for step in range(1, steps):
            for Leg in self.group3:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(500, 125, step, steps))
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(375, 125, step, steps))
            time.sleep(self.SleepTime)

        for step in range(1, 20):
            for Leg in self.group3:
                Leg.moveHip(self._MInterface.calculateVerticalPulse(575, 575, step, steps))
            time.sleep(self.SleepTime)
        """













