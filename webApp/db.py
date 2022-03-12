import mariadb, sys, time
sys.path.append("..")
from Model.CycleIrrigation import CycleIrrigation, BlackoutTime
from Model.TimedIrrigation import TimedIrrigation, IrrigationTime

class DB():
    def __init__(self):
        self.user = "admin"
        self.password = "Orangev8z"
        self.host = "localhost"
        self.port = 3306
        self.database = "bluefrog"

        try:
            self.conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)

        self.cur = self.conn.cursor()

    def addCycleIrrigation(self, cycleIrrigation) -> int: 
        try:
            self.cur.execute("INSERT INTO bluefrog.CycleIrrigation (Description, Name) VALUES (?,?);", (cycleIrrigation.getDescription(), cycleIrrigation.getName())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addCycleIrrigationBlackoutTimes(self, blackoutTimes) -> int: 
        try:
            #blackoutStart = time.strftime("%H:%M:%S", blackoutTimes.getBlackoutStartTime())
            #blackoutStop = time.strftime("%H:%M:%S", blackoutTimes.getBlackoutStopTime())
            self.cur.execute("INSERT INTO bluefrog.CycleIrrigationBlackoutTimes (CycleIrrigationFK, BlackoutStart, BlackoutStop) VALUES (?,?,?);", (blackoutTimes.getFK(), blackoutTimes.getBlackoutStartTime(), blackoutTimes.getBlackoutStopTime())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addTimedIrrigation(self, timedIrrigation) -> int: 
        try:
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigation (Name, Description) VALUES (?,?);", (timedIrrigation.getName(), timedIrrigation.getDescription())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addTimedIrrigationTimes(self, irrigationTime) -> int: 
        try:
            #startTime = time.strftime("%H:%M:%S", irrigationTime.getStartTime())
            #stopTime = time.strftime("%H:%M:%S", irrigationTime.getStopTime())
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigationTimes (TimedIrrigationFK, StartTime, StopTime, DaysToRun) VALUES (?,?,?,?);", (irrigationTime.getFK(), irrigationTime.getStartTime(), irrigationTime.getStopTime(), irrigationTime.getDaysToRun())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getCycleIrrigationBlackoutTimes(self, id: int):
        try:
            self.cur.execute("SELECT t1.id AS blackoutID, t1.BlackoutStart, t1.BlackoutStop, t1.CycleIrrigationFK, t2.id AS cycleID, t2.Description, t2.Name FROM CycleIrrigationBlackoutTimes AS t1 INNER JOIN CycleIrrigation AS t2 WHERE t1.CycleIrrigationFK = ?;", (id,)) 
            blackoutTimes = []
            cycledescription = ""
            cyclename = ""
            for blackoutID, BlackoutStart, BlackoutStop, CycleIrrigationFK, cycleID, Description, Name in self.cur:
                cycleid = cycleID
                cycledescription = Description
                cyclename = Name
                blackoutTime = BlackoutTime(blackoutID, cycleID, BlackoutStart, BlackoutStop)
                blackoutTimes.append(blackoutTime)
            cycleIrrigation = CycleIrrigation(id, cycledescription, cyclename, blackoutTimes) 
            return cycleIrrigation
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getAllCycleIrrigationTimes(self):
        try:
            self.cur.execute("SELECT t1.id AS blackoutID, t1.BlackoutStart, t1.BlackoutStop, t1.CycleIrrigationFK, t2.id AS cycleID, t2.Description, t2.Name FROM CycleIrrigation AS t2 LEFT JOIN CycleIrrigationBlackoutTimes AS t1 ON t1.CycleIrrigationFK = t2.id ORDER BY t1.CycleIrrigationFK, t2.id;") 
            blackoutTimesList = []
            cycleIrrigationList = []
            cycledescription = ""
            cyclename = ""
            cycleid = 0
            oldFK = None
            count = 0
            for blackoutID, BlackoutStart, BlackoutStop, CycleIrrigationFK, cycleID, Description, Name in self.cur:
                if (count != 0 and oldFK != CycleIrrigationFK) or CycleIrrigationFK == None:
                    cycleIrrigation = CycleIrrigation(cycleid, cycledescription, cyclename, blackoutTimesList) 
                    cycleIrrigationList.append(cycleIrrigation)
                    cycleid = 0
                    cycledescription = ""
                    cyclename = ""
                    blackoutTimesList = []
                oldFK = CycleIrrigationFK
                cycleid = cycleID
                cycledescription = Description
                cyclename = Name
                blackoutTime = BlackoutTime(blackoutID, cycleID, BlackoutStart, BlackoutStop)
                blackoutTimesList.append(blackoutTime)
                count+=1

            if count > 0: 
                cycleIrrigation = CycleIrrigation(cycleid, cycledescription, cyclename, blackoutTimesList) 
                cycleIrrigationList.append(cycleIrrigation)

            return cycleIrrigationList
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1


    def getTimedIrrigationTimes(self, id: int):
        try:
            self.cur.execute("SELECT t1.id AS TimedTimesID, t1.TimedIrrigationFK, t1.StartTime, t1.StopTime, t1.DaysToRun, t2.id As TimeID, t2.Name, t2.Description FROM TimedIrrigationTimes AS t1 INNER JOIN TimedIrrigation AS t2 WHERE t1.TimedIrrigationFK = ?", (id,)) 
            timedIrrigationTimes = []
            name = ""
            description = ""
            for TimedTimesID, TimedIrrigationFK, StartTime, StopTime, DaysToRun, TimeID, Name, Description in self.cur:
                name = Name
                description = Description
                #startTime = time.strptime(startTime, "%H:%M:%S")
                #stopTime = time.strptime(stopTime, "%H:%M:%S")
                irrigationTime = IrrigationTime(TimedTimesID, TimedIrrigationFK, StartTime, StopTime, DaysToRun)
                timedIrrigationTimes.append(irrigationTime)
            timedIrrigation = TimedIrrigation(id, Name, Description, timedIrrigationTimes) 
            return timedIrrigation
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1



