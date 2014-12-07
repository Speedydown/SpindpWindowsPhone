import time
import threading
import math
from threading import Thread

class Move(object):

    def __init__(self, _MInterface):
        self._MInterface = _MInterface
        self._LastCommand = 9
        self._MaxAngle = 20
        self._MinAngle = 6
        self._DefaultMaxAngle = 20
        self._DefaultMinAngle = 6
        self._DefaultHeight = self._MInterface._Height
        self.group1 = [self._MInterface._Legs[0], self._MInterface._Legs[3], self._MInterface._Legs[4]]
        self.group2 = [self._MInterface._Legs[1], self._MInterface._Legs[2], self._MInterface._Legs[5]]

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
            self.MoveForward()
            self._LastCommand = 11
        elif Command == 12:
            self.MoveForwardAndRotate(True)
            self._LastCommand = 12
        elif Command == 13:
            self.Rotate(False)
            self._LastCommand = 13
        elif Command == 14:
            self.MoveBackwardAndRotate(True)
            self._LastCommand = 14
        elif Command == 15:
            self.MoveBackward()
            self._LastCommand = 15
        elif Command == 16:
            self.MoveBackwardAndRotate(False)
            self._LastCommand = 16
        elif Command == 17:
            self.Rotate(True)
            self._LastCommand = 17
        elif Command == 18:
            self.MoveForwardAndRotate(False)
            self._LastCommand = 18
        elif Command == 20:
            self.MoveSidways(True)
            self._LastCommand = 20
        elif Command == 21:
            self.MoveSidways(False)
            self._LastCommand == 21
        elif Command == 25:
            self.turbo()
            self._LastCommand = 25
        elif Command == 26:
            self.Elevator()
            self._LastCommand = 26


    def exit(self):
        self.StopLegs()



    def rotateLegs(self, group1, group2, group1from, group1to, group2from, group2to):

        for i in range(0, 3):
            tempgroup = [group1[i], group2[i]]
            self._MInterface.raiseLegs(tempgroup)
            self._MInterface.MoveLegsForward([tempgroup[0]], True, [group1from, group1to])
            self._MInterface.MoveLegsBackward([tempgroup[1]], True, [group2from, group2to])
            self._MInterface.LowerLegs(tempgroup)


    def Rotate(self, Left=False):
        #make groups based on rotation direction
        if (Left):
            group1 = [self._MInterface._Legs[4], self._MInterface._Legs[2], self._MInterface._Legs[0]]
            group2 = [self._MInterface._Legs[1], self._MInterface._Legs[3], self._MInterface._Legs[5]]
        else:
            group2 = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[4]]
            group1 = [self._MInterface._Legs[5], self._MInterface._Legs[3], self._MInterface._Legs[1]]

        #check if last command was also left or right, and move to start position if direction does not match
        if not(self._LastCommand == 13 or self._LastCommand == 17):
            self.StopLegs()
            self.rotateLegs(group1, group2, 0, self._MaxAngle, 0, -self._MaxAngle)
        else:
            if (self._LastCommand == 13 and Left == True) or (self._LastCommand == 17 and Left == False):
                self.StopLegs()
                self.rotateLegs(group1, group2, 0, self._MaxAngle, 0, -self._MaxAngle)


        #move legs backward
        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (group1, False, [self._MaxAngle, -self._MaxAngle],))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (group2, False, [-self._MaxAngle, self._MaxAngle],))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        #tilt legs and move them back to start position for rotation, stop command moves them back to default position if next command != rotate
        self.rotateLegs(group1, group2, -self._MaxAngle, self._MaxAngle, self._MaxAngle, -self._MaxAngle)

    def MoveForwardAndRotate(self, Right = False):

        if Right == True:
            group1 = self.group1
            group2 = self.group2
            forwardleftsidegroup1 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardrightsidegroup1 = [self._MInterface._Legs[3]]
            forwardrightsidegroup2 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardleftsidegroup2 = [self._MInterface._Legs[2]]
        else:
            group2 = self.group1
            group1 = self.group2
            forwardrightsidegroup2 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardleftsidegroup2 = [self._MInterface._Legs[3]]
            forwardleftsidegroup1 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardrightsidegroup1 = [self._MInterface._Legs[2]]

        if not(self._LastCommand == 12 or self._LastCommand == 18):
            self.StopLegs()
            self._MInterface.raiseLegs(group2)
            self._MInterface.MoveLegsForward(forwardrightsidegroup2, True, [0, self._MaxAngle])
            self._MInterface.MoveLegsForward(forwardleftsidegroup2, True, [0, self._MinAngle])
            self._MInterface.LowerLegs(group2)
        else:
            if (self._LastCommand == 12 and Right == False) or (self._LastCommand == 18 and Right == True):
                self.StopLegs()
                self._MInterface.raiseLegs(group2)
                self._MInterface.MoveLegsForward(forwardrightsidegroup2, True, [0, self._MaxAngle])
                self._MInterface.MoveLegsForward(forwardleftsidegroup2, True, [0, self._MinAngle])
                self._MInterface.LowerLegs(group2)

        self._MInterface.raiseLegs(group1)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardleftsidegroup1, True, [0, self._MinAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardrightsidegroup1, True, [0, self._MaxAngle]))
        leg2Thread.start()
        leg3Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardrightsidegroup2, False, [self._MaxAngle, 0]))
        leg3Thread.start()
        leg4Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardleftsidegroup2, False, [self._MinAngle, 0]))
        leg4Thread.start()

        leg1Thread.join()
        leg2Thread.join()
        leg3Thread.join()
        leg4Thread.join()

        self._MInterface.LowerLegs(group1)
        self._MInterface.raiseLegs(group2)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardleftsidegroup2, True, [0, self._MinAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardrightsidegroup2, True, [0, self._MaxAngle]))
        leg2Thread.start()
        leg3Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardrightsidegroup1, False, [self._MaxAngle, 0]))
        leg3Thread.start()
        leg4Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardleftsidegroup1, False, [self._MinAngle, 0]))
        leg4Thread.start()

        leg1Thread.join()
        leg2Thread.join()
        leg3Thread.join()
        leg4Thread.join()
        self._MInterface.LowerLegs(group2)

    def MoveBackwardAndRotate(self, Right = False):

        if Right == True:
            group1 = self.group1
            group2 = self.group2
            forwardleftsidegroup1 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardrightsidegroup1 = [self._MInterface._Legs[3]]
            forwardrightsidegroup2 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardleftsidegroup2 = [self._MInterface._Legs[2]]
        else:
            group2 = self.group1
            group1 = self.group2
            forwardrightsidegroup2 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardleftsidegroup2 = [self._MInterface._Legs[3]]
            forwardleftsidegroup1 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardrightsidegroup1 = [self._MInterface._Legs[2]]

        if not(self._LastCommand == 14 or self._LastCommand == 16):
            self.StopLegs()
            self._MInterface.raiseLegs(group2)
            self._MInterface.MoveLegsBackward(forwardrightsidegroup2, True, [0, -self._MaxAngle])
            self._MInterface.MoveLegsBackward(forwardleftsidegroup2, True, [0, -self._MinAngle])
            self._MInterface.LowerLegs(group2)
        else:
            if (self._LastCommand == 14 and Right == False) or (self._LastCommand == 16 and Right == True):
                self.StopLegs()
                self._MInterface.raiseLegs(group2)
                self._MInterface.MoveLegsBackward(forwardrightsidegroup2, True, [0, -self._MaxAngle])
                self._MInterface.MoveLegsBackward(forwardleftsidegroup2, True, [0, -self._MinAngle])
                self._MInterface.LowerLegs(group2)

        self._MInterface.raiseLegs(group1)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardleftsidegroup1, True, [0, -self._MinAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardrightsidegroup1, True, [0, -self._MaxAngle]))
        leg2Thread.start()
        leg3Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardrightsidegroup2, False, [-self._MaxAngle, 0]))
        leg3Thread.start()
        leg4Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardleftsidegroup2, False, [-self._MinAngle, 0]))
        leg4Thread.start()

        leg1Thread.join()
        leg2Thread.join()
        leg3Thread.join()
        leg4Thread.join()

        self._MInterface.LowerLegs(group1)
        self._MInterface.raiseLegs(group2)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardleftsidegroup2, True, [0, -self._MinAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (forwardrightsidegroup2, True, [0, -self._MaxAngle]))
        leg2Thread.start()
        leg3Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardrightsidegroup1, False, [-self._MaxAngle, 0]))
        leg3Thread.start()
        leg4Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (forwardleftsidegroup1, False, [-self._MinAngle, 0]))
        leg4Thread.start()

        leg1Thread.join()
        leg2Thread.join()
        leg3Thread.join()
        leg4Thread.join()
        self._MInterface.LowerLegs(group2)


    def StopLegs(self):
        #laatste pootbeweging
        if self._LastCommand == 11:
            self._MInterface.raiseLegs(self.group1)
            self._MInterface.MoveLegsBackward(self.group2, False, [self._DefaultMaxAngle, 0])
            self._MInterface.LowerLegs(self.group1)
        elif self._LastCommand == 9:
            self._MInterface.LowerLegs(self._MInterface._Legs)
        elif self._LastCommand == 12:
            forwardrightsidegroup2 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardleftsidegroup2 = [self._MInterface._Legs[2]]

            self._MInterface.raiseLegs(self.group1)
            self._MInterface.MoveLegsBackward(forwardrightsidegroup2, False, [self._MaxAngle, 0])
            self._MInterface.MoveLegsBackward(forwardleftsidegroup2, False, [self._MinAngle, 0])
            self._MInterface.LowerLegs(self.group1)
        elif self._LastCommand == 13:
            group2 = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[4]]
            group1 = [self._MInterface._Legs[5], self._MInterface._Legs[3], self._MInterface._Legs[1]]

            leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (group1, False, [self._MaxAngle, 0],))
            leg1Thread.start()
            leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (group2, False, [-self._MaxAngle, 0],))
            leg2Thread.start()

            leg1Thread.join()
            leg2Thread.join()

        elif self._LastCommand == 14:
            forwardrightsidegroup2 = [self._MInterface._Legs[1], self._MInterface._Legs[5]]
            forwardleftsidegroup2 = [self._MInterface._Legs[2]]

            self._MInterface.raiseLegs(self.group1)
            self._MInterface.MoveLegsForward(forwardrightsidegroup2, False, [-self._MaxAngle, 0])
            self._MInterface.MoveLegsForward(forwardleftsidegroup2, False, [-self._MinAngle, 0])
            self._MInterface.LowerLegs(self.group1)


        elif self._LastCommand == 15:
            self._MInterface.raiseLegs(self.group1)
            self._MInterface.MoveLegsForward(self.group2, False, [-self._MaxAngle, 0])
            self._MInterface.LowerLegs(self.group1)

        elif self._LastCommand == 16:
            forwardrightsidegroup1 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardleftsidegroup1 = [self._MInterface._Legs[3]]

            self._MInterface.raiseLegs(self.group2)
            self._MInterface.MoveLegsForward(forwardrightsidegroup1, False, [-self._MaxAngle, 0])
            self._MInterface.MoveLegsForward(forwardleftsidegroup1, False, [-self._MinAngle, 0])
            self._MInterface.LowerLegs(self.group2)

        elif self._LastCommand == 17:
            group1 = [self._MInterface._Legs[4], self._MInterface._Legs[2], self._MInterface._Legs[0]]
            group2 = [self._MInterface._Legs[1], self._MInterface._Legs[3], self._MInterface._Legs[5]]

            leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (group1, False, [self._MaxAngle, 0],))
            leg1Thread.start()
            leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (group2, False, [-self._MaxAngle, 0],))
            leg2Thread.start()

            leg1Thread.join()
            leg2Thread.join()
        elif self._LastCommand == 18:
            forwardrightsidegroup1 = [self._MInterface._Legs[0], self._MInterface._Legs[4]]
            forwardleftsidegroup1 = [self._MInterface._Legs[3]]


            self._MInterface.raiseLegs(self.group2)
            self._MInterface.MoveLegsBackward(forwardrightsidegroup1, False, [self._MaxAngle, 0])
            self._MInterface.MoveLegsBackward(forwardleftsidegroup1, False, [self._MinAngle, 0])
            self._MInterface.LowerLegs(self.group2)
        elif self._LastCommand == 25:
            self._MInterface.MoveLegsBackward(self._MInterface._Legs, False, [50, 0])
            self._MInterface.setHeight(75)
            self._MInterface.setLength(65)
            self._MInterface.set_CurrentCommand == 10
            self._LastCommand = 25
            self._MInterface.LowerLegs(self._MInterface._Legs)
            self._MInterface.setMultiplier(1)
        else:
            pass

    def MoveBackward(self):

        #eerste pootbeweging
        if self._LastCommand != 15:
            self.StopLegs()
            self._MInterface.raiseLegs(self.group2)
            self._MInterface.MoveLegsBackward(self.group2, True, [0, -self._MaxAngle])
            self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group1, True, [0, -self._MaxAngle],))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group2, False, [-self._MaxAngle, 0],))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group1)
        self._MInterface.raiseLegs(self.group2)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group2, True, [0, -self._MaxAngle],))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group1, False, [-self._MaxAngle, 0],))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group2)

    def MoveForward(self):

        #eerste pootbeweging
        if self._LastCommand != 11:
            self.StopLegs()
            self._MInterface.raiseLegs(self.group2)
            self._MInterface.MoveLegsForward(self.group2, True, [0, self._MaxAngle])
            self._MInterface.LowerLegs(self.group2)

        self._MInterface.raiseLegs(self.group1)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group1, True, [0, self._MaxAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group2, False, [self._MaxAngle, 0]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group1)
        self._MInterface.raiseLegs(self.group2)

        leg1Thread = threading.Thread(target=self._MInterface.MoveLegsForward, args = (self.group2, True,[0, self._MaxAngle]))
        leg1Thread.start()
        leg2Thread = threading.Thread(target=self._MInterface.MoveLegsBackward, args = (self.group1, False, [self._MaxAngle, 0]))
        leg2Thread.start()

        leg1Thread.join()
        leg2Thread.join()

        self._MInterface.LowerLegs(self.group2)

    def MoveSidways(self, Right=True):
        if Right:
            group1 = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[4]]
            group2 = [self._MInterface._Legs[1], self._MInterface._Legs[3], self._MInterface._Legs[5]]
        else:
            group2 = [self._MInterface._Legs[0], self._MInterface._Legs[2], self._MInterface._Legs[4]]
            group1 = [self._MInterface._Legs[1], self._MInterface._Legs[3], self._MInterface._Legs[5]]

        if self._LastCommand != 21 or self._LastCommand != 22:
            self.StopLegs()


        DefaultPulseAnkleGroup1 = 0 # = group1[0].getAnkle()
        DefaultPulseKneeGroup1 = 0 #= group1[0].getKnee()
        DefaultPulseAnkleGroup2 = group2[0].getAnkle()
        DefaultPulseKneeGroup2 = group2[0].getKnee()

        steps = 100

        for Leg in group1:

            for step in range(1, steps):
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1, DefaultPulseKneeGroup1 - 90  , step, steps))
                time.sleep(self._MInterface.SleepTime)

            for step in range(1, steps):
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(DefaultPulseAnkleGroup1, DefaultPulseAnkleGroup1 + 30, step, steps))
                #Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1, DefaultPulseKneeGroup1  , step, steps))
                time.sleep(self._MInterface.SleepTime)

            for step in range(1, steps):
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1 - 90, DefaultPulseKneeGroup1  , step, steps))
                time.sleep(self._MInterface.SleepTime)


        for step in range(1, steps):
            for Leg in group1:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(DefaultPulseAnkleGroup1 + 30, DefaultPulseAnkleGroup1, step, steps))
                #Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1, DefaultPulseKneeGroup1  , step, steps))

            for Leg in group2:
                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(DefaultPulseAnkleGroup2, DefaultPulseAnkleGroup2 + 30, step, steps))
                #Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup2, DefaultPulseKneeGroup2  , step, steps))
            time.sleep(0.05)

        for Leg in group2:
            for step in range(1, steps):
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1, DefaultPulseKneeGroup1 - 90  , step, steps))
                time.sleep(self._MInterface.SleepTime)

            for step in range(1, steps):

                Leg.moveAnkle(self._MInterface.calculateVerticalPulse(DefaultPulseAnkleGroup1 + 30, DefaultPulseAnkleGroup1, step, steps))
                #Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1, DefaultPulseKneeGroup1  , step, steps))

                time.sleep(self._MInterface.SleepTime)

            for step in range(1, steps):
                Leg.moveKnee(self._MInterface.calculateVerticalPulse(DefaultPulseKneeGroup1 - 90, DefaultPulseKneeGroup1  , step, steps))
                time.sleep(self._MInterface.SleepTime)


    def turbo(self, offset=0):
         group = self._MInterface._Legs
         angle = 50

         if self._LastCommand != 25:
            self.StopLegs()

            self._MInterface.setLength(160)
            self._MInterface.setHeight(40)
            self._MInterface.set_CurrentCommand(25)
            self._MInterface.setMultiplier(4)

            self._MInterface.raiseLegs(group)
            self._MInterface.MoveLegsForward(group, False, [0,angle])
            self._MInterface.LowerLegs(group)

         self._MInterface.MoveLegsBackward(group, True, [angle, -angle])

         self._MInterface.raiseLegs(group)

         self._MInterface.MoveLegsForward(group, False, [-angle, angle])
         self._MInterface.LowerLegs(group)

    def Elevator(self):

        Leg = self._MInterface._Legs[4]

        startposAnkle = Leg.getAnkle()

        steps = 100

        self._MInterface.raiseLegs([Leg])
        self._MInterface.MoveLegsForward([Leg], True, [0, 90])
        self._MInterface.LowerLegs([Leg])


        #for step in range(1, steps):
        #   Leg.moveAnkle(self._MInterface.calculateVerticalPulse(startposAnkle, startposAnkle + 450, step, steps))

        #  #Leg.moveKnee(self._MInterface.calculateVerticalPulse())
        # time.sleep(self._MInterface.SleepTime)

        time.sleep(1)

        #for step in range(1, steps):
        #   Leg.moveAnkle(self._MInterface.calculateVerticalPulse(startposAnkle + 450, startposAnkle, step, steps))
        #  #Leg.moveKnee(self._MInterface.calculateVerticalPulse())
        # time.sleep(self._MInterface.SleepTime)

        self._MInterface.raiseLegs([Leg])
        self._MInterface.MoveLegsBackward([Leg], True, [90, 0])
        self._MInterface.LowerLegs([Leg])

        self._MInterface.set_CurrentCommand(10)
        


