import unittest
from ..Model.CycleIrrigation import CycleIrrigation, BlackoutTime
from ..db import DB

class TestDBMethods(unittest.TestCase):
    def test_addCycleIrrigation(self):
        cycleIrrigation = CycleIrrigation(0, "test description", "test name")
        db = DB()
        returnval = db.addCycleIrrigation(cycleIrrigation)
        self.assertGreater(returnval, -1)

if __name__ == '__main__':
    unittest.main()
