__author__ = 'Teake'

import time
import threading
import math
from threading import Thread


class BalloonRace(object):


    def __init__(self, _MInterface):
        self._MInterface = _MInterface
        self._LastCommand = 9
        self._MaxAngle = 50
        self.ForwardLegs = [self._MInterface._Legs[4], self._MInterface._Legs[5]]
        self.group = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[1], self._MInterface._Legs[3]]
        self.group1 = [self._MInterface._Legs[0], self._MInterface._Legs[2]]
        self.group2 = [self._MInterface._Legs[1], self._MInterface._Legs[3]]
        self._MInterface.setLength(160)
        self._MInterface.setHeight(40)
        self.StopLegs()

        self._MInterface.raiseLegs(self.ForwardLegs)
        self._MInterface.MoveLegsForward(self.ForwardLegs, True, [0, 100])
        self._MInterface.LowerLegs(self.ForwardLegs)

        startposAnkle = self.ForwardLegs[0].getAnkle()

        steps = 100
        for step in range(1, steps):
            for Leg in self.ForwardLegs:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 250, step, steps))

            time.sleep(self._MInterface.SleepTime)

        self._MInterface.setMultiplier(4)

    def executeCommand(self, Command):
        Command = int(Command)

        if Command == 9:
            self._LastCommand = 9;
            self._MInterface.set_CurrentCommand(10)
            self.StopLegs()
            self._LastCommand = 10;
        elif Command == 10:
            self.StopLegs()
            self._LastCommand = 10;
        elif Command == 11:
            self.Forward()
            self._LastCommand = 11
        elif Command == 12:
            self.Forward(0, -25)
            self._LastCommand = 12
        elif Command == 13:
            self.Forward(0, -35)
            self._LastCommand = 13
        elif Command == 14:
            self.Backward(0, -25)
            self._LastCommand = 14
        elif Command == 15:
            self.Backward()
            self._LastCommand = 15
        elif Command == 16:
            self.Backward(-35, 0)
            self._LastCommand = 16
        elif Command == 17:
            self.Forward(-35, 0)
            self._LastCommand = 17
        elif Command == 18:
            self.Forward(-25, 0)
            self._LastCommand = 18


    def StopLegs(self):
        # laatste pootbeweging
        if self._LastCommand == 9:
            self._MInterface.LowerLegs(self.group)
        elif self._LastCommand == 11:
            self._MInterface.raiseLegs(self.group)
            self._MInterface.MoveLegsForward(self.group, False, [-self._MaxAngle, 0])
            self._MInterface.LowerLegs(self.group)
        else:
            pass


    def exit(self):
        self.group = self._MInterface._Legs
        self._MInterface.setHeight(75)
        self._MInterface.setLength(65)
        self.StopLegs()


    def Forward(self, offsetLeft=0, offsetRight=0):
        if self._LastCommand == 10:
            self.StopLegs()
            self._MInterface.raiseLegs(self.group)

            leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group1, True, [0, self._MaxAngle + offsetLeft]))
            leg1Thread.start()
            leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group2, True, [0, self._MaxAngle + offsetRight]))
            leg2Thread.start()

            leg1Thread.join()
            leg2Thread.join()

            self._MInterface.LowerLegs(self.group)


        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group1, True, [self._MaxAngle, -self._MaxAngle + offsetLeft]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group2, True, [self._MaxAngle, -self._MaxAngle + offsetRight]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.raiseLegs(self.group)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group1, True, [-self._MaxAngle, self._MaxAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group2, True, [-self._MaxAngle, self._MaxAngle]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group)


    def Backward(self, offsetLeft=0, offsetRight=0):
        if self._LastCommand == 10:
            self.StopLegs()
            self._MInterface.raiseLegs(self.group)

            leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group1, True, [0, -self._MaxAngle + offsetLeft]))
            leg1Thread.start()
            leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group2, True, [0, -self._MaxAngle + offsetRight]))
            leg2Thread.start()

            leg1Thread.join()
            leg2Thread.join()

            self._MInterface.LowerLegs(self.group)


        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group1, True, [-self._MaxAngle, self._MaxAngle + offsetLeft]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group2, True, [-self._MaxAngle, self._MaxAngle + offsetRight]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.raiseLegs(self.group)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group1, True, [self._MaxAngle, -self._MaxAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group2, True, [self._MaxAngle, -self._MaxAngle]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group)