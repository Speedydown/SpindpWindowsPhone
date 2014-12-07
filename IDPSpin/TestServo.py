__author__ = 'Ivar'

from Leg import Leg
import time

Leg1 = Leg(["0x40", "0x40", "0x40"], [0, 1, 3], [375, 375, 375])

while (True):
  # Change speed of continuous servo on channel O
  #angle = int(raw_input("Angle 150 to 600: "))
  #Leg1.moveHip(angle)
  Leg1.moveKnee(475)
  Leg1.moveAnkle(475)
  time.sleep(1)
  Leg1.moveHip(475)
  time.sleep(1)
  Leg1.moveKnee(275)
  Leg1.moveAnkle(275)
  time.sleep(1)
  Leg1.moveHip(275)
  time.sleep(1)

