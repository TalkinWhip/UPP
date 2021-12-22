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
    def getID(self):
        return self.uid
class Lock:
    # STATES AND TRANSITIONS
    LOCKED = 'locked'
    UNLOCKED = 'unlocked'
    STATES = (LOCKED, UNLOCKED) 
    TRANSITIONS = [ # limited transitions between states based on different triggers - extendable
        {'trigger': 'lock', 'source':'unlocked','dest':'locked'},
        {'trigger': 'unlock', 'source': 'locked', 'dest':'unlocked'}
    ] 

    newid = itertools.count().next + 1 #probably won't persist, should pull from db.

    def __init__(self, pin:int):
        self.pin = pin
        self.state = events.State(Lock.STATES, Lock.TRANSITIONS)
        # self define lock_id --> pins from left to right, top to bottom, so lockers are consistantly numbered.
        self.lock_id = Lock.newid()
        # allocate user
        pass
    def lock(self):
        # turn off power from pin
        # log event
        event = events.Event(self)
        # update state machine
    def getID(self):
        return self.lock_id

        

class LedStrip:
    def __init__(self, pin:int, lock_id:int):
        # statically connect to lock
        pass
class Sensor:
    def __init__(self, pin:int, lock_id:int):
        # statically connect to lock 
        pass

