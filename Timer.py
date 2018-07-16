import pickle
#import threading


class Timer():
    test = "test text" #TODO delete this later, this is just a test

    def __init__(self, pin, name):
        self.name = name
        self.pin = pin
        self.on = False
        self.test = False
        self.currentStateOn = False
        self.save()
        #self.threadStart()


    def __str__(self):
        return self.name


    def save(self):
        f = open(self.name, "wb")
        pickle.dump(self, f)
        f.close()

    def load(self):
        f = open(self.name, "rb")
        self = pickle.load(f)
        f.close()

    #def threadStart(self):
    #    t = threading.Thread(target=self.run)
    #    t.start()

    def run(self):
        for i in Timer.timerList:
            i.run()

