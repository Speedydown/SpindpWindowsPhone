import NetworkBuffer
import NetworkInterface
import SpinLog
import time
import thread
import threading
import subprocess
import NetworkInterfaceBT
from MotionInterface import MotionInterface
from GyroData import GyroData
from GetSpiData import GetSpiData
from Move import Move
from threading import Thread
from subprocess import call
from Camera import Camera
from IOPIN import IOPIN

class Controller(object):

    CommandSize = 4
    
    def __init__(self):
        print "spInOS active"
        self._networkInputBuffer = NetworkBuffer.NetworkBuffer()
        self._NetworkInterface = NetworkInterface.NetworkInterface(self._networkInputBuffer)
        self.NetworkInterfaceBT = NetworkInterfaceBT.NetworkInterfaceBT(self._networkInputBuffer)
        self._MotionInterface = MotionInterface(1)
        self._SPIData = GetSpiData()
        self._GyroData = GyroData()
        self._Log = SpinLog.SpinLog()
        self._IOPIN = IOPIN()
        self._Camera = Camera()
        self._Exit = False;
        self._Mode = 1
                
        self._NetworkInterfaceThread = threading.Thread(target=self._NetworkInterface.run)
        self._NetworkInterfaceThread.start()
        self._NetworkInterfaceBTThread = threading.Thread(target=self.NetworkInterfaceBT.run)
        self._NetworkInterfaceBTThread.start()
        self._CommandHandlerThread = threading.Thread(target=self.CommandHandler)
        self._CommandHandlerThread.start()
        self._MotionInterfaceThread = threading.Thread(target=self._MotionInterface.runThread)
        self._MotionInterfaceThread.start()

        self._IOPIN.Horn()
    
    def CommandHandler(self):
        while self._Exit == False:
            data = self._networkInputBuffer.Pop()    

            if len(str(data)) > 0:
                ID = data[:6]
                Command = data[6:10]
                self._Log.append(str(data))
                
                if Command == "prin":
                    print(data[10:])
                    self.SendResponse("Printed: " + data[11:], ID)
                elif Command == "cocl":
                    self.SendResponse(len(self._NetworkInterface._NetworkClients), ID)
                elif Command == "glog":
                    self.SendResponse(self._Log.get(), ID)
                elif Command  == "cllg":
                    self.SendResponse("Cleared log!", ID)
                    self._Log.clear()
                elif Command == "gcpu":
                    self.gcpu(ID)
                elif Command == "tsen":
                    self.SendResponse(self._MotionInterface.test(data[11:]), ID)
                elif Command == "gspi":
                    self.SendResponse(self._SPIData.getSpi(), ID)
                elif Command == "smde":
                    self._Mode = data[11:12]
                    self._MotionInterface.exit()
                    self._MotionInterfaceThread.join()

                    if self._MotionInterface._currentModeInt != self._Mode:

                        if int(self._Mode) == 1:
                            self._MotionInterface = MotionInterface(1)
                        if int(self._Mode) == 2:
                            self._MotionInterface = MotionInterface(2)
                        if int(self._Mode) == 3:
                            self._MotionInterface = MotionInterface(3)
                        if int(self._Mode) == 4:
                            self._MotionInterface = MotionInterface(4)
                        if int(self._Mode) == 5:
                            self._MotionInterface = MotionInterface(5)
                        if int(self._Mode) == 6:
                            self._MotionInterface = MotionInterface(6)
                        if int(self._Mode) == 7:
                            self._MotionInterface = MotionInterface(7)
                        if int(self._Mode) == 8:
                            self._MotionInterface = MotionInterface(8)
                        if int(self._Mode) == 9:
                            self._MotionInterface = MotionInterface(9)
                    self.SendResponse("Mode set to:" + self._Mode, ID)
                    self._MotionInterfaceThread = threading.Thread(target=self._MotionInterface.runThread)
                    self._MotionInterfaceThread.start()
                elif Command == "gmde":
                    self.SendResponse(self._Mode, ID)
                elif Command == "move":
                    self.SendResponse(self._MotionInterface.set_CurrentCommand(data[11:13]), ID)
                elif Command == "slen":
                    self._MotionInterface.setLength(data[11:14])
                    self.SendResponse("length has been set", ID)
                elif Command == "shgt":
                    self._MotionInterface.setHeight(data[11:14])
                    self.SendResponse("height has been set to:" + data[11:14], ID)
                elif Command == "sspd":
                    self._MotionInterface.setSpeed(data[11:17])
                    self.SendResponse("Speed has been set to:" + data[11:14], ID)
                elif Command == "spul":
                    self._MotionInterface.setDefaultPulse(data[11:17])
                    self.SendResponse("Defaultpulse has been updated", ID)
                elif Command == "cali":
                    self._MotionInterface.Calibreren(data[11:12], data[14:17])
                    self.SendResponse("Defaultpulse has been updated", ID)
                elif Command == "gimg":
                    self.SendResponse(self._Camera.takeImage(), ID)
                elif Command == "gifm":
                    self.SendResponse(self._Camera.getImageFromMemory(), ID)
                elif Command == "ping":
                    self.SendResponse("ping", ID)
                elif Command == "sdeg":
                    self.SendResponse(self._MotionInterface.setDegrees(data[11:13]), ID)
                elif Command == "gdeg":
                    self.SendResponse(self._MotionInterface.getDegrees(), ID)
                elif Command == "ggyr":
                    self.SendResponse(self._GyroData.getDegrees(), ID)
                elif Command == "smul":
                    self.SendResponse(self._MotionInterface.setMultiplier(data[11:12]), ID)
                elif Command == "gmul":
                    self.SendResponse(self._MotionInterface.getMultiplier(), ID)
                elif Command == "horn":
                    self._IOPIN.Horn()
                    self.SendResponse("toot toot!", ID)
                elif Command == "exit":
                    self.SendResponse("Exited", ID)
                    self.Exit()
                    self._Exit = True
                    exit()
                elif Command == "rebt":
                    self.SendResponse("Reboot", ID)
                    self.Exit()
                    self._Exit = True
                    self.Reboot()
                elif Command == "shtd":
                    self.SendResponse("Shutting down!", ID)
                    self.Exit()
                    self._Exit = True
                    self.Shutdown()
                else:
                    self.SendResponse("Could not execute command", ID)

                    
            time.sleep(0.001)
        print "CommandHandler says goodbye"

    def SendResponse(self, Response, ID):
        try:
            self.NetworkInterfaceBT.Send(Response, ID)
        except:
            pass

        try:
            self._NetworkInterface.Send(Response, ID)
        except:
            pass
    
    def setMode(self, Mode):
        self._Mode = Mode
        self._MotionInterface.exit()
        self._MotionInterfaceThread.join()

        if self._MotionInterface._currentModeInt != self._Mode:

             if int(self._Mode) == 1:
                 self._MotionInterface = MotionInterface(1)
             if int(self._Mode) == 2:
                self._MotionInterface = MotionInterface(2)
             if int(self._Mode) == 3:
                self._MotionInterface = MotionInterface(3)
                if int(self._Mode) == 4:
                    self._MotionInterface = MotionInterface(4)
                if int(self._Mode) == 5:
                    self._MotionInterface = MotionInterface(5)
                if int(self._Mode) == 6:
                    self._MotionInterface = MotionInterface(6)
                if int(self._Mode) == 7:
                    self._MotionInterface = MotionInterface(7)
                if int(self._Mode) == 8:
                   self._MotionInterface = MotionInterface(8)
                self._NetworkInterface.Send("Mode set to:" + self._Mode, ID)
                self._MotionInterfaceThread = threading.Thread(target=self._MotionInterface.runThread)
                self._MotionInterfaceThread.start()




    def Exit(self):
        self._NetworkInterface.Exit()
        self._Camera.Exit()
        self._MotionInterface.exit()

        print "Goodbye"
        
    def Reboot(self):
        self._NetworkInterface.Exit()
        self._Camera.Exit()
        try:
            call(["reboot"])
            print "Goodbye"

            print "BRB"
        except:
            print "Cannot reboot"
        
    def Shutdown(self):
        self._NetworkInterface.Exit()
        self._Camera.Exit()

        try:
            call(["poweroff"])
            print "Goodbye"
        except:
            print "Cannot shut down"

    def gcpu(self, ID):
        cmd = ["top -b -n 10 -d.2 | grep 'Cpu' |  awk 'NR==3{ print($2)}'"]
        result = subprocess.check_output(cmd,shell=True)
        self.SendResponse("CPU usage: " + result, ID)
        
                
            

