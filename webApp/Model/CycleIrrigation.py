from .Device import Device

class CycleIrrigation(Device):
    def __init__(self, id: int, description: str, name: str, pin: int, onoff: bool, blackoutTimes = []):
        super().__init__(id, name, description, pin, onoff)
        self.blackoutTimes = blackoutTimes

    def getBlackoutTimes(self):
        return self.blackoutTimes

    def toDict(self):
        return {"id":self.id,"description":self.description,"name":self.name,"pin":self.pin,"onoff":self.onoff,"blackouttimes":[t.toDict() for t in self.blackoutTimes]}



class BlackoutTime():
    def __init__(self, id, fk: int, blackoutStart, blackoutStop):
        self.id = id
        self.fk = fk
        self.blackoutStart = blackoutStart
        self.blackoutStop = blackoutStop

    def getFK(self) -> int:
        return self.fk

    def getBlackoutStartTime(self):
        return self.blackoutStart

    def getBlackoutStopTime(self):
        return self.blackoutStop

    def toDict(self):
        return {"id":self.id,"blackoutStart":self.blackoutStart,"blackoutStop":self.blackoutStop}