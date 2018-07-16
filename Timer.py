import pickle
import threading


class Timer():
    test = "test text"
    timerList = []

    def __init__(self, pin, name):
        self.name = name
        self.pin = pin
        self.on = False
        self.test = False
        self.currentStateOn = False
        self.save()
        self.threadStart()

        try:
            file = open(self.name, "rb")
            self = pickle.load(file)
            file.close
            Timer.timerList.append(self)
        except:                         #TODO add broader except clause, see again what rb, wb is and put it in save() function
            self.saveValve()
            Timer.timerList.append(self)

    def __str__(self):
        return self.name

    def save(self):
        file = open(self.name, "wb")
        pickle.dump(self, file)
        file.close()

    #def threadStart(self):
    #    t = threading.Thread(target=self.run)
    #    t.start()

    def run(self):
        for i in Timer.timerList:
            i.run()

