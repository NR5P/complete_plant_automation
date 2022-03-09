import time

class TimedIrrigation():
    def __init__(self, id, name, description, irrigationTimes = []):
        self.id = id
        self.description = description
        self.name = name
        self.irrigationTimes = irrigationTimes

    def getId(self) -> int:
        return self.id

    def getDaysToRun(self) -> str:
        return self.daysToRun

    def getDescription(self) -> str:
        return self.description

    def getName(self) -> str:
        return self.name

    def getIrrigationTimes(self):
        return self.irrigationTimes


class IrrigationTime():
    def __init__(self, id: int, fk: int, startTime, stopTime, daysToRun: str):
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