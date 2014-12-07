import threading
from threading import Semaphore

"""
    Buffer class
    contains synchronized list

    methods:
        Append()
        Pop()
"""


class NetworkBuffer(object):

    def __init__(self):
        self._Buffer = []                                   #List containing the buffer data
        self._BufferSemaphore = threading.Semaphore(1)      #Semaphore, makes sure only 1 Thread can read or write to the List at a time

    #Method appends data to the bounded List
    def Append(self, var):       
        self._BufferSemaphore.acquire()
        self._Buffer.append(var)
        self._BufferSemaphore.release()

    #Method pops the last inserted item from the list
    def Pop(self):
        self._BufferSemaphore.acquire()
        
        output = ""
        try:
            output = self._Buffer.pop()
        except:
            output = ""
        self._BufferSemaphore.release()
        
        return output

    
