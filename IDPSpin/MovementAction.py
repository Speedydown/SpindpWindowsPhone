class MovementAction(object):

    def __init__(self, startingPulse, endPulse):
        self._StartingPulse = startingPulse
        self._EndPulse = endPulse

    def getStartPulse(self):
        return self._StartingPulse

    def getEndPulse(self):
        return self._EndPulse



