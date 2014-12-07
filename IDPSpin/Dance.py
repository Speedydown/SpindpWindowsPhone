__author__ = 'Matthe Jacobs'

import time
import threading
import math
from threading import Thread


class Dance(object):
    def __init__(self, _MInterface):
        self._MInterface = _MInterface        
        self.sleepTime = (0.01)
        self.group1 = [self._MInterface._Legs[0], self._MInterface._Legs[3], self._MInterface._Legs[4]]
        self.group2 = [self._MInterface._Legs[1], self._MInterface._Legs[2], self._MInterface._Legs[5]]
        self.allLegs = [self._MInterface._Legs[0], self._MInterface._Legs[1], self._MInterface._Legs[2],
                        self._MInterface._Legs[3], self._MInterface._Legs[4], self._MInterface._Legs[5]]
            
    def exit(self):
        self._MotionInterface.setHeight(75)
        self._MotionInterface.LowerLegs(self.Legs)

    def executeCommand(self, Command):

        Command = int(Command)

        if Command == 30:
            self.dance()
            self._MInterface.set_CurrentCommand(10)

    #Calling dance methods
    def dance(self):
        
        self.doMoveStamp(1)
        time.sleep(self.sleepTime)
        
        self.doMoveStamp(2)
        time.sleep(self.sleepTime)

        self.doMoveGoLow()
        time.sleep(self.sleepTime)
            
        self.doMoveWaveLeg()
        time.sleep(self.sleepTime)
        
        self.doMoveRaiseSingle(True)
        time.sleep(self.sleepTime)
        
        self.doMoveRaiseSingle(False)
        time.sleep(self.sleepTime)

        self.doMoveBig()
        time.sleep(self.sleepTime)
            
        self.doMoveWaveLeg()
        time.sleep(self.sleepTime)
        
        #self.doMoveWave()
        time.sleep(self.sleepTime)
        
        self.doMoveFourLegs()
        time.sleep(self.sleepTime)

        self.doMoveHip()
        time.sleep(self.sleepTime)

        self.doMoveWiggle()
        time.sleep(self.sleepTime)

        self.doMoveUpDown()
        time.sleep(self.sleepTime)

        self.doMoveWaveLegTwo()
        time.sleep(self.sleepTime)

        self.doMoveEnd()
        time.sleep(self.sleepTime)

    def doMoveStepForward(self):
        self._MInterface.raiseLegs(self.group2)
        self._MInterface.MoveLegsForward(self.group2, True, [0, self._MaxAngle])
        self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)

        self._MInterface.MoveLegsForward, args = (self.group1, True, [0, self._MaxAngle])
        self._MInterface.MoveLegsBackward, args = (self.group2, False, [self._MaxAngle, 0])

        self._MInterface.LowerLegs(self.group1)
        self._MInterface.raiseLegs(self.group2)

        self._MInterface.MoveLegsForward, args = (self.group2, True,[0, self._MaxAngle])
        self._MInterface.MoveLegsBackward, args = (self.group1, False, [self._MaxAngle, 0])

        self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)
        self._MInterface.MoveLegsBackward(self.group2, False, [self._DefaultMaxAngle, 0])
        self._MInterface.LowerLegs(self.group1)

    def doMoveStepBackward(self):
        self._MInterface.raiseLegs(self.group2)
        self._MInterface.MoveLegsBackward(self.group2, True, [0, -self._MaxAngle])
        self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)
        
        self._MInterface.MoveLegsBackward, args = (self.group1, True, [0, -self._MaxAngle],)
        self._MInterface.MoveLegsForward, args = (self.group2, False, [-self._MaxAngle, 0],)

        self._MInterface.LowerLegs(self.group1)
        self._MInterface.raiseLegs(self.group2)

        self._MInterface.MoveLegsBackward, args = (self.group2, True, [0, -self._MaxAngle],)
        self._MInterface.MoveLegsForward, args = (self.group1, False, [-self._MaxAngle, 0],)

        self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)
        self._MInterface.MoveLegsForward(self.group2, False, [-self._MaxAngle, 0])
        self._MInterface.LowerLegs(self.group1)
  
        
    #Do a wave with all 6 legs. First lower the 1st two than 2nd two etc.
    def doMoveWave(self):
        pass

    def doMoveWiggle(self):
        group1 = [self._MInterface._Legs[0], self._MotionInterface._Legs[2], self._MotionInterface._Legs[4]]
        group2 = [self._MInterface._Legs[1], self._MotionInterface._Legs[3], self._MotionInterface._Legs[5]]

        self._MInterface.setHeight(45)

        self._MInterface.MoveLegsForward(group1, True, [0, 30])
        self._MInterface.MoveLegsBackward(group2, True, [0, 30])
        self._MInterface.MoveLegsForward(group2, True, [0, 60])
        self._MInterface.MoveLegsBackward(group1, True, [0, 60])
        self._MInterface.MoveLegsForward(group1, True, [0, 60])
        self._MInterface.MoveLegsBackward(group2, True, [0, 60])
        self._MInterface.MoveLegsForward(group2, True, [0, 60])
        self._MInterface.MoveLegsBackward(group1, True, [0, 60])
        self._MInterface.MoveLegsForward(group2, True, [0, 30])
        self._MInterface.MoveLegsBackward(group1, True, [0, 30])

        self._LowerLegs(allLegs)

        self._MInterface.setHeight(75)

        

    def doMoveBig(self):
        self._MInterface.setHeight(40)
        self._MInterface.setLength(150)

        angle = 50

        self._MotionInterface.MoveLegsForward(allLegs, False, [0, angle])
        self._MotionInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MotionInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MotionInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MotionInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MotionInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MotionInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MotionInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MotionInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MotionInterface.MoveLegsBackward(allLegs, False, [angle, 0])

        self._MInterface.setHeight(75)
        self._MInterface.setLength(65)
        
        self._LowerLegs(allLegs)

            
    #Wave with 1 leg
    def doMoveWaveLeg(self):
        self._MInterface.raiseLegs([allLegs[5]], [-450, 90])
        self._MInterface.MoveLegsForward([allLegs[5]], False, [0, 90])

        self._MInterface.raiseLegs([allLegs[5]], [-450, 120])
        self._MInterface.raiseLegs([allLegs[5]], [-450, 90])
        self._MInterface.raiseLegs([allLegs[5]], [-450, 70])
        self._MInterface.raiseLegs([allLegs[5]], [-450, 90])
        self._MInterface.raiseLegs([allLegs[5]], [-450, 120])

        self._MInterface.LowerLegs([allLegs[5]])
        

    #Raises the 2 front legs and waves with them.
    def doMoveWaveLegTwo(self):
        group1 = [self._MotionInterface._Legs[0], self._MotionInterface._Legs[2], self._MotionInterface._Legs[4]]
        group2 = [self._MotionInterface._Legs[1], self._MotionInterface._Legs[3], self._MotionInterface._Legs[5]]

        self._MInterface.setHeight(55)
        
        self._MInterface.raiseLegs([group1[2], group2[2]])
        self._MInterface.MoveLegsForward([group1[2], group2[2]], True, [0, 30])

        self._MInterface.raiseLegs([group1[2], group2[2]], [0, 110])
        self._MInterface.raiseLegs([group1[2], group2[2]], [0, 90])
        self._MInterface.raiseLegs([group1[2], group2[2]], [0, 110])

        self._MInterface.LowerLegs([group1[2], group2[2]])

        self._MInterface.setHeight(75)

    def doMoveGoLow(self):
        self._MInterface.setHeight(55)
        
        self._MInterface.raiseLegs([self.group1[2], self.group2[2]])
        time.sleep(0.5)
        self._MInterface.raiseLegs([self.group1[1], self.group2[1]])
        time.sleep(0.5)
        self._MInterface.raiseLegs([self.group1[0], self.group2[0]])
        time.sleep(0.5)

        for x in range(0, 5):
            self._MInterface.raiseLegs([self.group1[x], self.group2[x]], [0, 110])
            self._MInterface.raiseLegs([self.group1[x], self.group2[x]], [0, 90])
            self._MInterface.raiseLegs([self.group1[x], self.group2[x]], [0, 110])
            time.sleep(0.5)

        self._MInterface.setHeight(75)

        self.MInterface.LowerLegs(self.allLegs)
        

    #Only move the hips
    def doMoveHip(self):
        angle = 20

        self._MInterface.MoveLegsForward(allLegs, False, [0, angle])
        self._MInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MInterface.MoveLegsBackward(allLegs, False, [angle, -angle])
        self._MInterface.MoveLegsForward(allLegs, False, [-angle, angle])
        self._MInterface.MoveLegsBackward(allLegs, False, [angle, 0])
                

    #The whole spin moves up and down
    def doMoveUpDown(self):
        self._MInterface.setHeight(55)
        time.sleep(sleepTime)
        self._MInterface.setHeight(180)
        time.sleep(sleepTime)
        self._MInterface.setHeight(75)
        
        
    #Spider stands on 4 legs
    def doMoveFourLegs(self):
        group = [self._MInterface._Legs[2], self._MInterface._Legs[3]]
        self._MInterface.raiseLegs(group)
        time.sleep(2)
        self._MInterface.LowerLegs(group)

    #4 Legs in the air and wave with them
    def doMoveFourAir(self):
        self._MInterface.setHeight(55)

        group = [allLegs[5]], [allLegs[4]], [allLegs[0]], [allLegs[1]]

        startpulseAnkle = Legs[0].getAnkle()        

        self._MInterface.raiseLegs(group, [-450, 90])
        self._MInterface.raiseLegs(group, [-450, 120])
        self._MInterface.raiseLegs(group, [-450, 90])
        self._MInterface.raiseLegs(group, [-450, 70])
        self._MInterface.raiseLegs(group, [-450, 110])

        self._MInterface.LowerLegs(group)
            
        
    #Raise and lower all 6 legs one by one
    def doMoveRaiseSingle(self, Start):        
        if(Start):
            for x in range(0, 6):
                array = [self.allLegs[x]]
                self._MInterface.raiseLegs(array, [0, 110])
                time.sleep(0.5)
                self._MInterface.LowerLegs(array)
                time.sleep(0.5)
        else:
            for x in range(5, -1, -1):
                array = [self.allLegs[x]]
                self._MInterface.raiseLegs(array, [0, 110])
                time.sleep(0.5)
                self._MInterface.LowerLegs(array)
                time.sleep(0.5)


    #Raise leg 1, 4, 6 and lower. After that same thing with 2, 3, 5
    def doMoveStamp(self, group):
        if(group == 1):
            self._MInterface.raiseLegs(self.group2, [0, 110])
            time.sleep(1)
            self._MInterface.LowerLegs(self.group2)
        else:
            self._MInterface.raiseLegs(self.group1, [0, 110])
            time.sleep(1)
            self._MInterface.LowerLegs(self.group1)

    def doMoveEnd(self):
        group1 = [self._MotionInterface._Legs[0], self._MotionInterface._Legs[2], self._MotionInterface._Legs[4]]
        group2 = [self._MotionInterface._Legs[1], self._MotionInterface._Legs[3], self._MotionInterface._Legs[5]]

        steps = 50

        self._MotionInterface.raiseLegs([group1[1], group2[1]])
        self._MotionInterface.MoveLegsForward([group1[1], group2[1]], True, [0,30])
        self._MotionInterface.LowerLegs([group1[1], group2[1]])

        self._MotionInterface.raiseLegs([group1[2], group2[2]], [-450, 90])
        self._MotionInterface.MoveLegsForward([group1[2], group2[2]], True, [0, 90])

        self._MotionInterface.raiseLegs([group1[0], group2[0]], [-300, 0])
