import pickle
#import threading


class Timer():
    timer_list = []

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

    @staticmethod
    def run():
        while True:
            for i in Timer.timer_list:
                i.run()

