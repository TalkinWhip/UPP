from datetime import time, calendar
from dataclasses import dataclass
from . import commands, events
import itertools

class User:
    newid = itertools.count().next + 1 #probably won't persist, should pull from db.
    def __init__(self, name:str):
        
        # increment uid of previous instance, if none, set as 2
        self.uid = User.newid()
        self.saltedUID = str(self.uid) + str(self.orgNr)
        

        # TODO: create x users automatically
class Lock:
    def __init__(self, pin:int):
        self.pin = pin
        # self define lock_id --> pins from left to right, top to bottom, so lockers are consistantly numbered.
        # allocate user
        pass

class LedStrip:
    def __init__(self, pin:int, lock_id:int):
        # statically connect to lock
        pass
class Sensor:
    def __init__(self, pin:int, lock_id:int):
        # statically connect to lock 
        pass

