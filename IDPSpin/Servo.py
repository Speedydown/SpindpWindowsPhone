__author__ = 'Ivar'
try:
    from Adafruit_PWM_Servo_Driver import PWM
except ImportError:
    print "my guess is you are running windows or your PWM driver is not correctly configured"

class Servo(object):
    """
    Setting the channels, address, startingPulse and frequency to create an servo.
    Using the Adafruit PWM servo driver to set the min and max Pulse of the servo.
    """
    def __init__(self, address, channel, startingPulse, inverse=False, offset=0):
    # Constructor
        self.pulse = startingPulse
        self.channel = channel
        self.address = address
        self.freq = 60
        self.maxPulse = 600
        self.minPulse = 150
        self.inverse = inverse
        self.offset = offset
        
        try:
            self.pwm = PWM(address)
            self.pwm.setPWMFreq(self.freq)
            self.setPulse(startingPulse)
        except:
            pass
        

    def setPulse(self, pulse):
        pulse  + self.offset
        # Setting the area of pulses between 150 and 600. If the input is bigger then 600 pulses
        # it will be set to the max 600 pulses. If pulses are lower then 150 it will be set tot 150 pulses

        if pulse > self.maxPulse:
            pulse = self.maxPulse
        elif pulse < self.minPulse:
            pulse = self.minPulse

        if self.inverse == True:
            pulse = pulse - 150
            #calculate difference
            difference = 225 - pulse
            pulse = 375 + difference

        try:
            self.pwm.setPWM(self.channel, 0, pulse) # 0 means: zero pulse away from input pulse.
        except:
            #print "moved servo " + str(self.address) + " " + str(self.channel) + " to: " + str(pulse)
            pass
        self.pulse = pulse                 # setting the input pulse

    def getPulse(self):
        if self.inverse == True:
            pulse = self.pulse - 150
            #calculate difference
            difference = 225 - pulse
            pulse = 375 + difference

            return pulse - self.offset

        return self.pulse
