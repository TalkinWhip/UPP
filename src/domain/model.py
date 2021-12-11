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