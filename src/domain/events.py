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
        # fromState = changeObject.previousState
        # toState = changeObject.state
        pass

    def toString(self):
        print(self.timestamp, ": ", self.changeObject,"/",self.changeObject.getID() ," : ", self.fromState, " --> ", self.toState)
class State:
    def __init__(self, states, transitions):
        self.states = states 
        self.transitions = transitions
        pass
    def change(trigger:str):
        #on trigger, go from state to destination, based on the transitions list
        pass