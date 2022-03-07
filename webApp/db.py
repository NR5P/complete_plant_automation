import mariadb, sys, time

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

    def addCycleIrrigation(self, daysToRun: str, description: str, name: str) -> int: 
        try:
            self.cur.execute("INSERT INTO bluefrog.CycleIrrigation (DaysToRun, Description, Name) VALUES (?,?,?);", (daysToRun, description, name)) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addCycleIrrigationBlackoutTimes(self, cycleIrrigationKey: int, blackoutStart: time, blackoutStop: time) -> int: 
        try:
            blackoutStart = time.strftime("%H:%M:%S", blackoutStart)
            blackoutStop = time.strftime("%H:%M:%S", blackoutStop)
            self.cur.execute("INSERT INTO bluefrog.CycleIrrigationBlackoutTimes (CycleIrrigationFK, BlackoutStart, BlackoutStop) VALUES (?,?,?);", (cycleIrrigationKey, blackoutStart, blackoutStop)) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addTimedIrrigation(self, name: str, description: str) -> int: 
        try:
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigation (Name, Description) VALUES (?,?);", (name, description)) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def addTimedIrrigationTimes(self, timedIrrigationFK: int, startTime: time, stopTime: time, daysToRun: str) -> int: 
        try:
            startTime = time.strftime("%H:%M:%S", startTime)
            stopTime = time.strftime("%H:%M:%S", stopTime)
            self.cur.execute("INSERT INTO bluefrog.TimedIrrigationTimes (TimedIrrigationFK, StartTime, StopTime, DaysToRun) VALUES (?,?,?);", (timedIrrigationFK, startTime, stopTime, daysToRun)) 
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getCycleIrrigation(self, id: int) -> Tuple[str, str, str]:
        try:
            self.cur.execute("SELECT * FROM CycleIrrigation WHERE id=?;", (id,)) 
            self.conn.commit()
            for DaysToRun, Description, Name in self.cur:
                return (DaysToRun, Description, Name)
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getCycleIrrigationBlackoutTimes(self, id: int) -> List[Tuple[int, time, time]]:
        try:
            self.cur.execute("SELECT * FROM CycleIrrigationBlackoutTimes WHERE CycleIrrigationFK=?;", (id,)) 
            self.conn.commit()
            times = []
            for id, BlackoutStart, BlackoutStop in self.cur:
                BlackoutStart = time.strptime(BlackoutStart, "%H:%M:%S")
                BlackoutStop = time.strptime(BlackoutStop, "%H:%M:%S")
                times.append((id, BlackoutStart, BlackoutStop))
            return times
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getTimedIrrigation(self, id: int) -> Tuple[str, str]:
        try:
            self.cur.execute("SELECT * FROM TimedIrrigation WHERE id=?;", (id,)) 
            self.conn.commit()
            for Name, Description in self.cur:
                return (Name, Description)
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1

    def getTimedIrrigationTimes(self, id: int) -> List[Tuple[int, time, time, str]]:
        try:
            self.cur.execute("SELECT * FROM TimedIrrigationTimes WHERE TimedIrrigationFK=?;", (id,)) 
            self.conn.commit()
            times = []
            for id, StartTime, StopTime, DaysToRun in self.cur:
                startTime = time.strptime(StartTime, "%H:%M:%S")
                stopTime = time.strptime(StopTime, "%H:%M:%S")
                times.append((id, startTime, stopTime, DaysToRun))
            return times
        except mariadb.Error as e:
            print(f"Error: {e}")
            return -1
