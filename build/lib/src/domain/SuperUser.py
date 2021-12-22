'''
using module as a singleton class.
Super user always has ID of 0
'''

__uid = 0
__saltedUID = ""
__userName = ""
__orgNr = 0

# orgNr - 4 digit code
 
def initialize(name:str, orgNrInput:int):
    if (len(str(orgNrInput))!=4):
        raise NameError("orgNr should be a 4 digit code")
    else:
        print("setting \n")
        global __userName
        global __orgNr
        global __saltedUID
        __userName += name
        __orgNr = orgNrInput
        __saltedUID = (str(__orgNr) + str(__uid))


def getUserName():
    return __userName
def getSaltedUID():
    return __saltedUID
def getUID():
    return __uid




