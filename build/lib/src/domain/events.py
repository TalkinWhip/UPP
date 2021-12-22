from time import strftime,gmtime
from dataclasses import dataclass
class Event:
    timestamp:str
    changeObject:object
    fromState:str
    toState:str
    
    def __init__(self, changeObject:object):
        self.changeObject = changeObject
        self.timestamp = strftime("%d-%m-%Y %H:%M:%S", gmtime())
        # log event on creation using toString
        pass

    def toString(self):
        print(self.timestamp, ": ", self.fromState, " --> ", self.toState)