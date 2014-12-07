__author__ = 'Ivar'

from Servo import Servo

class Leg(object):
    """
    Setting the addresses, channels and default position of the 3 servos of the leg.
    """

    def __init__(self, AddressArray, ChannelArray, DefaultPulseArray, inverse=False, offset=[0,0,0]):
        self._AddressArray = AddressArray
        self._ChannelArray = ChannelArray
        self._DefaultPulseArray = DefaultPulseArray
        self._inverse = inverse
        self._offset = offset

    # Receiving variables, this will be set into arrays. If there aren't 3 input variables of the address
    # it will print an Error.
        if len(self._AddressArray) == 3:
            self._Hip = Servo(self._AddressArray[0], self._ChannelArray[0], self._DefaultPulseArray[0], self._inverse, self._offset[0])
            self._Knee = Servo(self._AddressArray[1], self._ChannelArray[1], self._DefaultPulseArray[1], self._inverse, self._offset[1])
            self._Ankle = Servo(self._AddressArray[2], self._ChannelArray[2],self._DefaultPulseArray[2], self._inverse, self._offset[2]) #3 keer nul? aangepast naar 0,1,2
        else:
            print "-----------Error Creating leg-----------"

    # Setting the Hip to the position of the given pulse
    def moveHip(self, Pulse):
        self._Hip.setPulse(Pulse)

    # Setting the Knee to the position of the given pulse
    def moveKnee(self, Pulse):
        self._Knee.setPulse(Pulse)

    # Setting the Ankle to the position of the given pulse
    def moveAnkle(self, Pulse):
        self._Ankle.setPulse(Pulse)

    # Setting the full Leg to the starting position of 375 pulses
    def defaultPos(self):
        self.moveHip(self._Hip, self._DefaultPulseArray[0])
        self.moveKnee(self._Knee, self._DefaultPulseArray[1])
        self.moveAnkle(self._Ankle, self._DefaultPulseArray[2])

    def getHip(self):
        return self._Hip.getPulse()

    def getKnee(self):
        return self._Knee.getPulse()

    def getAnkle(self):
        return self._Ankle.getPulse()
        
       

