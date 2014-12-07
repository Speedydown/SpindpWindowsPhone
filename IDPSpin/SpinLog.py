import datetime
import threading
from threading import Semaphore

class SpinLog(object):

    def __init__(self):
        self._Log = self.ReadLogFromFile()
        self._LogSemaphore = threading.Semaphore(1)

    def append(self, String):
        self._LogSemaphore.acquire()
        self._Log = str(self._Log) + "[" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "]: " + String + " \n"
        self._LogSemaphore.release()
        self.WriteLogToFile()

    def get(self):
        self._LogSemaphore.acquire()
        log = self._Log
        self._LogSemaphore.release()
        return log

    def clear(self):
        self._LogSemaphore.acquire()
        self._Log = ""
        self._LogSemaphore.release()
        self.WriteLogToFile()

    def ReadLogFromFile(self):
        try:
            SpInOSLog = open('spInOSLog.txt', 'r') 
            return SpInOSLog.read()
        except:
            return ""
    
    def WriteLogToFile(self):
        self._LogSemaphore.acquire()
        try:
            SpInOSLog = open('spInOSLog.txt', 'w')
            SpInOSLog.write(self._Log)
            SpInOSLog.close()
        except:
            print "Error writing log to file"
        
        self._LogSemaphore.release()
