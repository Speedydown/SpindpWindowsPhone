__author__ = 'Teake'

import time
import threading
import math
from threading import Thread


class SpiderGap2(object):


    def __init__(self, _MInterface):
        self._MInterface = _MInterface
        self._LastCommand = 9
        self._MaxAngle = 100
        self.ForwardLegs = [self._MInterface._Legs[4], self._MInterface._Legs[5]]
        self.group = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[1], self._MInterface._Legs[3]]
        self.group1 = [self._MInterface._Legs[0], self._MInterface._Legs[2]]
        self.group2 = [self._MInterface._Legs[1], self._MInterface._Legs[3]]
        self._MInterface.setLength(160)
        self._MInterface.setHeight(40)

        group = self._MInterface._Legs
        angle = 100

        self._MInterface.setMultiplier(1)
        self._MInterface.raiseLegs(group)
        self._MInterface.MoveLegsForward(group, False, [0,angle])
        self._MInterface.LowerLegs(group)

        self._MInterface.MoveLegsBackward(group, True, [angle, -angle])
        self._MInterface.raiseLegs(group)

        self._MInterface.MoveLegsForward(group, False, [-angle, angle])
        self._MInterface.LowerLegs(group)


        #copy
        self._MInterface.MoveLegsBackward(group, True, [angle, -angle])
        self._MInterface.raiseLegs(group)

        self._MInterface.MoveLegsForward(group, False, [-angle, angle])
        self._MInterface.LowerLegs(group)
        self._MInterface.MoveLegsBackward(group, True, [angle, -angle])
        self._MInterface.raiseLegs(group)

        self._MInterface.MoveLegsForward(group, False, [-angle, angle])
        self._MInterface.LowerLegs(group)
        self._MInterface.MoveLegsBackward(group, True, [angle, -angle])
        self._MInterface.raiseLegs(group)

        self._MInterface.MoveLegsForward(group, False, [-angle, angle])
        self._MInterface.LowerLegs(group)

    def executeCommand(self, Command):
        pass


    def exit(self):
     self._MotionInterface.setHeight(75)
     self._MotionInterface.setLength(65)
     self._MotionInterface.LowerLegs(self.Legs)
