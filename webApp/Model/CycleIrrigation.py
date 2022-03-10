class CycleIrrigation():
    def __init__(self, id: int, description: str, name: str, blackoutTimes = []):
        self.id = id
        self.description = description
        self.name = name
        self.blackoutTimes = blackoutTimes

    def getDescription(self):
        return self.description

    def getName(self):
        return self.name

    def getBlackoutTimes(self):
        return self.blackoutTimes

    def toDict(self):
        return {"id":self.id,"description":self.description,"name":self.name,"blackouttimes":[t.toDict() for t in self.blackoutTimes]}



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