#The class to control only one leg
__author__ = 'Matthe Jacobs'


from MotionInterface import MotionInterface

class SingleLeg(self, MotionInterface):
    def __init__(self, ):
        MotionInterface.__init__(self)

    def ControlLeg1(self, pulseHip, pulseKnee, pulseAnkle):
        moveLeg(1, pulseHip, pulseKnee, pulseAnkle)

    def ControlLeg2(self, pulseHip, pulseKnee, pulseAnkle):
        moveLeg(2, pulseHip, pusleKnee, pulseAnkle)

    def ControlLeg3(self, pulseHip, pusleKnee, pulseAnkle):
        moveLeg(3, pulseHip, pulseKnee, pulseAnkle)

    def ControlLeg4(self, pulseHip, pusleKnee, pulseAnkle):
        moveLeg(4, pulseHip, pulseKnee, pulseAnkle)

    def ControlLeg5(self, pulseHip, pusleKnee, pulseAnkle):
        moveLeg(5, pulseHip, pulseKnee, pulseAnkle)

    def ControlLeg6(self, pulseHip, pulseKnee, pulseAnkle):
        moveLeg(6, pulseHip, pulseKnee, pulseAnkle)

    #Function to move the leg
    def moveLeg(self, legNum, pulseHip, pulseKnee, pulseAnkle):    
        if legNum == 1:
            MotionInterface.Legs[0].moveHip(pulseHip)
            MotionInterface.Legs[0].moveKnee(pulseKnee)
            MotionInterface.Legs[0].moveAnkle(pulseAnkle)
        elif legNum == 2:
            MotionInterface.Legs[1].moveHip(pulseHip)
            MotionInterface.Legs[1].moveKnee(pulseKnee)
            MotionInterface.Legs[1].moveAnkle(pulseAnkle)
        elif legNum == 3:
            MotionInterface.Legs[2].moveHip(pulseHip)
            MotionInterface.Legs[2].moveKnee(pulseKnee)
            MotionInterface.Legs[2].moveAnkle(pulseAnkle)
        elif legNum == 4:
            MotionInterface.Legs[3].moveHip(pulseHip)
            MotionInterface.Legs[3].moveKnee(pulseKnee)
            MotionInterface.Legs[3].moveAnkle(pulseAnkle)
        elif legNum == 5:
            MotionInterface.Legs[4].moveHip(pulseHip)
            MotionInterface.Legs[4].moveKnee(pulseKnee)
            MotionInterface.Legs[4].moveAnkle(pulseAnkle)
        elif legNum == 6:
            MotionInterface.Legs[5].moveHip(pulseHip)
            MotionInterface.Legs[5].moveKnee(pulseKnee)
            MotionInterface.Legs[5].moveAnkle(pulseAnkle)
