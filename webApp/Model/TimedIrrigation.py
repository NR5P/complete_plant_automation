import time
from .Device import Device

class TimedIrrigation(Device):
    def __init__(self, id, name, description, irrigationTimes = []):
        super().__init__(id, name, description)
        self.irrigationTimes = irrigationTimes

    def getId(self) -> int:
        return self.id

    def getDaysToRun(self) -> str:
        return self.daysToRun

    def getIrrigationTimes(self):
        return self.irrigationTimes

    def toDict(self):
        return {"id":self.id,"description":self.description,"name":self.name,"irrigationTimes":[t.toDict() for t in self.irrigationTimes]}


class IrrigationTime():
    def __init__(self, id: int, fk: int, startTime, stopTime, daysToRun: str):
        self.id = id
        self.fk = fk
        self.startTime = startTime
        self.stopTime = stopTime
        self.daysToRun = daysToRun

    def getFK(self) -> int:
        return self.fk

    def getStartTime(self):
        return self.startTime

    def getStopTime(self):
        return self.stopTime

    def getDaysToRun(self):
        return self.daysToRun

    def toDict(self):
        return {"id":self.id,"startTime":self.startTime,"stopTime":self.stopTime, "daysToRun":self.daysToRun}