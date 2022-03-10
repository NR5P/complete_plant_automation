import sys
sys.path.append("..")
import unittest
from Model.CycleIrrigation import CycleIrrigation, BlackoutTime
from Model.TimedIrrigation import TimedIrrigation, IrrigationTime
from db import DB

class TestDBMethods(unittest.TestCase):
    def test_addCycleIrrigation(self):
        cycleIrrigation = CycleIrrigation(0, "test description", "test name")
        db = DB()
        returnval = db.addCycleIrrigation(cycleIrrigation)
        self.assertGreater(returnval, -1)

    def test_addCycleIrrigationBlackoutTimes(self):
        blackoutTime = BlackoutTime(0, 16, "12:13:14", "13:14:15")
        db = DB()
        returnval = db.addCycleIrrigationBlackoutTimes(blackoutTime)
        self.assertGreater(returnval, -1)

    def test_addTimedIrrigation(self):
        timedIrrigation = TimedIrrigation(0, "test name", "test description")
        db = DB()
        returnval = db.addTimedIrrigation(timedIrrigation)
        self.assertGreater(returnval, -1)

    def test_addTimedIrrigationTimes(self):
        irrigationTime = IrrigationTime(0, 1, "11:10:22", "12:00:00", "mtw")
        db = DB()
        returnval = db.addTimedIrrigationTimes(irrigationTime)
        self.assertGreater(returnval, -1)

    def test_getCycleIrrigationBlackoutTimesName(self):
        db = DB()
        cycleIrrigation = db.getCycleIrrigationBlackoutTimes(16)
        self.assertEqual("test name", cycleIrrigation.getName())
        #self.assertEqual("test description", cycleIrrigation.getDescription())

    def test_getTimedIrrigationTimesName(self):
        db = DB()
        timedIrrigation = db.getTimedIrrigationTimes(1)
        self.assertEqual("test name", timedIrrigation.getName())

    def test_getTimedIrrigationTimesDescription(self):
        db = DB()
        timedIrrigation = db.getTimedIrrigationTimes(1)
        self.assertEqual("test description", timedIrrigation.getDescription())

if __name__ == '__main__':
    unittest.main()
