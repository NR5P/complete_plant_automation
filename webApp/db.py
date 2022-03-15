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
            self.cur.execute("INSERT INTO bluefrog.CycleIrrigation (Description, Name, pin, onoff) VALUES (?,?,?,?);", (cycleIrrigation.getDescription(), cycleIrrigation.getName(), cycleIrrigation.getPin(), cycleIrrigation.getOnoff())) 
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
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigation (Name, Description, pin, onoff) VALUES (?,?,?,?);", (timedIrrigation.getName(), timedIrrigation.getDescription(), timedIrrigation.getPin(), timedIrrigation.getOnoff())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addTimedIrrigationTimes(self, irrigationTime) -> int: 
        try:
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigationTimes (TimedIrrigationFK, StartTime, StopTime, DaysToRun) VALUES (?,?,?,?);", (irrigationTime.getFK(), irrigationTime.getStartTime(), irrigationTime.getStopTime(), irrigationTime.getDaysToRun())) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getAllCycleIrrigationTimes(self, passedID = None):
        try:
            if passedID == None:
                self.cur.execute("SELECT t1.id AS blackoutID, t1.BlackoutStart, t1.BlackoutStop, t1.CycleIrrigationFK, t2.id AS cycleID, t2.Description, t2.Name, t2.pin, t2.onoff FROM CycleIrrigation AS t2 LEFT JOIN CycleIrrigationBlackoutTimes AS t1 ON t1.CycleIrrigationFK = t2.id ORDER BY t1.CycleIrrigationFK, t2.id;") 
            else:
                self.cur.execute("SELECT t1.id AS blackoutID, t1.BlackoutStart, t1.BlackoutStop, t1.CycleIrrigationFK, t2.id AS cycleID, t2.Description, t2.Name, t2.pin, t2.onoff FROM CycleIrrigation AS t2 LEFT JOIN CycleIrrigationBlackoutTimes AS t1 ON t1.CycleIrrigationFK = t2.id WHERE t2.id = ? ORDER BY t1.CycleIrrigationFK, t2.id;",(passedID,)) 

            blackoutTimesList = []
            cycleIrrigationList = []
            cycledescription = ""
            cyclename = ""
            pin = None
            onoff = False
            cycleid = 0
            oldFK = None
            count = 0
            for blackoutID, BlackoutStart, BlackoutStop, CycleIrrigationFK, cycleID, Description, Name, pin, onoff in self.cur:
                if (count != 0 and oldFK != CycleIrrigationFK) or CycleIrrigationFK == None:
                    cycleIrrigation = CycleIrrigation(cycleid, cycledescription, cyclename, pin, onoff, blackoutTimesList) 
                    cycleIrrigationList.append(cycleIrrigation)
                    cycleid = 0
                    cycledescription = ""
                    cyclename = ""
                    pin = None
                    onoff = False
                    blackoutTimesList = []
                oldFK = CycleIrrigationFK
                cycleid = cycleID
                cycledescription = Description
                pin = pin
                onoff = onoff
                cyclename = Name
                blackoutTime = BlackoutTime(blackoutID, cycleID, BlackoutStart, BlackoutStop)
                blackoutTimesList.append(blackoutTime)
                count+=1

            if count > 0: 
                cycleIrrigation = CycleIrrigation(cycleid, cycledescription, cyclename, pin, onoff, blackoutTimesList) 
                cycleIrrigationList.append(cycleIrrigation)

            return cycleIrrigationList
        except mariadb.Error as e:
            print(f"Error get all cycle irrigation: {e}")
            return -1


    def getAllTimedIrrigationTimes(self, passedID = None):
        try:
            if passedID == None:
                self.cur.execute("SELECT t1.id AS TimedTimesID, t1.TimedIrrigationFK, t1.StartTime, t1.StopTime, t1.DaysToRun, t2.id As TimeID, t2.Name, t2.Description, t2.pin, t2.onoff FROM TimedIrrigation AS t2 LEFT JOIN TimedIrrigationTimes AS t1 ON t1.TimedIrrigationFK = t2.id ORDER BY t1.TimedIrrigationFK, t2.id;") 
            else:
                self.cur.execute("SELECT t1.id AS TimedTimesID, t1.TimedIrrigationFK, t1.StartTime, t1.StopTime, t1.DaysToRun, t2.id As TimeID, t2.Name, t2.Description, t2.pin, t2.onoff FROM TimedIrrigation AS t2 LEFT JOIN TimedIrrigationTimes AS t1 ON t1.TimedIrrigationFK = t2.id WHERE t2.id = ? ORDER BY t1.TimedIrrigationFK, t2.id;",(passedID,)) 

            timedIrrigationTimesList = []
            timedIrrigationList = []
            name = ""
            description = ""
            pin = None
            onoff = False
            timedID = 0
            oldFK = None
            count = 0
            for TimedTimesID, TimedIrrigationFK, StartTime, StopTime, DaysToRun, TimeID, Name, Description, pin, onoff in self.cur:
                if (count != 0 and oldFK != TimedIrrigationFK) or TimedIrrigationFK == None:
                    timedIrrigation = TimedIrrigation(timedID, name, description, pin, onoff, timedIrrigationTimesList)
                    timedIrrigationList.append(timedIrrigation)
                    timedID = 0
                    description = ""
                    pin = None
                    onoff = False
                    name = ""
                    timedIrrigationTimesList = []
                oldFK = TimedIrrigationFK
                timedID = TimeID
                name = Name
                description = Description
                pin = pin
                onoff = onoff
                irrigationTime = IrrigationTime(TimedTimesID, TimedIrrigationFK, StartTime, StopTime, DaysToRun)
                timedIrrigationTimesList.append(irrigationTime)
                count+=1

            if count > 0:
                timedIrrigation = TimedIrrigation(timedID, name, description, pin, onoff, timedIrrigationTimesList)
                timedIrrigationList.append(timedIrrigation)


            return timedIrrigationList
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1



